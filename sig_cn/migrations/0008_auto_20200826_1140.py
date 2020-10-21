# Generated by Django 3.0.3 on 2020-08-26 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sig_cn', '0007_auto_20200826_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='department',
            field=models.CharField(blank=True, choices=[('Investment partner', 'Investment partner'), ('Investment manager', 'Investment manager'), ('Global concept', 'Global concept'), ('Investment adviser', 'Investment adviser'), ('Post-investment', 'Post-investment'), ('Legal', 'Legal'), ('Operation', 'Operation')], max_length=30, null=True),
        ),
    ]
