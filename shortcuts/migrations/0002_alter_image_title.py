# Generated by Django 4.1.7 on 2023-03-16 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortcuts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='title',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
