# Generated by Django 4.0 on 2021-12-27 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('salary', '0003_remove_deduction_eid'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Department',
        ),
    ]
