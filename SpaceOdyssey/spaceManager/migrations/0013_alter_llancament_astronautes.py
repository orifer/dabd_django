# Generated by Django 3.2.3 on 2021-06-10 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaceManager', '0012_auto_20210610_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='llancament',
            name='astronautes',
            field=models.ManyToManyField(db_table='spaceManager_assignat', related_name='astronautes', to='spaceManager.Astronauta'),
        ),
    ]