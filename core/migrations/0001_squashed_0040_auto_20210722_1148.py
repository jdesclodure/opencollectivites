# Generated by Django 3.2.7 on 2021-09-09 13:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [
        ("core", "0001_initial"),
        ("core", "0002_editor_platform_scope"),
        ("core", "0003_auto_20201030_1618"),
        ("core", "0004_auto_20210119_1338"),
        ("core", "0005_auto_20210119_1430"),
        ("core", "0006_auto_20210119_1435"),
        ("core", "0007_auto_20210119_1515"),
        ("core", "0008_auto_20210121_0912"),
        ("core", "0009_auto_20210121_0913"),
        ("core", "0010_auto_20210121_0951"),
        ("core", "0011_auto_20210121_1448"),
        ("core", "0012_metadata"),
        ("core", "0013_auto_20210122_0955"),
        ("core", "0014_auto_20210122_0957"),
        ("core", "0015_auto_20210122_1011"),
        ("core", "0016_auto_20210122_1012"),
        ("core", "0017_auto_20210122_1029"),
        ("core", "0018_auto_20210122_1038"),
        ("core", "0019_auto_20210122_1104"),
        ("core", "0020_auto_20210122_1109"),
        ("core", "0021_auto_20210122_1320"),
        ("core", "0022_auto_20210122_1322"),
        ("core", "0023_source_document_type"),
        ("core", "0024_auto_20210122_1447"),
        ("core", "0025_auto_20210122_1449"),
        ("core", "0026_auto_20210122_1527"),
        ("core", "0027_auto_20210122_1559"),
        ("core", "0028_auto_20210122_1604"),
        ("core", "0029_auto_20210122_1606"),
        ("core", "0030_auto_20210122_1808"),
        ("core", "0031_auto_20210122_1830"),
        ("core", "0032_auto_20210122_1908"),
        ("core", "0033_auto_20210122_1911"),
        ("core", "0034_auto_20210122_1915"),
        ("core", "0035_auto_20210208_0853"),
        ("core", "0036_auto_20210212_1601"),
        ("core", "0037_auto_20210225_1717"),
        ("core", "0038_auto_20210225_1846"),
        ("core", "0039_auto_20210326_1447"),
        ("core", "0040_auto_20210722_1148"),
    ]

    initial = True

    dependencies = [
        ("feeds", "0008_auto_20201027_1623"),
        ("francedata", "0001_initial"),
        ("feeds", "0009_auto_20201104_1023"),
    ]

    operations = [
        migrations.CreateModel(
            name="Topic",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="nom")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date de création"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="date de modification"
                    ),
                ),
                (
                    "icon_path",
                    models.CharField(
                        max_length=255, null=True, verbose_name="Chemin de l’icône"
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "thématique",
            },
        ),
        migrations.CreateModel(
            name="Editor",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="nom")),
                ("logo", models.ImageField(blank=True, upload_to="logos")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date de création"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="date de modification"
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "éditeur",
            },
        ),
        migrations.CreateModel(
            name="Scope",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="nom")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date de création"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="date de modification"
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "portée",
            },
        ),
        migrations.CreateModel(
            name="DataYear",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("year", models.PositiveSmallIntegerField(verbose_name="année")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date de création"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="date de modification"
                    ),
                ),
            ],
            options={
                "ordering": ["year"],
                "verbose_name": "millésime",
            },
        ),
        migrations.CreateModel(
            name="DocumentType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="nom")),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date de création"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="date de modification"
                    ),
                ),
                (
                    "icon_path",
                    models.CharField(
                        max_length=255, null=True, verbose_name="Chemin de l’icône"
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "type de document",
                "verbose_name_plural": "types de document",
            },
        ),
        migrations.CreateModel(
            name="Source",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100, verbose_name="titre")),
                ("url", models.URLField(blank=True, null=True, verbose_name="URL")),
                (
                    "editor",
                    models.ManyToManyField(to="core.Editor", verbose_name="éditeur"),
                ),
                (
                    "rss_feed",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="feeds.source",
                        verbose_name="flux RSS",
                    ),
                ),
                (
                    "last_update",
                    models.DateField(
                        default=datetime.date.today, verbose_name="dernière mise à jour"
                    ),
                ),
                (
                    "scope",
                    models.ManyToManyField(
                        blank=True, to="core.Scope", verbose_name="portée"
                    ),
                ),
                (
                    "topics",
                    models.ManyToManyField(
                        blank=True, to="core.Topic", verbose_name="sujet"
                    ),
                ),
                (
                    "years",
                    models.ManyToManyField(
                        blank=True, to="core.DataYear", verbose_name="année"
                    ),
                ),
                (
                    "base_domain",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="domaine"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date de création"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="date de modification"
                    ),
                ),
                (
                    "communes",
                    models.ManyToManyField(
                        blank=True,
                        to="francedata.Commune",
                        verbose_name="commune",
                    ),
                ),
                (
                    "departements",
                    models.ManyToManyField(
                        blank=True,
                        to="francedata.Departement",
                        verbose_name="département",
                    ),
                ),
                (
                    "epcis",
                    models.ManyToManyField(
                        blank=True, to="francedata.Epci", verbose_name="EPCI"
                    ),
                ),
                (
                    "regions",
                    models.ManyToManyField(
                        blank=True,
                        to="francedata.Region",
                        verbose_name="région",
                    ),
                ),
                (
                    "document_type",
                    models.ManyToManyField(
                        blank=True,
                        related_name="documents_type",
                        to="core.DocumentType",
                        verbose_name="type des documents inclus",
                    ),
                ),
                (
                    "source_type",
                    models.ManyToManyField(
                        blank=True,
                        related_name="source_type",
                        to="core.DocumentType",
                        verbose_name="type de source",
                    ),
                ),
            ],
            options={
                "ordering": ["title"],
            },
        ),
        migrations.CreateModel(
            name="PageType",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date de création"
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="nom")),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="date de modification"
                    ),
                ),
            ],
            options={
                "ordering": ["name"],
                "verbose_name": "type de page",
                "verbose_name_plural": "types de page",
            },
        ),
        migrations.CreateModel(
            name="Document",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="titre"
                    ),
                ),
                (
                    "url",
                    models.URLField(max_length=512, unique=True, verbose_name="URL"),
                ),
                (
                    "is_published",
                    models.BooleanField(
                        blank=True, null=True, verbose_name="est publié"
                    ),
                ),
                (
                    "last_update",
                    models.DateField(
                        blank=True, null=True, verbose_name="dernière mise à jour"
                    ),
                ),
                (
                    "rss_post",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="feeds.post",
                        verbose_name="Post associé",
                    ),
                ),
                (
                    "scope",
                    models.ManyToManyField(
                        blank=True, to="core.Scope", verbose_name="portée"
                    ),
                ),
                (
                    "topics",
                    models.ManyToManyField(
                        blank=True, to="core.Topic", verbose_name="sujet"
                    ),
                ),
                (
                    "document_type",
                    models.ManyToManyField(
                        blank=True,
                        to="core.DocumentType",
                        verbose_name="type de document",
                    ),
                ),
                (
                    "source",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.source",
                    ),
                ),
                ("years", models.ManyToManyField(blank=True, to="core.DataYear")),
                (
                    "base_domain",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="domaine"
                    ),
                ),
                (
                    "publication_pages",
                    models.ManyToManyField(
                        blank=True,
                        to="core.PageType",
                        verbose_name="pages de publication",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date de création"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="date de modification"
                    ),
                ),
                (
                    "regions",
                    models.ManyToManyField(
                        blank=True, to="francedata.Region", verbose_name="région"
                    ),
                ),
                (
                    "departements",
                    models.ManyToManyField(
                        blank=True,
                        to="francedata.Departement",
                        verbose_name="département",
                    ),
                ),
                (
                    "communes",
                    models.ManyToManyField(
                        blank=True, to="francedata.Commune", verbose_name="commune"
                    ),
                ),
                (
                    "epcis",
                    models.ManyToManyField(
                        blank=True, to="francedata.Epci", verbose_name="EPCI"
                    ),
                ),
                ("body", models.TextField(blank=True)),
                (
                    "image_url",
                    models.URLField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="URL de l’image",
                    ),
                ),
                (
                    "weight",
                    models.PositiveSmallIntegerField(default=100, verbose_name="poids"),
                ),
            ],
            options={
                "ordering": ["created_at"],
            },
        ),
        migrations.CreateModel(
            name="Metadata",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date de création"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="date de modification"
                    ),
                ),
                (
                    "prop",
                    models.CharField(
                        max_length=100, unique=True, verbose_name="propriété"
                    ),
                ),
                ("value", models.CharField(max_length=255, verbose_name="valeur")),
            ],
            options={
                "abstract": False,
                "verbose_name": "métadonnée",
            },
        ),
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="date de création"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="date de modification"
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="nom")),
                (
                    "acronym",
                    models.CharField(blank=True, max_length=100, verbose_name="sigle"),
                ),
                ("logo", models.ImageField(blank=True, upload_to="logos")),
                (
                    "part_of",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="core.organization",
                    ),
                ),
            ],
            options={
                "verbose_name": "organisation",
                "ordering": ["name"],
            },
        ),
        migrations.DeleteModel(
            name="Editor",
        ),
        migrations.AlterField(
            model_name="source",
            name="editor",
            field=models.ManyToManyField(
                to="core.Organization", verbose_name="éditeur"
            ),
        ),
    ]
