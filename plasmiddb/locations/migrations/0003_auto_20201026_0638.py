# Generated by Django 3.0.7 on 2020-10-26 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locations', '0002_auto_20201025_2221'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='containercontent',
            unique_together={('container', 'row', 'column')},
        ),
    ]
