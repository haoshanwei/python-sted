# Generated by Django 2.1 on 2019-12-22 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20191222_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, verbose_name='文章标题')),
                ('desc', models.CharField(blank=True, default='这个文章没有描述', max_length=100, null=True, verbose_name='描述')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('img', models.ImageField(default='images/1.jpg', upload_to='article_img', verbose_name='文章图片')),
                ('recommend', models.BooleanField(default=False, verbose_name='是否推荐')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('is_delete', models.BooleanField(default=False, verbose_name='是否删除')),
                ('category', models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.DO_NOTHING, to='user.Category', verbose_name='分类')),
            ],
            options={
                'verbose_name': '文章',
                'verbose_name_plural': '文章',
                'db_table': 'article',
                'ordering': ['create_time'],
            },
        ),
    ]
