# Generated by Django 3.1.7 on 2021-03-31 18:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('practice', '0007_auto_20210330_2059'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='exercise',
            options={'ordering': ('id',), 'verbose_name': 'задание', 'verbose_name_plural': 'задания'},
        ),
    ]
