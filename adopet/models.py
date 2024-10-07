from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class Tutor(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    email = models.EmailField(max_length=100, blank=False, default='tutor@tutor.com')
    password = models.CharField(max_length=100, blank=False)
    
    def __str__(self):
        return self.name
    
    def clean(self):
        # Validação do nome
        if not self.name.isalpha():
            raise ValidationError(_('Name must only contain alphabetic characters.'))

        # Validação da senha (mínimo de 8 caracteres)
        if len(self.password) < 8:
            raise ValidationError(_('Password must be at least 8 characters long.'))

    def save(self, *args, **kwargs):
        self.clean()  # Chama a validação antes de salvar
        super().save(*args, **kwargs)

class Shelter(models.Model):
    name = models.CharField(max_length=100, blank=False)
    
    def __str__(self):
        return self.name

class Pet(models.Model):
    SIZE = (
        ('SM', 'Small'),
        ('M', 'Medium'),
        ('B', 'Big'),
    )
    name = models.CharField(max_length=100, blank=False)
    age = models.CharField(max_length=100, blank=False)
    size = models.CharField(max_length=2, choices=SIZE, blank=False, null=False, default='SM')
    description = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    adopted = models.BooleanField(blank=False, default=False)
    image = models.URLField(max_length=200, blank=False)
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    