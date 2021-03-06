# Generated by Django 3.2.3 on 2021-06-08 13:44

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('spaceManager', '0004_pais_plataforma'),
    ]

    operations = [
        migrations.CreateModel(
            name='Astronauta',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('cognom', models.CharField(max_length=50)),
                ('naixement', models.DateField(default=django.utils.timezone.now)),
                ('genere', models.CharField(max_length=1)),
                ('altura', models.IntegerField()),
                ('grup_sanguini', models.CharField(max_length=3)),
                ('agencia', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='spaceManager.agencia')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='spaceManager.pais')),
            ],
        ),
    ]
