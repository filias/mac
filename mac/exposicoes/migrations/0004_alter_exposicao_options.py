# Generated by Django 3.2 on 2021-10-06 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exposicoes', '0003_auto_20210403_1319'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exposicao',
            options={'ordering': ['-data_inicio'], 'verbose_name': 'Exposição', 'verbose_name_plural': 'Exposições'},
        ),
    ]