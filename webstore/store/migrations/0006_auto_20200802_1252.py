# Generated by Django 3.0.8 on 2020-08-02 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img1',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='img2',
            field=models.TextField(blank=True, null=True),
        ),
    ]
