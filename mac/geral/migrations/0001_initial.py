# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import filebrowser.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Destaque",
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
                ("nome", models.CharField(max_length=50)),
                (
                    "imagem",
                    models.ImageField(null=True, upload_to=b"inicial/", blank=True),
                ),
                ("texto", models.TextField(null=True, blank=True)),
                ("texto_en", models.TextField(null=True, blank=True)),
                ("url", models.CharField(max_length=100)),
                ("visivel", models.BooleanField(default=False)),
                ("ordem", models.SmallIntegerField()),
            ],
            options={
                "ordering": ["nome"],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="Foto",
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
                ("nome", models.CharField(max_length=100)),
                (
                    "thumbnail",
                    filebrowser.fields.FileBrowseField(
                        max_length=200, null=True, blank=True
                    ),
                ),
                (
                    "image",
                    filebrowser.fields.FileBrowseField(
                        max_length=200, null=True, blank=True
                    ),
                ),
            ],
            options={
                "ordering": ["nome"],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="Material",
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
                ("nome", models.CharField(max_length=50)),
            ],
            options={
                "ordering": ["nome"],
                "verbose_name": "Material",
                "verbose_name_plural": "Materiais",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="Tecnica",
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
                ("nome", models.CharField(max_length=50)),
            ],
            options={
                "ordering": ["nome"],
                "verbose_name": "Tecnica",
                "verbose_name_plural": "Tecnicas",
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="Tela",
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
                ("image", models.ImageField(upload_to=b"geral/")),
            ],
            options={
                "ordering": ["titulo"],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name="Tipo",
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
                ("nome", models.CharField(max_length=50)),
            ],
            options={
                "ordering": ["nome"],
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name="tecnica",
            name="categoria",
            field=models.ForeignKey(to="geral.Tipo", on_delete=models.CASCADE),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name="material",
            name="categoria",
            field=models.ForeignKey(to="geral.Tipo", on_delete=models.CASCADE),
            preserve_default=True,
        ),
    ]
