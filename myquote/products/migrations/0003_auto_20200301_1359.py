# Generated by Django 3.0.3 on 2020-03-01 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20200229_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default_image.jpg', upload_to='images/'),
        ),
    ]
