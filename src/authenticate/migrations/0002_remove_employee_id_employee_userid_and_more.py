# Generated by Django 4.0 on 2021-12-17 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='id',
        ),
        migrations.AddField(
            model_name='employee',
            name='userid',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accountant',
            name='aid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authenticate.employee'),
        ),
    ]