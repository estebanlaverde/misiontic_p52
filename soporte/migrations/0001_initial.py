# Generated by Django 3.2.7 on 2021-11-16 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PersonaSoporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='PQR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=32)),
                ('comentario', models.TextField(blank=True)),
                ('creacion', models.DateField()),
                ('persona_soporte', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='soporte.personasoporte')),
            ],
        ),
    ]
