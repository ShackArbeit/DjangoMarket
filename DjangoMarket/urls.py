from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path("",include('core.urls')),
    path('items/',include('item.urls')),
    path('dashboard/',include('dashboard.urls')),
    path('inbox/',include('conversation.urls')),
    path("admin/", admin.site.urls),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
# 加上static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 讓在開發環境時，可以透過指定的 url 訪問在 media/item_images 下的圖片
# 例如 : http://localhost:8000/media/item_images/hq720.jpg