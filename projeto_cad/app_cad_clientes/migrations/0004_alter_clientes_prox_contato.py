# Generated by Django 5.1.1 on 2024-10-01 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "app_cad_clientes",
            "0003_remove_clientes_observacoes_clientes_bairro_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="clientes",
            name="prox_contato",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
