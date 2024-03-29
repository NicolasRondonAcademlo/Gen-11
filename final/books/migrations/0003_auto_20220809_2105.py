# Generated by Django 3.2 on 2022-08-10 02:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20220809_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookitem',
            name='is_available',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bookitem',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('1d9e29f3-e6f6-4f04-a10c-eff58fdfc1bc')),
        ),
    ]
