# Generated by Django 3.1.2 on 2020-12-31 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userorder', '0002_auto_20201230_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderno',
            field=models.CharField(max_length=255, verbose_name='訂單編號'),
        ),
    ]