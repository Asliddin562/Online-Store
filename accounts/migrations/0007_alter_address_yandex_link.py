# Generated by Django 5.2.4 on 2025-07-28 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_alter_address_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='yandex_link',
            field=models.URLField(default='null'),
            preserve_default=False,
        ),
    ]
