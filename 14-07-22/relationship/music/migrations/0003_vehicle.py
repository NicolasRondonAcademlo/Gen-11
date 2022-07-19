# Generated by Django 3.2 on 2022-07-15 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_article_reporter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(max_length=150)),
                ('color', models.CharField(max_length=150)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]