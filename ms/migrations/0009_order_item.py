# Generated by Django 5.0.6 on 2024-07-23 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ms', '0008_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='item',
            field=models.ManyToManyField(to='ms.item'),
        ),
    ]