# Generated by Django 3.2.3 on 2021-06-10 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spaceManager', '0015_auto_20210610_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pais',
            name='nom',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
