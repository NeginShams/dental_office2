# Generated by Django 3.0.4 on 2020-06-16 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seapp', '0005_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='visit',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='visit',
            name='phone_number',
            field=models.CharField(default='', max_length=11),
        ),
    ]