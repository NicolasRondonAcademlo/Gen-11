# Generated by Django 3.2 on 2022-08-10 02:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_bookitem_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookitem',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='bookitem',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('2ee38f47-2feb-4501-8cd8-1a991249c53b')),
        ),
    ]
