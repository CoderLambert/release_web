# Generated by Django 2.0.3 on 2018-04-17 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20180417_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='images/%Y/%m', verbose_name='用户头像'),
        ),
    ]
