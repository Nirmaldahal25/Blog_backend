# Generated by Django 5.0.4 on 2024-04-26 08:19

import content.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ('-date',)},
        ),
        migrations.AddField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to=content.models.save_image),
        ),
        migrations.DeleteModel(
            name='PostImages',
        ),
    ]