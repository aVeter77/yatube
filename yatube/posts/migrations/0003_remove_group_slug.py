# Generated by Django 2.2.19 on 2021-12-02 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20211202_0636'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='slug',
        ),
    ]
