# Generated by Django 3.0.8 on 2020-09-20 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopproduct',
            name='price',
            field=models.IntegerField(default=1),
        ),
    ]
