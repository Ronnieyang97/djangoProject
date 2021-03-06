# Generated by Django 3.0.3 on 2020-09-29 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sig_cn', '0013_auto_20200928_1507'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='introduction',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='enterprise',
            name='picture_owner',
            field=models.ImageField(blank=True, null=True, upload_to='owner'),
        ),
        migrations.AlterField(
            model_name='enterprise',
            name='site',
            field=models.URLField(blank=True, null=True),
        ),
    ]
