# Generated by Django 3.2.24 on 2024-02-23 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='item_category',
            new_name='product_category',
        ),
    ]
