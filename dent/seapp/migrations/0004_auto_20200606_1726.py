# Generated by Django 3.0.4 on 2020-06-06 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seapp', '0003_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='firstName',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='gender',
            field=models.BinaryField(editable=True, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='lastName',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='nationalCode',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
