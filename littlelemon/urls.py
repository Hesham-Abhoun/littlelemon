from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from restaurant.views import BookingViewSet,MenuViewSet
from restaurant import views

router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)
router.register(r'meals',views.MenuViewSet)
urlpatterns = [

#    
#    

    path('admin/', admin.site.urls),
    path('api/',include('restaurant.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('restaurant/menu/', include(router.urls)),
    path('restaurant/booking/', include(router.urls)),


   
]

