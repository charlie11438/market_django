# Generated by Django 3.1.2 on 2020-12-19 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('productName', models.CharField(max_length=64, verbose_name='商品名稱')),
                ('price', models.IntegerField(verbose_name='商品價格')),
                ('amount', models.IntegerField(verbose_name='商品數量')),
                ('sort', models.CharField(max_length=32, verbose_name='類別')),
                ('avatar', models.ImageField(upload_to='productImage/')),
            ],
            options={
                'db_table': 'product',
            },
        ),
    ]
