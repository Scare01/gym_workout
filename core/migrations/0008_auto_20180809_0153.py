# Generated by Django 2.0.5 on 2018-08-09 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20180809_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='continuity',
            field=models.PositiveIntegerField(choices=[(4, '4 month'), (6, '6 month'), (8, '8 month')]),
        ),
    ]
