# Generated by Django 2.2.12 on 2020-05-03 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feepattern', '0003_feepatternhead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feepatternhead',
            name='total_tution_fee',
            field=models.CharField(max_length=50),
        ),
    ]