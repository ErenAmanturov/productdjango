# Generated by Django 4.2.3 on 2023-08-16 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_phone_phone_user_phone_alter_user_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.phone'),
        ),
    ]
