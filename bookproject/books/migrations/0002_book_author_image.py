# Generated by Django 5.2.3 on 2025-06-18 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_image',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
