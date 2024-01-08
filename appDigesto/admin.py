from django.contrib import admin

# Register your models here.

from .models import Digesto 
from .models import Categoria
from .models import Subcategoria  
# Register your models here.


admin.site.register(Digesto)
admin.site.register(Categoria)
admin.site.register(Subcategoria)