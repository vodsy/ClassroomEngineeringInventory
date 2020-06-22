# Generated by Django 3.0.4 on 2020-04-16 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0002_auto_20200415_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalreportingdata',
            name='model_brand',
            field=models.CharField(choices=[('ML', 'MLC Plus 200'), ('IN', 'IN1606'), ('ML', 'MLC 226'), ('MP', 'MPS409')], max_length=2),
        ),
        migrations.AlterField(
            model_name='reportingdata',
            name='model_brand',
            field=models.CharField(choices=[('ML', 'MLC Plus 200'), ('IN', 'IN1606'), ('ML', 'MLC 226'), ('MP', 'MPS409')], max_length=2),
        ),
    ]