# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artistas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=200)),
                ('url', models.URLField()),
            ],
            options={
                'ordering': ['nome'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publicacao',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=200)),
                ('autor', models.CharField(max_length=100, null=True, blank=True)),
                ('editor', models.CharField(max_length=100, null=True, blank=True)),
                ('tipo', models.CharField(max_length=10, choices=[('Newsletter', 'Newsletter'), ('Catalogo', 'Catalogo'), ('Monografia', 'Monografia'), ('Imprensa', 'Imprensa'), ('Critica', 'Critica')])),
                ('data', models.DateField(null=True, blank=True)),
                ('descricao', models.TextField(null=True, blank=True)),
                ('descricao_en', models.TextField(null=True, blank=True)),
                ('ficheiro', models.FileField(max_length=200, null=True, upload_to=b'publicacoes/', blank=True)),
                ('artista', models.ForeignKey(blank=True, to='artistas.Artista', null=True, on_delete=models.CASCADE)),
            ],
            options={
                'ordering': ['-data'],
                'verbose_name': 'Publicacao',
                'verbose_name_plural': 'Publicacoes',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Texto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=500)),
                ('texto', models.TextField(null=True, blank=True)),
                ('texto_en', models.TextField(null=True, blank=True)),
            ],
            options={
                'ordering': ['titulo'],
            },
            bases=(models.Model,),
        ),
    ]
