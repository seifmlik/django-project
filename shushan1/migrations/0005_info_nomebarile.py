# Generated by Django 3.0.8 on 2020-08-25 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shushan1', '0004_auto_20200825_1530'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='nomebarile',
            field=models.CharField(default='br1', max_length=20),
            preserve_default=False,
        ),
    ]
