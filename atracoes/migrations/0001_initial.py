# Generated by Django 2.2.4 on 2019-08-06 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atracao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('horario_funcionamento', models.TextField()),
                ('idade_minina', models.IntegerField()),
            ],
        ),
    ]
