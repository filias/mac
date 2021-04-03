# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("geral", "__first__"),
        ("artistas", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Aniversario",
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
                ("data", models.DateField(null=True, blank=True)),
                ("descricao", models.TextField(null=True, blank=True)),
                (
                    "convite",
                    models.FileField(null=True, upload_to=b"convites/", blank=True),
                ),
                (
                    "catalogo",
                    models.FileField(null=True, upload_to=b"catalogos/", blank=True),
                ),
                (
                    "fotos",
                    models.ManyToManyField(to="geral.Foto", null=True, blank=True),
                ),
                (
                    "trofeu",
                    models.ForeignKey(
                        blank=True,
                        to="artistas.Obra",
                        null=True,
                        on_delete=models.CASCADE,
                    ),
                ),
            ],
            options={
                "ordering": ["data"],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="Galeria",
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
                ("nome", models.CharField(max_length=200)),
                ("descricao", models.TextField(null=True, blank=True)),
                ("rua", models.CharField(max_length=50, null=True, blank=True)),
                ("cidade", models.CharField(max_length=30, null=True, blank=True)),
                ("cod_postal", models.CharField(max_length=8, null=True, blank=True)),
                ("telefone", models.CharField(max_length=13, null=True, blank=True)),
                ("email", models.EmailField(max_length=75, null=True, blank=True)),
                ("horario", models.CharField(max_length=200, null=True, blank=True)),
                ("mapa", models.URLField(null=True, blank=True)),
                (
                    "fotos",
                    models.ManyToManyField(to="geral.Foto", null=True, blank=True),
                ),
            ],
            options={
                "ordering": ["nome"],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="Premiado",
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
                ("nome", models.CharField(max_length=150)),
                ("profissao", models.CharField(max_length=50, null=True, blank=True)),
                (
                    "foto",
                    models.ForeignKey(
                        blank=True, to="geral.Foto", null=True, on_delete=models.CASCADE
                    ),
                ),
            ],
            options={
                "ordering": ["nome"],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="Premio",
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
                ("nome", models.CharField(max_length=150)),
                ("descricao", models.TextField(null=True, blank=True)),
                (
                    "aniversario",
                    models.ForeignKey(
                        blank=True,
                        to="galeria.Aniversario",
                        null=True,
                        on_delete=models.CASCADE,
                    ),
                ),
                (
                    "foto",
                    models.ForeignKey(
                        blank=True, to="geral.Foto", null=True, on_delete=models.CASCADE
                    ),
                ),
                (
                    "premiado",
                    models.ForeignKey(
                        blank=True,
                        to="galeria.Premiado",
                        null=True,
                        on_delete=models.CASCADE,
                    ),
                ),
            ],
            options={
                "ordering": ["nome"],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="Staff",
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
                ("nome", models.CharField(max_length=150)),
                ("funcao", models.CharField(max_length=50, null=True, blank=True)),
                ("email", models.EmailField(max_length=75, null=True, blank=True)),
                ("telefone", models.CharField(max_length=13, null=True, blank=True)),
                (
                    "foto",
                    models.ForeignKey(
                        blank=True, to="geral.Foto", null=True, on_delete=models.CASCADE
                    ),
                ),
            ],
            options={
                "ordering": ["nome"],
            },
            bases=(models.Model,),
        ),
    ]
