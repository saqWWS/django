# Generated by Django 4.2.6 on 2023-10-15 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Work', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('color', models.CharField(max_length=50)),
                ('crated_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('description', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
