# Generated by Django 5.1.2 on 2024-10-26 16:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_authormodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.authormodel'),
        ),
    ]