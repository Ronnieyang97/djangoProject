# Generated by Django 3.0.3 on 2020-08-20 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=16)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
