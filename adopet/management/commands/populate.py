from django.core.management.base import BaseCommand
from faker import Faker
import random
from adopet.models import Pet, Tutor, Shelter

class Command(BaseCommand):
    help = 'Popula o banco de dados com dados falsos para Pet, Tutor e Abrigo.'

    def handle(self, *args, **options):
        fake = Faker('pt_BR')

        # Populando Tutores
        for _ in range(20):
            name = fake.name()
            email = fake.email()
            password = fake.password()
            Tutor.objects.create(name=name, email=email, password=password)
    
        # Populando Abrigos
        for _ in range(5):
            name = fake.company()
            Shelter.objects.create(name=name)
            
                # Populando Pets
        shelters = list(Shelter.objects.all())  # Obtendo todos os abrigos disponíveis

        # Populando Pets
        for _ in range(20):
            name = fake.first_name()
            age = f'{random.randint(1, 10)} anos'
            size = random.choice(['pequeno', 'médio', 'grande', 'médio/grande'])
            description = random.choice(['Calmo', 'Educado', 'Ativo', 'Carinhoso', 'Brincalhão'])
            address = fake.address()
            adopted = False
            image = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQktXg5_v8-L9AslphhrFvphE12SWkGl-_Jig&usqp=CAU'
            shelter = random.choice(shelters)
            Pet.objects.create(name=name, age=age, size=size, description=description, address=address, adopted=adopted, image=image, shelter=shelter)

        self.stdout.write(self.style.SUCCESS('Banco de dados populado com sucesso!'))
