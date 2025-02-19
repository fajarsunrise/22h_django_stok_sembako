# Generated by Django 4.1.13 on 2025-02-11 14:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tabel_stok', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produksembako',
            name='deskripsi',
        ),
        migrations.AddField(
            model_name='produksembako',
            name='kategori',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
