# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artistas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artista',
            name='telas',
            field=models.ManyToManyField(to='geral.Tela', blank=True),
        ),
        migrations.AlterField(
            model_name='obra',
            name='materiais',
            field=models.ManyToManyField(to='geral.Material', blank=True),
        ),
        migrations.AlterField(
            model_name='obra',
            name='tecnicas',
            field=models.ManyToManyField(to='geral.Tecnica', blank=True),
        ),
    ]
