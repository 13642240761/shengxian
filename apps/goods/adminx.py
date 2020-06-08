from django.core.cache import cache

import xadmin

from apps.goods.models import GoodsType, GoodsSKU, GoodsImage, IndexGoodsBanner, IndexTypeGoodsBanner, \
    IndexPromotionBanner, Goods


class BaseModelAdmin(object):
    # def save_model(self, request, obj, form, change):
    #     '''新增或更新表中的数据时调用'''
    #     super().save_model(request, obj, form, change)
    #
    #     # 发出任务，让celery worker重新生成首页静态页
    #     from celery_tasks.tasks import generate_static_index_html
    #     generate_static_index_html.delay()
    #
    #     # 清除首页的缓存数据
    #     cache.delete('index_page_data')
    #
    # def delete_model(self, request, obj):
    #     '''删除表中的数据时调用'''
    #     super().delete_model(request, obj)
    #     # 发出任务，让celery worker重新生成首页静态页
    #     from celery_tasks.tasks import generate_static_index_html
    #     generate_static_index_html.delay()
    #
    #     # 清除首页的缓存数据
    #     cache.delete('index_page_data')

    def save_models(self):
        from celery_tasks.tasks import generate_static_index_html
        # 发出任务，让celery worker重新生成首页静态页
        generate_static_index_html.delay()

        # 清除首页的缓存数据
        cache.delete('index_page_data')
        obj = self.new_obj
        obj.save()

    def delete_models(self):
        from celery_tasks.tasks import generate_static_index_html
        # 发出任务，让celery worker重新生成首页静态页
        generate_static_index_html.delay()

        # 清除首页的缓存数据
        cache.delete('index_page_data')
        obj = self.new_obj
        obj.save()


# 商品种类
class GoodsTypeAdmin(BaseModelAdmin):
    list_display = ['name', 'logo', 'image']  # 页面显示的列
    search_fields = ['name','logo']  # 搜索
    list_editable = ['name', 'logo', 'image']  # 可编辑
    list_filter = ['name','logo']  # 用于过滤


# 商品SKU
class GoodsSKUAdmin(BaseModelAdmin):
    # 页面显示的列[种类，    商品SPU， 名称，   价格，   单位，   库存，   销量，   状态，   图片]
    list_display = ['type', 'goods', 'name', 'price', 'unite', 'stock', 'sales', 'status', 'image']
    search_fields = ['type', 'goods', 'name', 'stock', 'status']  # 搜索
    list_editable = ['type', 'goods', 'name', 'price', 'unite', 'stock', 'sales', 'status', 'image', 'desc']  # 可编辑
    list_filter = ['type', 'goods', 'name', 'stock', 'status']  # 用于过滤


# 商品SPU
class GoodsAdmin(BaseModelAdmin):
    # 页面显示的列
    list_display = ['name', 'detail']
    search_fields = ['name']  # 搜索
    list_editable = ['name', 'detail']  # 可编辑
    list_filter = ['name']  # 用于过滤


# 商品图片
class GoodsImageAdmin(BaseModelAdmin):
    # 页面显示的列
    list_display = ['sku', 'image']
    search_fields = ['sku']  # 搜索
    list_editable = ['sku', 'image']  # 可编辑
    list_filter = ['sku']  # 用于过滤


# 首页轮播
class IndexGoodsBannerAdmin(BaseModelAdmin):
    # 页面显示的列
    list_display = ['sku', 'image', 'index']
    search_fields = ['sku', 'index']  # 搜索
    list_editable = ['sku', 'image', 'index']  # 可编辑
    list_filter = ['sku', 'index']  # 用于过滤


# 主页分类展示商品
class IndexTypeGoodsBannerAdmin(BaseModelAdmin):
    # 页面显示的列
    list_display = ['type', 'sku', 'display_type', 'index']
    search_fields = ['type', 'sku', 'display_type', 'index']  # 搜索
    list_editable = ['type', 'sku', 'display_type', 'index']  # 可编辑
    list_filter = ['type', 'sku', 'display_type', 'index']  # 用于过滤


# 主页促销活动
class IndexPromotionBannerAdmin(BaseModelAdmin):
    # 页面显示的列
    list_display = ['name', 'index', 'url', 'image']
    search_fields = ['name', 'index', 'url']  # 搜索
    list_editable = ['name', 'index', 'url', 'image']  # 可编辑
    list_filter = ['name', 'index', 'url']  # 用于过滤


xadmin.site.register(GoodsType, GoodsTypeAdmin)
xadmin.site.register(GoodsSKU, GoodsSKUAdmin)
xadmin.site.register(Goods, GoodsAdmin)
xadmin.site.register(GoodsImage, GoodsImageAdmin)
xadmin.site.register(IndexGoodsBanner, IndexGoodsBannerAdmin)
xadmin.site.register(IndexTypeGoodsBanner, IndexTypeGoodsBannerAdmin)
xadmin.site.register(IndexPromotionBanner, IndexPromotionBannerAdmin)
