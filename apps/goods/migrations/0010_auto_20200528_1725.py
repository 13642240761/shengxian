# Generated by Django 2.1 on 2020-05-28 09:25
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import migrations



class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0009_goods_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='detail',
            field=RichTextUploadingField(blank=True, verbose_name='商品详情'),
        ),
    ]