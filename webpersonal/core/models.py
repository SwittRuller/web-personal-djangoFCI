from django.db import models

# Create your models here.
class Refrigeradora(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    precio = models.IntegerField(verbose_name="Precio")  # Cambiar a IntegerField
    image = models.ImageField(verbose_name="Imagen", upload_to="proyects")
    url = models.URLField(null=True, blank=True, verbose_name="URL")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha actualizada")
    capacidad = models.CharField(null=True, blank=True, max_length=100, verbose_name="capacidad")
    altura = models.CharField(null=True, blank=True, max_length=100, verbose_name="altura")
    ancho = models.CharField(null=True, blank=True, max_length=100, verbose_name="ancho")
    peso = models.CharField(null=True, blank=True, max_length=100, verbose_name="peso")
    consumo = models.CharField(null=True, blank=True, max_length=100, verbose_name="consumo")
    garantia = models.CharField(null=True, blank=True, max_length=100, verbose_name="garantia")

    class Meta:
        verbose_name = 'refrigeradoras'
        verbose_name_plural = 'refrigeradoras'

    def __str__(self):
        return self.title

class Microonda(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    precio = models.IntegerField(verbose_name="Precio")  # Cambiar a IntegerField
    image = models.ImageField(verbose_name="Imagen", upload_to="proyects")
    url = models.URLField(null=True, blank=True, verbose_name="URL")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha actualizada")
    capacidad = models.CharField(null=True, blank=True, max_length=100, verbose_name="capacidad")
    altura = models.CharField(null=True, blank=True, max_length=100, verbose_name="altura")
    ancho = models.CharField(null=True, blank=True, max_length=100, verbose_name="ancho")
    peso = models.CharField(null=True, blank=True, max_length=100, verbose_name="peso")
    consumo = models.CharField(null=True, blank=True, max_length=100, verbose_name="consumo")
    garantia = models.CharField(null=True, blank=True, max_length=100, verbose_name="garantia")

    class Meta:
        verbose_name = 'microondas'
        verbose_name_plural = 'microondas'

    def __str__(self):
        return self.title
    
class Lavadora(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    precio = models.IntegerField(verbose_name="Precio")  # Cambiar a IntegerField
    image = models.ImageField(verbose_name="Imagen", upload_to="proyects")
    url = models.URLField(null=True, blank=True, verbose_name="URL")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha actualizada")
    capacidad = models.CharField(null=True, blank=True, max_length=100, verbose_name="capacidad")
    altura = models.CharField(null=True, blank=True, max_length=100, verbose_name="altura")
    ancho = models.CharField(null=True, blank=True, max_length=100, verbose_name="ancho")
    peso = models.CharField(null=True, blank=True, max_length=100, verbose_name="peso")
    consumo = models.CharField(null=True, blank=True, max_length=100, verbose_name="consumo")
    garantia = models.CharField(null=True, blank=True, max_length=100, verbose_name="garantia")

    class Meta:
        verbose_name = 'lavadoras'
        verbose_name_plural = 'lavadoras'

    def __str__(self):
        return self.title
        
class Televisor(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    precio = models.IntegerField(verbose_name="Precio")  # Cambiar a IntegerField
    image = models.ImageField(verbose_name="Imagen", upload_to="proyects")
    url = models.URLField(null=True, blank=True, verbose_name="URL")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha actualizada")
    sistema = models.CharField(null=True, blank=True, max_length=100, verbose_name="Sistema Operativo")
    altura = models.CharField(null=True, blank=True, max_length=100, verbose_name="altura")
    ancho = models.CharField(null=True, blank=True, max_length=100, verbose_name="ancho")
    peso = models.CharField(null=True, blank=True, max_length=100, verbose_name="peso")
    consumo = models.CharField(null=True, blank=True, max_length=100, verbose_name="consumo")
    garantia = models.CharField(null=True, blank=True, max_length=100, verbose_name="garantia")

    class Meta:
        verbose_name = 'televisors'
        verbose_name_plural = 'televisors'

    def __str__(self):
        return self.title

class Licuadora(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    precio = models.IntegerField(verbose_name="Precio")  # Cambiar a IntegerField
    image = models.ImageField(verbose_name="Imagen", upload_to="proyects")
    url = models.URLField(null=True, blank=True, verbose_name="URL")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha actualizada")
    velocidades = models.CharField(null=True, blank=True, max_length=100, verbose_name="velocidades")
    altura = models.CharField(null=True, blank=True, max_length=100, verbose_name="altura")
    vaso = models.CharField(null=True, blank=True, max_length=100, verbose_name="vaso")
    peso = models.CharField(null=True, blank=True, max_length=100, verbose_name="peso")
    consumo = models.CharField(null=True, blank=True, max_length=100, verbose_name="consumo")
    garantia = models.CharField(null=True, blank=True, max_length=100, verbose_name="garantia")

    class Meta:
        verbose_name = 'licuadoras'
        verbose_name_plural = 'licuadoras'

    def __str__(self):
        return self.title
    
class Cocina(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    description = models.TextField(verbose_name="Descripción")
    precio = models.IntegerField(verbose_name="Precio")  # Cambiar a IntegerField
    image = models.ImageField(verbose_name="Imagen", upload_to="proyects")
    url = models.URLField(null=True, blank=True, verbose_name="URL")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha actualizada")
    estufa = models.CharField(null=True, blank=True, max_length=100, verbose_name="Numero de Estufas")
    tipo_gas_induccion = models.CharField(null=True, blank=True, max_length=100, verbose_name="Tipo de Cocina")
    altura = models.CharField(null=True, blank=True, max_length=100, verbose_name="altura")
    ancho = models.CharField(null=True, blank=True, max_length=100, verbose_name="ancho")
    peso = models.CharField(null=True, blank=True, max_length=100, verbose_name="peso")
    consumo = models.CharField(null=True, blank=True, max_length=100, verbose_name="consumo")
    garantia = models.CharField(null=True, blank=True, max_length=100, verbose_name="garantia")

    class Meta:
        verbose_name = 'cocinas'
        verbose_name_plural = 'cocinas'

    def __str__(self):
        return self.title

class Contacto(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="nombre")
    correo = models.EmailField(verbose_name="correo")
    producto = models.CharField(max_length=1000, verbose_name="producto")  # Considera cambiar este nombre
    comentario = models.CharField(max_length=200, verbose_name="comentario")

    class Meta:
        verbose_name = 'contacto'
        verbose_name_plural = 'contactos'

    def __str__(self):
        return self.nombre
