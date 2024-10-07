# Generated by Django 5.0.3 on 2024-10-07 05:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopet', '0002_shelter_pet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adoption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adopet.pet')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adopet.tutor')),
            ],
        ),
    ]
