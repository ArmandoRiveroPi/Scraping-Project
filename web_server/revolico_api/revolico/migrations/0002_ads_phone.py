# Generated by Django 2.2.4 on 2019-08-08 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('revolico', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='phone',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
