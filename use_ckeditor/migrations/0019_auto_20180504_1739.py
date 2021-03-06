# Generated by Django 2.0.3 on 2018-05-04 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('use_ckeditor', '0018_auto_20180502_1854'),
    ]

    operations = [
        migrations.CreateModel(
            name='Web_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True, verbose_name='网站分类')),
            ],
            options={
                'verbose_name': '网站分类',
                'verbose_name_plural': '网站分类',
            },
        ),
        migrations.AddField(
            model_name='web_link',
            name='tag',
            field=models.ManyToManyField(blank=True, to='use_ckeditor.Web_type', verbose_name='网站分类'),
        ),
    ]
