# Generated by Django 5.1.2 on 2024-10-29 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0002_ledgeraccount_cr_ledgeraccount_dr'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ledgeraccount',
            name='cr',
        ),
        migrations.RemoveField(
            model_name='ledgeraccount',
            name='dr',
        ),
    ]
