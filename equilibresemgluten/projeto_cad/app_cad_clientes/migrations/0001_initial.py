# Generated by Django 5.1.1 on 2024-09-21 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Clientes",
            fields=[
                ("id_cliente", models.AutoField(primary_key=True, serialize=False)),
                ("empresa", models.CharField(max_length=150)),
                ("segmento", models.CharField(max_length=100)),
                ("contato", models.CharField(max_length=100)),
                ("telefone", models.CharField(max_length=20)),
                ("cidade", models.CharField(max_length=100)),
                ("estado", models.CharField(max_length=2)),
                ("email", models.EmailField(max_length=254)),
                ("instagram", models.CharField(max_length=100)),
                ("cnpj", models.CharField(max_length=18)),
                ("qtd_lojas", models.IntegerField()),
                ("observacoes", models.TextField()),
                ("prox_contato", models.DateField()),
                ("primeiro_contato", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]