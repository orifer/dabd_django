# Generated by Django 3.2.3 on 2021-06-10 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('spaceManager', '0010_rename_platafora_llancament_plataforma'),
    ]

    operations = [
        migrations.AddField(
            model_name='agencia',
            name='astronautes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='astronautes', to='spaceManager.astronauta'),
        ),
        migrations.AddField(
            model_name='astronauta',
            name='llancaments',
            field=models.ManyToManyField(related_name='spacemanager_astronauta_related', related_query_name='spacemanager_astronautas', to='spaceManager.Llancament'),
        ),
        migrations.AddField(
            model_name='llancament',
            name='astronautes',
            field=models.ManyToManyField(related_name='spacemanager_llancament_related', related_query_name='spacemanager_llancaments', to='spaceManager.Astronauta'),
        ),
    ]
