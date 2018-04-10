# Generated by Django 2.0.3 on 2018-04-10 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('use_ckeditor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Web_link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='name')),
                ('address', models.URLField(max_length=256, verbose_name='address')),
            ],
        ),
    ]