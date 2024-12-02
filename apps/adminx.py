import xadmin
from xadmin import views

# 注册全局设置
class GlobalSetting(object):
    site_title = "后台管理系统"
    site_footer = "后台管理系统"
    menu_style = "accordion"

xadmin.site.register(views.CommAdminView, GlobalSetting)
