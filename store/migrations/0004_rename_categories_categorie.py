# Generated by Django 4.2.4 on 2023-08-26 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_category_categories'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Categories',
            new_name='Categorie',
        ),
    ]
