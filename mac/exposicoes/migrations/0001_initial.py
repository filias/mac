# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ("geral", "__first__"),
        ("galeria", "__first__"),
        ("publicacoes", "__first__"),
        ("artistas", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Exposicao",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("titulo", models.CharField(max_length=200)),
                (
                    "tipo",
                    models.CharField(
                        blank=True,
                        max_length=1,
                        choices=[("I", "Individual"), ("C", "Colectiva")],
                    ),
                ),
                ("descricao", models.TextField(null=True, blank=True)),
                ("descricao_en", models.TextField(null=True, blank=True)),
                ("data_inicio", models.DateField(verbose_name="data de inicio")),
                ("data_fim", models.DateField(verbose_name="data de fim")),
                (
                    "convite",
                    models.FileField(null=True, upload_to=b"convites/", blank=True),
                ),
                (
                    "press_release",
                    models.FileField(
                        null=True, upload_to=b"press_releases/", blank=True
                    ),
                ),
                (
                    "artistas",
                    models.ManyToManyField(
                        to="artistas.Artista", null=True, blank=True
                    ),
                ),
                (
                    "catalogo",
                    models.ForeignKey(
                        blank=True,
                        to="publicacoes.Publicacao",
                        null=True,
                        on_delete=models.CASCADE,
                    ),
                ),
                (
                    "fotos",
                    models.ManyToManyField(to="geral.Foto", null=True, blank=True),
                ),
                ("galerias", models.ManyToManyField(to="galeria.Galeria")),
                (
                    "obras",
                    models.ManyToManyField(to="artistas.Obra", null=True, blank=True),
                ),
                ("telas", models.ManyToManyField(to="geral.Tela")),
                ("tipo_arte", models.ManyToManyField(to="geral.Tipo")),
            ],
            options={
                "ordering": ["-data_inicio"],
                "verbose_name": "Exposicao",
                "verbose_name_plural": "Exposicoes",
            },
            bases=(models.Model,),
        ),
    ]
