# Generated by Django 4.1.5 on 2023-01-21 11:42

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to=app.models.upload_path)),
                ('photo_name', models.CharField(max_length=40)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('album', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='app.album')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
