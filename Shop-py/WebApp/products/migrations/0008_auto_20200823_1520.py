# Generated by Django 3.1 on 2020-08-23 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_auto_20200823_1513'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='Description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='Image',
            new_name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='Quantity',
        ),
    ]
