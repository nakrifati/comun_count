# Generated by Django 3.0.4 on 2020-03-12 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('count_page', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='com',
            name='date',
            field=models.DateField(),
        ),
    ]
