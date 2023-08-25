# Generated by Django 4.2.3 on 2023-08-07 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_alter_colour_id_alter_drain_id_alter_profile_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile',
            new_name='material',
        ),
        migrations.AlterField(
            model_name='window',
            name='height',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='window',
            name='open_window',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='window',
            name='weight',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='window',
            name='window',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
