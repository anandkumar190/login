# Generated by Django 3.1.1 on 2020-09-16 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Signup',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('designation', models.CharField(default='', max_length=50)),
                ('gender', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=500)),
            ],
        ),
    ]