from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission

class TutorManager(BaseUserManager):
    """Gerenciador de usuários customizado para o modelo Tutor"""
    def create_user(self, email, name, password=None, **extra_fields):
        if not email:
            raise ValueError("O usuário deve ter um email")
        email = self.normalize_email(email)
        tutor = self.model(email=email, name=name, **extra_fields)
        tutor.set_password(password)  # Armazena a senha com hash
        tutor.save(using=self._db)
        return tutor

    def create_superuser(self, email, name, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, name, password, **extra_fields)

class Tutor(AbstractBaseUser, PermissionsMixin):
    """Modelo de Tutor que será usado no sistema de adoção de pets"""
    name = models.CharField(max_length=100, blank=False, unique=True)
    email = models.EmailField(max_length=100, blank=False, default='tutor@tutor.com', unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        related_name="tutor_set",  # Evita conflito com auth.User.groups
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="tutor_permissions_set",  # Evita conflito com auth.User.user_permissions
        blank=True
    )

    objects = TutorManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    
class Shelter(models.Model):
    name = models.CharField(max_length=100, blank=False)
    
    def __str__(self):
        return self.name


class Pet(models.Model):
    SIZE = (
        ('pequeno', 'P'),
        ('médio', 'M'),
        ('grande', 'G'),
        ('médio/grande', 'MG'),
    )

    name = models.CharField(max_length=100, blank=False)
    age = models.CharField(max_length=10, blank=False)
    size = models.CharField(max_length=100, choices=SIZE, blank=False, null=False, default='SM')
    description = models.CharField(max_length=100, blank=False, null=False)
    address = models.CharField(max_length=100, blank=False, null=False)
    adopted = models.BooleanField(blank=False, default=False, editable=False)
    image = models.URLField(max_length=200, blank=False)
    shelter = models.ForeignKey(Shelter, on_delete=models.CASCADE) # One-to-Many relationship

    def __str__(self):
        return self.name
    
    
class Adoption(models.Model):
    date = models.DateField(auto_now=False, auto_now_add=True)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        self.pet.adopted = True
        self.pet.save()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.tutor.name} adotou {self.pet.name}"
    
    class Meta:
        ordering = ['date'] 
    