# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aniversario',
            name='fotos',
            field=models.ManyToManyField(to='geral.Foto', blank=True),
        ),
        migrations.AlterField(
            model_name='galeria',
            name='fotos',
            field=models.ManyToManyField(to='geral.Foto', blank=True),
        ),
    ]
