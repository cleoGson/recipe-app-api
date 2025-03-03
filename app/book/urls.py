from django.urls import path , include
from rest_framework.routers  import DefaultRouter



router = DefaultRouter()
router.register('versions', views.VersionViewSet)

app_name= 'book'
urlpatterns = [ 
    path('', include(router.urls)),   
]