# Generated by Django 5.1.2 on 2024-10-29 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ledger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ledgeraccount',
            name='cr',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
        migrations.AddField(
            model_name='ledgeraccount',
            name='dr',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=10),
        ),
    ]
