# Generated by Django 5.0.7 on 2024-07-30 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0014_topmanagement'),
    ]

    operations = [
        migrations.AddField(
            model_name='topmanagement',
            name='picture',
            field=models.ImageField(null=True, upload_to='topManagement/'),
        ),
    ]
