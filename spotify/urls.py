"""
URL configuration for spotify project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    
    path('',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('forgot/',views.forgotpassword,name="forgotpassword"),
    path('passwordupdate/<id>',views.passwordupdate,name="passupdated"),
    

    path('category/',views.Category,name="category"),
    path('subcatedata/',views.Subcategorydata,name="subcatedata"),
    path('subcateview/',views.subcateview,name="subcateview"),
    path('subcateupdate/<id>',views.subcateupdate,name="subcateupdate"),
    
    
    path('songdata/',views.songdata,name="songdata"),
    path('songdetail/<int:id>/', views.songdetail, name='songdetail'),
    # path('songdetail/<str:trans_Id>/<int:id>',views.songdetail,name="songdetail"),
    path('songupdate/<str:songname>/<id>',views.songdataupdate,name="songupdate"),
    

    path('songpageview/<id>',views.songpageview,name="songpageview"),
    path('search',views.searchbar,name="search"),
    path('whishlist',views.whishlist,name="wish"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
