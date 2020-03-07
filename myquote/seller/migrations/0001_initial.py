# Generated by Django 3.0.3 on 2020-03-07 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id_code', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.BigIntegerField(unique=True)),
                ('dt_entrance', models.TextField(blank=True, null=True)),
            ],
        ),
    ]