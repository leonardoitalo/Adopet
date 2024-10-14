from django.core.management.base import BaseCommand
from faker import Faker
import random
from adopet.models import Pet, Tutor, Shelter, Adoption


class Command(BaseCommand):
    help = "Popula o banco de dados com dados falsos para Pet, Tutor e Abrigo."

    def handle(self, *args, **options):
        fake = Faker("pt_BR")

        # Populando Tutores
        for _ in range(30):
            name = fake.name()
            email = fake.email()
            password = fake.password()
            Tutor.objects.create(name=name, email=email, password=password)
        tutors = list(Tutor.objects.all())

        # Populando Abrigos
        for _ in range(10):
            name = fake.company()
            Shelter.objects.create(name=name)
        shelters = list(Shelter.objects.all())

        # Polando Pets
        for _ in range(25):
            name = fake.first_name()
            age = f"{random.randint(1, 10)} anos"
            size = random.choice(["pequeno", "médio", "grande", "médio/grande"])
            description = random.choice(
                ["Calmo", "Educado", "Ativo", "Carinhoso", "Brincalhão"]
            )
            address = fake.address()
            adopted = False
            image = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQktXg5_v8-L9AslphhrFvphE12SWkGl-_Jig&usqp=CAU"
            shelter = random.choice(shelters)
            Pet.objects.create(
                name=name,
                age=age,
                size=size,
                description=description,
                address=address,
                adopted=adopted,
                image=image,
                shelter=shelter,
            )
        pets = list(Pet.objects.all())

        # Populando Adoções
        for _ in range(10):
            date = fake.date()
            pet = random.choice(pets)
            tutor = random.choice(tutors)
            Adoption.objects.create(date=date, pet=pet, tutor=tutor)

        self.stdout.write(self.style.SUCCESS("Banco de dados populado com sucesso!"))
