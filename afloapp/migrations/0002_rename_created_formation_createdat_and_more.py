# Generated by Django 4.1.5 on 2023-01-19 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('afloapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formation',
            old_name='created',
            new_name='createdAt',
        ),
        migrations.RenameField(
            model_name='formation',
            old_name='updated',
            new_name='updatedAt',
        ),
    ]