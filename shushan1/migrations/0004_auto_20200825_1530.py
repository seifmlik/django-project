# Generated by Django 3.0.8 on 2020-08-25 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shushan1', '0003_auto_20200825_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='acapacita',
            field=models.IntegerField(default=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='tipoaggiunto',
            field=models.CharField(default='40', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='info',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]