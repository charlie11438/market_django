# Generated by Django 3.1.2 on 2020-12-19 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=16, verbose_name='用戶名稱')),
                ('password', models.CharField(max_length=255, verbose_name='用戶密碼')),
                ('email', models.CharField(max_length=255, verbose_name='用戶EMAIL')),
                ('phone', models.CharField(max_length=16, verbose_name='用戶電話')),
                ('address', models.CharField(max_length=255, verbose_name='用戶地址')),
                ('avatar', models.ImageField(upload_to='userProfile/')),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
