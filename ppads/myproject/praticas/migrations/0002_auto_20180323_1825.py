# Generated by Django 2.0.3 on 2018-03-23 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('praticas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='endereço',
            new_name='endereco',
        ),
    ]
