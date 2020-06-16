# Generated by Django 3.0.4 on 2020-06-06 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('seapp', '0002_auto_20200604_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(max_length=30)),
                ('birthDay', models.DateField(null=True)),
                ('gender', models.BinaryField(editable=True)),
                ('phone_number', models.CharField(max_length=11)),
                ('drugs_notes', models.TextField()),
                ('diseases_notes', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]