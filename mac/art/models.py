from django.db import models
from django.utils.translation import ugettext_lazy as _


STATE_CHOICES = (
    ("A", "Acervo"),
    ("E", "Exposicao"),
    ("C", "Coleccao"),
)


class Artist(models.Model):
    name = models.CharField(max_length=100, db_column="nome")
    bio_short_pt = models.TextField(null=True, blank=True, db_column="bio_resumo")
    bio_short_en = models.TextField(null=True, blank=True, db_column="bio_resumo_en")
    foto = models.ForeignKey(
        "gallery.Foto", null=True, related_name="foto", on_delete=models.CASCADE
    )
    foto_art_work = models.ForeignKey(
        "gallery.Foto", null=True, related_name="foto_obra", on_delete=models.CASCADE, db_column="foto_obra_id"
    )
    bio = models.FileField(upload_to="biografias/", null=True, blank=True, db_column="biografia")
    art_type = models.ManyToManyField("ArtType", db_table="artistas_artista_tipo")
    canvases = models.ManyToManyField("Canvas", blank=True, db_table="artistas_artista_telas")
    mac_artist = models.BooleanField(default=False, db_column="artista_mac")

    def __str__(self):
        return self.name

    def tem_acervo(self):
        return ArtWork.objects.filter(author=self, estado="A")

    class Meta:
        db_table = "artistas_artista"
        ordering = ["name"]
        verbose_name = _("Artista")
        verbose_name_plural = _("Artistas")


class ArtWork(models.Model):
    author = models.ForeignKey("Artist", on_delete=models.CASCADE, db_column="autor_id")
    title = models.CharField(max_length=100, db_column="titulo")
    year = models.CharField(max_length=12, db_column="ano")
    description = models.TextField(null=True, blank=True, db_column="descricao")
    description_en = models.TextField(null=True, blank=True, db_column="descricao_en")
    art_work_type = models.ForeignKey("ArtType", on_delete=models.CASCADE, db_column="tipo_id")
    techniques = models.ManyToManyField("ArtTechnique", blank=True, db_table="artistas_obra_tecnicas")
    height = models.IntegerField(null=True, blank=True, db_column="altura")
    width = models.IntegerField(null=True, blank=True, db_column="largura")
    depth = models.IntegerField(null=True, blank=True, db_column="profundidade")
    materials = models.ManyToManyField("ArtMaterial", blank=True, db_table="artistas_obra_materiais")
    state = models.CharField(max_length=1, choices=STATE_CHOICES, db_column="estado")
    foto = models.ForeignKey("gallery.Foto", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "%s - %s" % (self.author.name, self.title)

    class Meta:
        db_table = "artistas_obra"
        ordering = ["author", "-year"]
        verbose_name = _("Obra")
        verbose_name_plural = _("Obras")


class Canvas(models.Model):
    title = models.CharField(max_length=200, db_column="titulo")
    image = models.ImageField(upload_to="geral/")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "geral_tela"
        ordering = ["title"]


class ArtType(models.Model):
    name = models.CharField(max_length=50, db_column="nome")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "geral_tipo"
        ordering = ["name"]


class ArtTechnique(models.Model):
    name = models.CharField(max_length=50, db_column="nome")
    category = models.ForeignKey("ArtType", on_delete=models.CASCADE, db_column="categoria_id")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "geral_tecnica"
        ordering = ["name"]
        verbose_name = _("Técnica")
        verbose_name_plural = _("Técnicas")


class ArtMaterial(models.Model):
    name = models.CharField(max_length=50, db_column="nome")
    category = models.ForeignKey("ArtType", on_delete=models.CASCADE, db_column="categoria_id")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "geral_material"
        ordering = ["name"]
        verbose_name = _("Material")
        verbose_name_plural = _("Materiais")
