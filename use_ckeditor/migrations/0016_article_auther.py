# Generated by Django 2.0.3 on 2018-04-12 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('use_ckeditor', '0015_article_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='auther',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='作者'),
        ),
    ]
