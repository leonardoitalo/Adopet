# Generated by Django 5.0.3 on 2024-10-07 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adopet', '0003_adoption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adoption',
            name='data',
            field=models.DateField(auto_now_add=True),
        ),
    ]
