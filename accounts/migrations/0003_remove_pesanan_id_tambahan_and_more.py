# Generated by Django 5.2.1 on 2025-06-03 02:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_email_pengguna_email_alter_lapangan_gambar_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pesanan',
            name='id_tambahan',
        ),
        migrations.RemoveField(
            model_name='pesanantambahan',
            name='id_tambahan',
        ),
        migrations.AddField(
            model_name='pesanan',
            name='tambahan_items',
            field=models.ManyToManyField(through='accounts.PesananTambahan', to='accounts.tambahan'),
        ),
        migrations.AddField(
            model_name='pesanantambahan',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.tambahan'),
        ),
        migrations.AddField(
            model_name='pesanantambahan',
            name='pesanan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='accounts.pesanan'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pesanantambahan',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
