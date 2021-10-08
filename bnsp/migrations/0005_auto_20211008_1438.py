# Generated by Django 3.2.8 on 2021-10-08 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_alter_document_tags'),
        ('bnsp', '0004_rename_live_query_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='query',
            name='query',
            field=models.CharField(help_text="Entrer '*' pour rechercher toutes les entrées", max_length=1000, verbose_name='requête'),
        ),
        migrations.AlterUniqueTogether(
            name='query',
            unique_together={('query', 'source')},
        ),
    ]
