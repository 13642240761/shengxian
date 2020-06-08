import xadmin


# xadmin.site.register(UserProfile)
from xadmin import views


class BaseSettings(object):
    enable_themes = True  # 主题
    use_bootswatch = True  # 主题菜单


class GlobalSettings(object):
    site_title = '生鲜商城后台管理'
    site_footer = '生鲜商城'


xadmin.site.register(views.BaseAdminView, BaseSettings)
xadmin.site.register(views.CommAdminView, GlobalSettings)
