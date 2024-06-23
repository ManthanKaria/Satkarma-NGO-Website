# Generated by Django 5.0.2 on 2024-03-31 04:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_satkarma', '0006_alter_product_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_satkarma.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_satkarma.student')),
            ],
        ),
    ]
