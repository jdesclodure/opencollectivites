# Generated by Django 3.1.6 on 2021-02-12 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0035_auto_20210208_0853'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='topic',
            options={'ordering': ['name'], 'verbose_name': 'thématique'},
        ),
        migrations.AddField(
            model_name='document',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]