# Generated by Django 2.2 on 2020-12-03 16:51

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='data',
            field=jsonfield.fields.JSONField(max_length=200, null=True),
        ),
    ]