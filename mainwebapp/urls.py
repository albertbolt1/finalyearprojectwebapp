from django.urls import path,include
from . import views 
from django.conf import settings 
from django.conf.urls.static import static 

app_name = 'mainwebapp'
urlpatterns = [
    path('',views.home,name='home'),
    path('image_upload', views.plantdisease_image_view, name = 'image_upload'), 
    path('disease_images', views.display_disease_images, name = 'disease_images'), 
]


if settings.DEBUG: 
        urlpatterns += static(settings.MEDIA_URL, 
                              document_root=settings.MEDIA_ROOT) 