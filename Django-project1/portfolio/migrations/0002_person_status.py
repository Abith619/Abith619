# Generated by Django 4.0.4 on 2022-06-02 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
