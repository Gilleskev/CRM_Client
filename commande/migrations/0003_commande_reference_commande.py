# Generated by Django 3.1.5 on 2021-01-23 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0002_auto_20210123_1950'),
    ]

    operations = [
        migrations.AddField(
            model_name='commande',
            name='reference_commande',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
