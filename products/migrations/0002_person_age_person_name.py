# Generated by Django 4.2.2 on 2023-06-25 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='person',
            name='name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
