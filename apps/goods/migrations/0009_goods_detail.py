# Generated by Django 2.1 on 2020-05-28 07:18
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0008_remove_goods_detail'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='detail',
            field=RichTextUploadingField(default='', verbose_name='商品详情'),
        ),
    ]
