from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Digesto
from .forms import DigestoForm
from django.contrib import messages
# Create your views here.


def signup(request):
    if request.method == "GET":
        return render(request, "signup.html", {"form": UserCreationForm})

    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                # registrar usuario
                user = User.objects.create_user(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                login(request, user)
                return redirect("createDigesto")
            except:
                return render(
                    request,
                    "signup.html",
                    {"form": UserCreationForm, "error": "el usuario ya existe"},
                )

        return render(
            request,
            "signup.html",
            {"form": UserCreationForm, "error": "contrasena no coinciden"},
        )
    
def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {"form": AuthenticationForm})
    else:
        user = authenticate(
            request,
            username=request.POST["username"],
            password=request.POST["password"],
        )
        if user is None:
            return render(
                request,
                "signin.html",
                {
                    "form": AuthenticationForm,
                    "error": "usuario o contrasena incorrecto",
                },
            )
        else:
            login(request, user)
            return redirect("createDigesto")






def out(request):
    logout(request)
    return redirect("/")

@login_required
def createDigesto(request):
   username = request.user.username
   digestos=  Digesto.objects.all().order_by('-id')[:5]
   if request.method == "GET":
        return render(request, 'createDigesto.html', {"form": DigestoForm , 'username':username,'digestos':digestos})
   else:
        try:
            
            form = DigestoForm(request.POST,request.FILES)
            new_Digesto = form.save(commit=False)
            new_Digesto.usuario = request.user
            new_Digesto.save()
            messages.success(request, 'Digesto creado exitosamente.')
            return redirect('createDigesto')
        except ValueError:
            messages.error(request, 'Hubo un error al crear el Digesto.')
            return render(request, 'createDigesto.html', {"form": DigestoForm,'username':username,'digestos':digestos})



def home(request):
    username = request.user.username
    return render(request, "base.html",{'username':username})


@login_required
def digestos(request):
    username = request.user.username
    digestos=  Digesto.objects.all().order_by('-id')
    return render(request, "digestos.html",{'username':username ,'digestos':digestos})

@login_required
def digesto_detalle(request ,id):
     username = request.user.username
     if request.method == 'GET':
        digesto=get_object_or_404(Digesto, pk=id)
        form=DigestoForm(instance= digesto)
        return render(request, "digesto_detalle.html",{'username':username ,'digesto':digesto ,'form':form})
     else:
        try:
            digesto=get_object_or_404(Digesto, pk=id ,usuario=request.user)
            form=DigestoForm(request.POST,request.FILES, instance= digesto)
            form.save()
            messages.success(request, 'Digesto Actualizado exitosamente.')
            return redirect('digestos')
        except ValueError:
            messages.error(request, 'Hubo un error al actualizar el Digesto.')
            return render(request, "digesto_detalle.html",{'username':username ,'digesto':digesto ,'form':form,
                                                           'error':'error al actualizar digesto'})


@login_required
def delete_digesto(request, id):
    digesto=get_object_or_404(Digesto, pk=id ,usuario=request.user)
    print()
    if request.method == 'POST':
      try:
        digesto.delete()
        messages.success(request, 'Digesto eliminado correctamente.')
        return redirect('digestos')
      except ValueError:
           messages.error(request, 'Hubo un error al eliminar el Digesto.')
           return render(request, "digesto_detalle.html",{'digesto':digesto,
                                                           'error':'error al actualizar digesto'})