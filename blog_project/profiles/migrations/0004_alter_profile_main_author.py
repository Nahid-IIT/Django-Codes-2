# Generated by Django 5.0.6 on 2024-05-29 01:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
        ('profiles', '0003_rename_author_profile_main_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='main_author',
            field=models.OneToOneField(default='A', on_delete=django.db.models.deletion.CASCADE, to='authors.author'),
        ),
    ]
