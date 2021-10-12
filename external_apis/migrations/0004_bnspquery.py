# Generated by Django 3.2.8 on 2021-10-11 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0046_auto_20211011_1433'),
        ('external_apis', '0003_auto_20211008_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='BnspQuery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='date de modification')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='nom')),
                ('query', models.CharField(help_text="Entrer '*' pour rechercher toutes les entrées", max_length=1000, verbose_name='requête')),
                ('last_polled', models.DateTimeField(blank=True, null=True, verbose_name='dernière tentative')),
                ('last_success', models.DateTimeField(blank=True, null=True, verbose_name='dernière réussite')),
                ('last_change', models.DateTimeField(blank=True, null=True, verbose_name='dernier changement')),
                ('is_active', models.BooleanField(default=True, verbose_name='requête active')),
                ('identify_regions', models.BooleanField(default=False, verbose_name='Identifier les noms de régions')),
                ('identify_departements', models.BooleanField(default=False, verbose_name='Identifier les noms de départements')),
                ('identify_metropoles', models.BooleanField(default=False, verbose_name='Identifier les noms de métropoles')),
                ('identify_main_cities', models.BooleanField(default=False, help_text='Ne marche que si la source possède des départements ou régions.', verbose_name='Identifier les noms des principales villes')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.source', verbose_name='source associée')),
            ],
            options={
                'verbose_name': 'requête',
                'unique_together': {('query', 'source')},
            },
        ),
    ]
