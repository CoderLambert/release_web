# Generated by Django 2.0.3 on 2018-04-30 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_markdownartical'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailverifyrecord',
            name='send_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]