# Generated by Django 4.1.7 on 2023-04-05 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_img1',
            field=models.ImageField(blank=True, default='jobs/default.jpg', null=True, upload_to='jobs/'),
        ),
        migrations.AddField(
            model_name='job',
            name='job_img2',
            field=models.ImageField(blank=True, default='jobs/default.jpg', null=True, upload_to='jobs/'),
        ),
        migrations.AddField(
            model_name='job',
            name='job_img3',
            field=models.ImageField(blank=True, default='jobs/default.jpg', null=True, upload_to='jobs/'),
        ),
    ]
