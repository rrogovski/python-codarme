# Generated by Django 4.0.6 on 2022-07-10 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_horario', models.DateTimeField()),
                ('nome_cliente', models.CharField(max_length=200)),
                ('email_cliente', models.EmailField(max_length=254)),
                ('telefone_cliente', models.CharField(max_length=20)),
            ],
        ),
    ]
