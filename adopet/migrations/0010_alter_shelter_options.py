# Generated by Django 5.0.3 on 2024-10-10 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adopet', '0009_alter_tutor_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shelter',
            options={'ordering': ['name']},
        ),
    ]
