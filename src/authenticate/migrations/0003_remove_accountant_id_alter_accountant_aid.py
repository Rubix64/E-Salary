# Generated by Django 4.0 on 2021-12-17 18:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0002_remove_employee_id_employee_userid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accountant',
            name='id',
        ),
        migrations.AlterField(
            model_name='accountant',
            name='aid',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='authenticate.employee'),
        ),
    ]