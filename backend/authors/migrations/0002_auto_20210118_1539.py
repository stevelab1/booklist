# Generated by Django 3.1.5 on 2021-01-18 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/'),
        ),
    ]
