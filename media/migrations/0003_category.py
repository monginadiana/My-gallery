# Generated by Django 3.2.7 on 2021-11-27 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0002_auto_20211127_0048'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
    ]
