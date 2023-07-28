from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from portfolio import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main_page),
    path('blog/', include('blog.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
