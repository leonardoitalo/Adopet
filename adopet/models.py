from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from .validators import validate_age

class Tutor(models.Model):
    name = models.CharField(max_length=100, blank=False, unique=True)
    email = models.EmailField(max_length=100, blank=False, default='tutor@tutor.com')
    password = models.CharField(max_length=100, blank=False)
    
    def __str__(self):
        return self.name
    
    def clean(self):
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
        ('S', 'Small'),
        ('M', 'Medium'),
        ('B', 'Big'),
        ('SM', 'Small/Medium'),
        ('MB', 'Medium/Big'),
    )

    name = models.CharField(max_length=100, blank=False)
    age = models.CharField(max_length=10, blank=False, validators=[validate_age])
    size = models.CharField(max_length=2, choices=SIZE, blank=False, null=False, default='SM')
    description = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    adopted = models.BooleanField(blank=False, default=False)
    image = models.URLField(max_length=200, blank=False)
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE) # One-to-Many relationship

    def __str__(self):
        return self.name
    
class Adoption(models.Model):
    data = models.DateField(auto_now=False, auto_now_add=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        self.pet.adopted = True
        self.pet.save()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.tutor.name} adotou {self.pet.name}"
    