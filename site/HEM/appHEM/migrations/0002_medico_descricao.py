# Generated by Django 5.1.1 on 2024-11-19 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appHEM', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='medico',
            name='descricao',
            field=models.TextField(blank=True, default='Descrição', max_length=250),
        ),
    ]