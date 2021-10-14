import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
from filebrowser.fields import FileBrowseField


class Gallery(models.Model):
    name = models.CharField(max_length=200, db_column="nome")
    description = models.TextField(null=True, blank=True, db_column="descricao")
    street = models.CharField(max_length=50, null=True, blank=True, db_column="rua")
    city = models.CharField(max_length=30, null=True, blank=True, db_column="cidade")
    zip_code = models.CharField(
        max_length=8, null=True, blank=True, db_column="cod_postal"
    )
    phone = models.CharField(max_length=13, null=True, blank=True, db_column="telefone")
    email = models.EmailField(max_length=75, null=True, blank=True)
    opening_times = models.CharField(
        max_length=200, null=True, blank=True, db_column="horario"
    )
    fotos = models.ManyToManyField("Foto", blank=True, db_table="galeria_galeria_fotos")
    map = models.URLField(null=True, blank=True, db_column="mapa")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "galeria_galeria"
        ordering = ["name"]


EXHIBITION_TYPE_CHOICES = (
    ("I", "Individual"),
    ("C", "Colectiva"),
)


class Exhibition(models.Model):
    title = models.CharField(max_length=200, db_column="titulo")
    exhibition_type = models.CharField(
        max_length=1, choices=EXHIBITION_TYPE_CHOICES, blank=True, db_column="tipo"
    )
    art_type = models.ManyToManyField(
        "art.ArtType", db_table="exposicoes_exposicao_tipo_arte"
    )
    description = models.TextField(null=True, blank=True, db_column="descricao")
    description_en = models.TextField(null=True, blank=True, db_column="descricao_en")
    start_date = models.DateField("data de inicio", db_column="data_inicio")
    end_date = models.DateField("data de fim", db_column="data_fim")
    galleries = models.ManyToManyField(
        "Gallery", db_table="exposicoes_exposicao_galerias"
    )
    artists = models.ManyToManyField(
        "art.Artist", blank=True, db_table="exposicoes_exposicao_artistas"
    )
    art_works = models.ManyToManyField(
        "art.ArtWork", blank=True, db_table="exposicoes_exposicao_obras"
    )
    fotos = models.ManyToManyField(
        "Foto", blank=True, db_table="exposicoes_exposicao_fotos"
    )
    catalog = models.ForeignKey(
        "Publication",
        null=True,
        blank=True,
        limit_choices_to={"tipo__exact": "Catalogo"},
        on_delete=models.CASCADE,
        db_column="catalogo_id",
    )
    invitation = models.FileField(
        upload_to="convites/", null=True, blank=True, db_column="convite"
    )
    press_release = models.FileField(upload_to="press_releases/", null=True, blank=True)
    canvases = models.ManyToManyField(
        "art.Canvas", db_table="exposicoes_exposicao_telas"
    )

    def __str__(self):
        return self.title

    @property
    def is_current(self):
        return self.start_date <= datetime.date.today() <= self.end_date

    @property
    def is_past(self):
        return self.end_date < datetime.date.today()

    @property
    def is_future(self):
        return self.start_date > datetime.date.today()

    class Meta:
        db_table = "exposicoes_exposicao"
        ordering = ["-start_date"]
        verbose_name = _("Exposição")
        verbose_name_plural = _("Exposições")


class Awardee(models.Model):
    name = models.CharField(max_length=150, db_column="nome")
    profession = models.CharField(
        max_length=50, null=True, blank=True, db_column="profissao"
    )
    foto = models.ForeignKey(
        "gallery.Foto", null=True, blank=True, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "galeria_premiado"
        ordering = ["name"]


class Anniversary(models.Model):
    date = models.DateField(null=True, blank=True, db_column="data")
    description = models.TextField(null=True, blank=True, db_column="descricao")
    trophy = models.ForeignKey(
        "art.ArtWork",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        db_column="trofeu_id",
    )
    invitation = models.FileField(
        upload_to="convites/", null=True, blank=True, db_column="convite"
    )
    catalog = models.FileField(
        upload_to="catalogos/", null=True, blank=True, db_column="catalogo"
    )
    fotos = models.ManyToManyField(
        "Foto", blank=True, db_table="galeria_aniversario_fotos"
    )

    def __str__(self):
        return self.description

    class Meta:
        db_table = "galeria_aniversario"
        ordering = ["date"]


class Award(models.Model):
    name = models.CharField(max_length=150, db_column="nome")
    description = models.TextField(null=True, blank=True, db_column="descricao")
    awardee = models.ForeignKey(
        "Awardee",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        db_column="premiado_id",
    )
    anniversary = models.ForeignKey(
        "Anniversary",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        db_column="aniversario_id",
    )
    foto = models.ForeignKey("Foto", null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "galeria_premio"
        ordering = ["name"]


PUBLICATION_TYPE_CHOICES = (
    ("Catalogo", "Catalogo"),
    ("Imprensa", "Imprensa"),
    ("Critica", "Critica"),
)


class Publication(models.Model):
    title = models.CharField(max_length=200, db_column="titulo")
    author = models.CharField(max_length=100, null=True, blank=True, db_column="autor")
    editor = models.CharField(max_length=100, null=True, blank=True)
    artist = models.ForeignKey(
        "art.Artist",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        db_column="artista_id",
    )
    publication_type = models.CharField(
        max_length=10, choices=PUBLICATION_TYPE_CHOICES, db_column="tipo"
    )
    date = models.DateField(null=True, blank=True, db_column="data")
    description = models.TextField(null=True, blank=True, db_column="descricao")
    description_en = models.TextField(null=True, blank=True, db_column="descricao_en")
    file = models.FileField(
        upload_to="publicacoes/",
        max_length=200,
        null=True,
        blank=True,
        db_column="ficheiro",
    )

    def __str__(self):
        return self.title

    class Meta:
        db_table = "publicacoes_publicacao"
        ordering = ["-date"]
        verbose_name = _("Publicação")
        verbose_name_plural = _("Publicações")


class Text(models.Model):
    title = models.CharField(max_length=500, db_column="titulo")
    text = models.TextField(null=True, blank=True, db_column="texto")
    text_en = models.TextField(null=True, blank=True, db_column="texto_en")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "publicacoes_texto"
        ordering = ["title"]


class Link(models.Model):
    name = models.CharField(max_length=200, db_column="nome")
    url = models.URLField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "publicacoes_link"
        ordering = ["name"]


class Foto(models.Model):
    name = models.CharField(max_length=100, db_column="nome")
    thumbnail = FileBrowseField(
        max_length=200,
        directory="/",
        extensions=[".jpg", ".jpeg", ".gif", ".png", ".tif", ".tiff"],
        blank=True,
        null=True,
    )
    image = FileBrowseField(
        max_length=200,
        directory="/",
        extensions=[".jpg", ".jpeg", ".gif", ".png", ".tif", ".tiff"],
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "geral_foto"
        ordering = ["name"]


class Snippet(models.Model):
    name = models.CharField(max_length=50, db_column="nome")
    image = models.ImageField(
        upload_to="inicial/", null=True, blank=True, db_column="imagem"
    )
    text = models.TextField(null=True, blank=True, db_column="texto")
    text_en = models.TextField(null=True, blank=True, db_column="texto_en")
    url = models.CharField(max_length=100)
    is_visible = models.BooleanField(default=False, db_column="visivel")
    ordering = models.SmallIntegerField(db_column="ordem")

    def __str__(self):
        return self.url

    class Meta:
        db_table = "geral_destaque"
        ordering = ["name"]
