# Generated by Django 3.2.9 on 2021-11-09 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_auto_20211109_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='is_published',
            field=models.BooleanField(blank=True, default=True, null=True, verbose_name='est publié'),
        ),
    ]