"""procurementmanagementsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from pms import views
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "Comms Lodge Admin"
admin.site.site_title = "Comms Lodge Admin Portal"
admin.site.index_title = "Welcome to Comms Lodge"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",views.home,name="home"),
    path('', views.loginUser,name="login"),
    path('logout/', views.logoutUser,name="logout"),
    path('createuser/', views.createuser,name="createuser"), 
    path('createuser1/', views.createuser1,name="createuser1"), 
    path('forgot/', views.forgot,name="forgot"),
    path('edituser/', views.edituser,name=""), 
    path('createcompany/', views.createcompany,name="createcompany"),
    path('searchuser/', views.searchuser,name="usersearch"),
    path('searchcompany/', views.searchcompany,name="companysearch"),
    path('showuser/', views.showuser,name=""),
    path('showcompany/', views.showcompany,name=""),
    path('chatroom1/', views.chatroom1,name=""),
    path('addemp/', views.addemp,name=""),
    path('remove/', views.remove,name=""),
    path('removeemp/', views.removeemp,name=""),
    path('addchatroom/', views.addchatroom,name=""),
    path('addchatroom2/', views.addchatroom2,name=""),
    path('readuser/', views.readuser,name=""),
    path('readcompany/', views.readcompany,name=""),
    path('editcompany/', views.editcompany,name=""),
    path('chatrooms_admin/', views.chatroom4,name=""),
    path('chatrooms_emp/', views.chatroom5,name=""),
    path('chatrooms_client/', views.chatroom6,name=""),
    path('sendmessage/', views.sendmessage,name=""),
    path('sendmessageemp/', views.sendmessageemp,name=""),
    path('sendmessageclient/', views.sendmessagec,name=""),
    path('chatroom_sidebar/', views.chatroom_sidebar,name=""),
    path('chatroom_sidebar_emp/', views.chatroom_sidebar,name=""),
    path('payment/', views.payment,name=""),
    path('resetpass/<token>/', views.resetpass,name=""),
    path('paydetail/', views.paydetail,name=""),
    path('room/', views.room,name=""),
    path('editchatroom/', views.editchatroom,name=""),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)