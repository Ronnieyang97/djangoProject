# Generated by Django 3.0.3 on 2020-08-26 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sig_cn', '0003_employee_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='picture',
            field=models.URLField(null=True),
        ),
    ]
