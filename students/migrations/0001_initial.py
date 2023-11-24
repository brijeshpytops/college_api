# Generated by Django 4.2.7 on 2023-11-24 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=200)),
                ('mobile', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
    ]
