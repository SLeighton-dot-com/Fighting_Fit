# Generated by Django 3.2.24 on 2024-03-09 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_rename_text_review_review_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_text',
            field=models.TextField(max_length=200),
        ),
    ]
