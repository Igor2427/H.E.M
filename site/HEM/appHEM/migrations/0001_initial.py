# Generated by Django 2.2.12 on 2024-10-25 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=256)),
                ('nome', models.TextField(max_length=50)),
                ('senha', models.CharField(max_length=30)),
                ('crm', models.CharField(max_length=8)),
                ('especialidade', models.TextField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=256)),
                ('nome', models.TextField(max_length=50)),
                ('senha', models.CharField(max_length=30)),
            ],
        ),
    ]
