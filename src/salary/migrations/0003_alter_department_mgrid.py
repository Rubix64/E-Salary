# Generated by Django 4.0 on 2021-12-17 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('salary', '0002_alter_salary_eid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='mgrid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
