# Generated by Django 3.1.2 on 2023-05-21 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_carrito_usuario'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AddField(
            model_name='producto',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

