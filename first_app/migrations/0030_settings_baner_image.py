# Generated by Django 5.0.7 on 2024-08-01 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0029_email_inbox'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='baner_image',
            field=models.ImageField(null=True, upload_to='settings/banerImage/'),
        ),
    ]
