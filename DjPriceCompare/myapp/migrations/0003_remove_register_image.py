# Generated by Django 4.2 on 2023-04-16 09:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_history'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='image',
        ),
    ]
