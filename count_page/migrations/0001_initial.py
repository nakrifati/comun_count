# Generated by Django 3.0.4 on 2020-03-12 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Com',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('electric', models.CharField(default='', max_length=256)),
                ('water_h', models.CharField(default='', max_length=256)),
                ('water_c', models.CharField(default='', max_length=256)),
                ('waste', models.CharField(default='', max_length=256)),
                ('date', models.CharField(default='', max_length=256)),
            ],
        ),
    ]
