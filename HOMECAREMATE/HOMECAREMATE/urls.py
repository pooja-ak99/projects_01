"""
URL configuration for HOMECAREMATE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from ServiceApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home,name="home"),
    path("categorypage/<c1>",views.categorypage,name="categorypage"),
    path("allcategory",views.allcategory,name="allcategory"),
    path("customreg",views.customreg,name="customreg"),
    path("serviceproviderreg",views.serviceproviderreg,name="serviceproviderreg"),
    path("adminreg",views.adminreg,name="adminreg"),
    path('login',views.user_login,name="login"),
    path('logout',views.user_logout,name="logout"),
    path('career',views.career,name="career"),
    path('careerapply',views.careerapplication,name="careerapply"),
    path('careerapplications',views.careerapplications,name="careerapplications"),
    path("booking",views.booking,name="booking"),
    path("applicationslist",views.applicationslist,name="applicationslist"),
    path("delete/<int:p>",views.delete,name="delete"),
    path("bookinglist",views.bookinglist,name="bookinglist"),
    path("remove/<int:p>",views.remove,name="remove"),
    path("addcategory",views.addcategory,name="addcategory"),
    path("empdetail",views.empdetail,name="empdetail"),
    path("editcategory/<int:p>",views.editcategory,name="editcategory"),
    path("viewcategory",views.viewcategory,name="viewcategory"),
    path("deletecategory/<int:p>",views.deletecategory,name="erase"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
