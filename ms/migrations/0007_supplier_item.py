# Generated by Django 5.0.6 on 2024-07-23 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ms', '0006_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='item',
            field=models.ManyToManyField(to='ms.item'),
        ),
    ]
