# Generated by Django 3.1 on 2020-10-04 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20200927_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parametri',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Chiave', models.CharField(max_length=30)),
                ('Valore', models.CharField(max_length=300)),
            ],
            options={
                'verbose_name': 'Parametri',
                'verbose_name_plural': 'Parametri',
            },
        ),
    ]
