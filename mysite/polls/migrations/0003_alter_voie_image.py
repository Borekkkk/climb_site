# Generated by Django 4.0.1 on 2022-02-19 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_voie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voie',
            name='image',
            field=models.ImageField(upload_to='media'),
        ),
    ]
