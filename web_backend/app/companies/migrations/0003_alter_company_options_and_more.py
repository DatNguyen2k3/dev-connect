# Generated by Django 4.1.7 on 2023-04-07 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_company_full_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'ordering': ['-id']},
        ),
        migrations.AddIndex(
            model_name='company',
            index=models.Index(fields=['id'], name='companies_c_id_e5b8cb_idx'),
        ),
    ]
