# Generated by Django 2.2.12 on 2020-05-20 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_details',
            name='student_fee_deatils',
            field=models.CharField(max_length=50),
        ),
    ]