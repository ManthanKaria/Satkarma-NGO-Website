# Generated by Django 5.0.2 on 2024-03-17 11:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_satkarma', '0004_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Product_Image',
            field=models.ImageField(default='', upload_to='result/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'pdf'])]),
        ),
    ]
