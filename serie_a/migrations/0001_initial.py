# Generated by Django 4.2.6 on 2023-10-18 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atalanta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=30)),
                ('birth_of_date', models.DateTimeField()),
                ('age', models.PositiveIntegerField(default=15)),
                ('citizenship', models.CharField(max_length=50)),
                ('position', models.CharField(choices=[('G', 'Goalkeeper'), ('D', 'Defender'), ('M', 'Midfielder'), ('F', 'Forward')], max_length=1)),
                ('number', models.PositiveIntegerField(max_length=99)),
                ('foot', models.CharField(choices=[('R', 'Right'), ('L', 'Left'), ('B', 'Both')], max_length=1)),
                ('image', models.ImageField(upload_to='media/')),
            ],
            options={
                'verbose_name': 'Atalanta',
                'verbose_name_plural': 'Atalanta',
            },
        ),
    ]