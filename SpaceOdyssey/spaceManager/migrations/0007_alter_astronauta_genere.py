# Generated by Django 3.2.3 on 2021-06-09 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaceManager', '0006_alter_astronauta_genere'),
    ]

    operations = [
        migrations.AlterField(
            model_name='astronauta',
            name='genere',
            field=models.CharField(choices=[('H', 'H'), ('D', 'D'), ('?', '?')], max_length=1),
        ),
    ]