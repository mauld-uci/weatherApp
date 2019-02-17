# Generated by Django 2.1.7 on 2019-02-17 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0002_auto_20190216_1434'),
    ]

    operations = [
        migrations.RenameField(
            model_name='weatherdata',
            old_name='apparentTemp',
            new_name='apparent_temp',
        ),
        migrations.RenameField(
            model_name='weatherdata',
            old_name='precipitation',
            new_name='precip_prob',
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='time',
            field=models.DateTimeField(),
        ),
    ]