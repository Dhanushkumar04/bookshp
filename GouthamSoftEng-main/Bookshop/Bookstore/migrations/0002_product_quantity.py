# Generated by Django 5.0.6 on 2024-05-21 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.TextField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
