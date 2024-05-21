# Generated by Django 5.0.6 on 2024-05-21 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Bookstore', '0002_product_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('description', models.TextField(null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('image', models.ImageField(upload_to='products/')),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
