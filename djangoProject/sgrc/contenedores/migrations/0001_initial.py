# Generated by Django 3.0.2 on 2020-03-05 05:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contenedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(help_text='Descripción del Contenedor', max_length=100, unique=True)),
                ('activo', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last created.', verbose_name='modified at')),
                ('weight', models.FloatField(blank=True, default=0, null=True)),
                ('lat', models.FloatField(blank=True, default=0, null=True)),
                ('lng', models.FloatField(blank=True, default=0, null=True)),
                ('colaborador', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Contenedores',
            },
        ),
    ]
