# Generated by Django 4.1.7 on 2023-04-07 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_workexperience_company'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'ordering': ['-created']},
        ),
        migrations.AddIndex(
            model_name='profile',
            index=models.Index(fields=['id'], name='users_profi_id_6c07ac_idx'),
        ),
    ]