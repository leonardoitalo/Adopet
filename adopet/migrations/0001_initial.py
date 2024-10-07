# Generated by Django 5.0.3 on 2024-10-06 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('email', models.EmailField(default='tutor@tutor.com', max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
