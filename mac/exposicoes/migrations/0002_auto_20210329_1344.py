# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("exposicoes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exposicao",
            name="artistas",
            field=models.ManyToManyField(to="artistas.Artista", blank=True),
        ),
        migrations.AlterField(
            model_name="exposicao",
            name="fotos",
            field=models.ManyToManyField(to="geral.Foto", blank=True),
        ),
        migrations.AlterField(
            model_name="exposicao",
            name="obras",
            field=models.ManyToManyField(to="artistas.Obra", blank=True),
        ),
    ]
