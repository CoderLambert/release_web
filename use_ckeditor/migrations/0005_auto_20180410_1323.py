# Generated by Django 2.0.3 on 2018-04-10 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('use_ckeditor', '0004_auto_20180410_1321'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '标签', 'verbose_name_plural': '标签'},
        ),
    ]
