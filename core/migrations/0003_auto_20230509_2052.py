# Generated by Django 3.1.2 on 2023-05-10 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20230503_1341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='vencimiento',
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='producto',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
    ]