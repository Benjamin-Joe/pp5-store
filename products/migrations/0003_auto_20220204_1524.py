# Generated by Django 3.2 on 2022-02-04 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20220203_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='Description Here'),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='placeholder', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=8, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='001', max_length=200, unique=True),
        ),
    ]
