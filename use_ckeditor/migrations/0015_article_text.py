# Generated by Django 2.0.3 on 2018-04-12 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('use_ckeditor', '0014_auto_20180410_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='text',
            field=models.TextField(blank=True, null=True, verbose_name='纯文本'),
        ),
    ]