# Generated by Django 4.0.3 on 2022-06-23 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0030_auto_20210511_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='video',
            field=models.CharField(max_length=250),
        ),
    ]
