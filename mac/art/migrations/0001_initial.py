# Generated by Django 3.2.8 on 2021-10-08 18:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='nome', max_length=100)),
                ('bio_short_pt', models.TextField(blank=True, db_column='bio_resumo', null=True)),
                ('bio_short_en', models.TextField(blank=True, db_column='bio_resumo_en', null=True)),
                ('bio', models.FileField(blank=True, db_column='biografia', null=True, upload_to='biografias/')),
                ('mac_artist', models.BooleanField(db_column='artista_mac', default=False)),
            ],
            options={
                'verbose_name': 'Artista',
                'verbose_name_plural': 'Artistas',
                'db_table': 'artistas_artista',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ArtMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='nome', max_length=50)),
            ],
            options={
                'verbose_name': 'Material',
                'verbose_name_plural': 'Materiais',
                'db_table': 'geral_material',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ArtTechnique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='nome', max_length=50)),
            ],
            options={
                'verbose_name': 'Técnica',
                'verbose_name_plural': 'Técnicas',
                'db_table': 'geral_tecnica',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ArtType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='nome', max_length=50)),
            ],
            options={
                'db_table': 'geral_tipo',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Canvas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='titulo', max_length=200)),
                ('image', models.ImageField(upload_to='geral/')),
            ],
            options={
                'db_table': 'geral_tela',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='ArtWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='titulo', max_length=100)),
                ('year', models.CharField(db_column='ano', max_length=12)),
                ('description', models.TextField(blank=True, db_column='descricao', null=True)),
                ('description_en', models.TextField(blank=True, db_column='descricao_en', null=True)),
                ('height', models.IntegerField(blank=True, db_column='altura', null=True)),
                ('width', models.IntegerField(blank=True, db_column='largura', null=True)),
                ('depth', models.IntegerField(blank=True, db_column='profundidade', null=True)),
                ('state', models.CharField(choices=[('A', 'Acervo'), ('E', 'Exposicao'), ('C', 'Coleccao')], db_column='estado', max_length=1)),
                ('art_work_type', models.ForeignKey(db_column='tipo_id', on_delete=django.db.models.deletion.CASCADE, to='art.arttype')),
                ('author', models.ForeignKey(db_column='autor_id', on_delete=django.db.models.deletion.CASCADE, to='art.artist')),
            ],
            options={
                'verbose_name': 'Obra',
                'verbose_name_plural': 'Obras',
                'db_table': 'artistas_obra',
                'ordering': ['author', '-year'],
            },
        ),
    ]
