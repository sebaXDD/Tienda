# Generated by Django 3.1.2 on 2023-05-21 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_auto_20230521_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=3000),
        ),
    ]
