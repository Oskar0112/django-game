# Generated by Django 3.2.4 on 2023-06-10 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_page'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setting',
            name='api_key',
        ),
        migrations.RemoveField(
            model_name='setting',
            name='secret_key',
        ),
    ]