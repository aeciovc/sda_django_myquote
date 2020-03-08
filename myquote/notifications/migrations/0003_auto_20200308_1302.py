# Generated by Django 3.0.3 on 2020-03-08 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0002_auto_20200308_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='content',
            field=models.CharField(default='Buyer', max_length=40),
        ),
        migrations.AlterField(
            model_name='notification',
            name='type',
            field=models.CharField(choices=[('B', 'Buyer'), ('S', 'Seller')], default='Seller', max_length=2),
        ),
    ]