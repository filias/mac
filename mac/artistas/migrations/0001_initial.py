# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geral', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artista',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nome', models.CharField(max_length=100)),
                ('bio_resumo', models.TextField(null=True, blank=True)),
                ('bio_resumo_en', models.TextField(null=True, blank=True)),
                ('biografia', models.FileField(null=True, upload_to=b'biografias/', blank=True)),
                ('artista_mac', models.BooleanField(default=False)),
                ('foto', models.ForeignKey(related_name='foto', blank=True, to='geral.Foto', null=True, on_delete=models.CASCADE)),
                ('foto_obra', models.ForeignKey(related_name='foto_obra', blank=True, to='geral.Foto', null=True, on_delete=models.CASCADE)),
                ('telas', models.ManyToManyField(to='geral.Tela', null=True, blank=True)),
                ('tipo', models.ManyToManyField(to='geral.Tipo')),
            ],
            options={
                'ordering': ['nome'],
                'verbose_name': 'Artista',
                'verbose_name_plural': 'Artistas',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Obra',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=100)),
                ('ano', models.CharField(max_length=12)),
                ('descricao', models.TextField(null=True, blank=True)),
                ('descricao_en', models.TextField(null=True, blank=True)),
                ('altura', models.IntegerField(null=True, blank=True)),
                ('largura', models.IntegerField(null=True, blank=True)),
                ('profundidade', models.IntegerField(null=True, blank=True)),
                ('estado', models.CharField(max_length=1, choices=[('A', 'Acervo'), ('E', 'Exposicao'), ('C', 'Coleccao')])),
                ('autor', models.ForeignKey(to='artistas.Artista', on_delete=models.CASCADE)),
                ('foto', models.ForeignKey(blank=True, to='geral.Foto', null=True, on_delete=models.CASCADE)),
                ('materiais', models.ManyToManyField(to='geral.Material', null=True, blank=True)),
                ('tecnicas', models.ManyToManyField(to='geral.Tecnica', null=True, blank=True)),
                ('tipo', models.ForeignKey(to='geral.Tipo', on_delete=models.CASCADE)),
            ],
            options={
                'ordering': ['autor', '-ano'],
                'verbose_name': 'Obra',
                'verbose_name_plural': 'Obras',
            },
            bases=(models.Model,),
        ),
    ]
