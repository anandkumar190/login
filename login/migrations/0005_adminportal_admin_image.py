# Generated by Django 3.1.1 on 2020-09-19 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_auto_20200919_1147'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminportal',
            name='admin_image',
            field=models.ImageField(default='', upload_to='admin/images'),
        ),
    ]
