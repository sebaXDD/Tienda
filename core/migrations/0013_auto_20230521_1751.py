# Generated by Django 3.1.2 on 2023-05-21 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_merge_20230521_1751'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='producto',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(max_length=30000),
        ),
    ]