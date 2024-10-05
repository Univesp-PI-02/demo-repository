# Generated by Django 5.1.1 on 2024-10-01 22:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_cad_clientes", "0002_clientes_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="clientes",
            name="observacoes",
        ),
        migrations.AddField(
            model_name="clientes",
            name="bairro",
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="clientes",
            name="cep",
            field=models.IntegerField(default=1, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="clientes",
            name="complemento",
            field=models.CharField(default=1, max_length=120),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="clientes",
            name="numero_end",
            field=models.IntegerField(default=1, max_length=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="clientes",
            name="rua",
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="clientes",
            name="telefone_2",
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="clientes",
            name="primeiro_contato",
            field=models.DateTimeField(),
        ),
        migrations.CreateModel(
            name="Observacoes",
            fields=[
                ("id_observacao", models.AutoField(primary_key=True, serialize=False)),
                ("descricao", models.TextField()),
                ("data_observacao", models.DateTimeField(auto_now_add=True)),
                (
                    "id_cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="observacoes",
                        to="app_cad_clientes.clientes",
                    ),
                ),
            ],
        ),
    ]
