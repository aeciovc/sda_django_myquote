# Generated by Django 3.0.3 on 2020-02-27 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('brand', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('P', 'Published'), ('NP', 'Not published')], default='NP', max_length=2)),
                ('image', models.ImageField(default='default_image.jpg', storage='product_image', upload_to='')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='products.Category')),
            ],
        ),
    ]
