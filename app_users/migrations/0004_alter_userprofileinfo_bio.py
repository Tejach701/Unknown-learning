# Generated by Django 4.0.3 on 2022-06-18 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_users', '0003_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='bio',
            field=models.CharField(max_length=50),
        ),
    ]