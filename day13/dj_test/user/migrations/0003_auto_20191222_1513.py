# Generated by Django 2.1 on 2019-12-22 15:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20191222_1436'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-create_time'], 'verbose_name': '文章分类', 'verbose_name_plural': '文章分类'},
        ),
    ]
