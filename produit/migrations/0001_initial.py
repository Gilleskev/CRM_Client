# Generated by Django 3.1.5 on 2021-01-23 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, null=True)),
                ('prix', models.FloatField(null=True)),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
