from django.contrib import admin
from.models import Refrigeradora
from.models import Microonda
from.models import Lavadora
from.models import Televisor
from.models import Licuadora
from.models import Cocina
from.models import Contacto
# Register your models here.
class proyectAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')

admin.site.register(Refrigeradora, proyectAdmin)
admin.site.register(Microonda, proyectAdmin)
admin.site.register(Lavadora, proyectAdmin)
admin.site.register(Televisor, proyectAdmin)
admin.site.register(Licuadora, proyectAdmin)
admin.site.register(Cocina, proyectAdmin)
admin.site.register(Contacto)