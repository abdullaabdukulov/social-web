# Generated by Django 4.1.7 on 2023-03-11 13:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ShortCuts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(blank=True, max_length=200)),
                ('url', models.URLField(max_length=250)),
                ('image', models.ImageField(upload_to='images/%Y/%m/%d/')),
                ('desc', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='short_created', to=settings.AUTH_USER_MODEL)),
                ('users_like', models.ManyToManyField(blank=True, related_name='short_liked', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_at'],
            },
        ),
        migrations.AddIndex(
            model_name='shortcuts',
            index=models.Index(fields=['-created_at'], name='shortcuts_s_created_63054e_idx'),
        ),
    ]
