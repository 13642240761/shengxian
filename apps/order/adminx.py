import xadmin

# xadmin.site.register(UserProfile)
from apps.order.models import OrderInfo, OrderGoods
from xadmin import views


# 订单模型类
class OrderInfoAdmin(object):
    # 页面显示的列[订单id,        用户,    地址,    支付方式,     商品数量,       商品总价,      订单运费,         订单状态 ,     支付编号]
    list_display = ['order_id', 'user', 'addr', 'pay_method', 'total_count', 'total_price', 'transit_price',
                    'order_status', 'trade_no']
    search_fields = ['order_id', 'user', 'pay_method', 'order_status', 'trade_no']  # 搜索
    list_editable = ['order_id', 'user', 'addr', 'pay_method', 'total_count', 'total_price', 'transit_price',
                     'order_status', 'trade_no']  # 可编辑
    list_filter = ['order_id', 'user', 'pay_method', 'order_status', 'trade_no']  # 用于过滤


class OrderGoodsAdmin(object):
    # 页面显示的列[  订单,  商品SKU, 商品数目,商品价格 ,评论]
    list_display = ['order', 'sku', 'count', 'price', 'comment']
    search_fields = ['order', 'sku', 'comment']  # 搜索
    list_editable = ['order', 'sku', 'count', 'price', 'comment']  # 可编辑
    list_filter = [['order', 'sku', 'comment']]  # 用于过滤


xadmin.site.register(OrderInfo, OrderInfoAdmin)
xadmin.site.register(OrderGoods, OrderGoodsAdmin)
