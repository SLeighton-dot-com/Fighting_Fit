# Generated by Django 3.2.24 on 2024-03-09 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_review'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='text',
            new_name='review_text',
        ),
    ]
