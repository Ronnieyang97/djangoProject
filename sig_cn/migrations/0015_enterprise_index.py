# Generated by Django 3.0.3 on 2020-09-29 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sig_cn', '0014_auto_20200929_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='enterprise',
            name='index',
            field=models.BooleanField(null=True),
        ),
    ]