# Generated by Django 4.0.3 on 2023-01-29 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announecements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='annonce',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
