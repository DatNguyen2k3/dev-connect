# Generated by Django 4.1.7 on 2023-04-04 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_skill'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Skill',
            new_name='WorkExperience',
        ),
    ]
