# Generated by Django 3.2.9 on 2021-11-30 10:33

from django.db import migrations, models
import django.db.models.deletion
import francedata.services.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CollectivityMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='date de modification')),
                ('collectivity_type', models.CharField(choices=[('COMM', 'Communes'), ('DEPT', 'Départements'), ('EPCI', 'EPCIs'), ('REG', 'Régions')], max_length=4, verbose_name='type de collectivité')),
                ('siren', models.CharField(max_length=9, validators=[francedata.services.validators.validate_siren], verbose_name='numéro Siren')),
                ('message', models.TextField(verbose_name='message')),
            ],
            options={
                'verbose_name': 'message lié à une collectivité',
                'verbose_name_plural': 'messages liés à une collectivité',
            },
        ),
        migrations.CreateModel(
            name='DataTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='date de modification')),
                ('name', models.CharField(max_length=100, verbose_name='nom')),
                ('slug', models.SlugField(max_length=120, verbose_name='slug')),
                ('page_type', models.CharField(choices=[('COMM', 'Communes'), ('DEPT', 'Départements'), ('EPCI', 'EPCIs'), ('REG', 'Régions')], max_length=4, verbose_name='type de fiche')),
                ('rank', models.PositiveSmallIntegerField(default=0, verbose_name='rang')),
            ],
            options={
                'verbose_name': 'tableau',
                'verbose_name_plural': 'tableaux',
                'ordering': ['rank'],
            },
        ),
        migrations.CreateModel(
            name='DataRow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='date de modification')),
                ('rank', models.PositiveSmallIntegerField(default=0, verbose_name='rang')),
                ('key', models.CharField(max_length=50, verbose_name='clef')),
                ('label', models.CharField(max_length=250, verbose_name='libellé')),
                ('tooltip', models.CharField(blank=True, max_length=250, null=True, verbose_name='infobulle')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collectivity_pages.datatable')),
            ],
            options={
                'verbose_name': 'ligne de tableau',
                'verbose_name_plural': 'lignes de tableau',
                'ordering': ['table', 'rank'],
            },
        ),
    ]
