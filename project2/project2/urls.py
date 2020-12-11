"""project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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

from django.conf import settings
from django.conf.urls.static import static
import app1.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app1.views.home, name='home'),

	path('main2/', app1.views.main2, name='main2'),
	path('pictures/', app1.views.pictures, name='pictures'),
	
	#servo
    path('main2/left', app1.views.left, name='left'),
    path('main2/right', app1.views.right, name='right'),
    path('main2/up', app1.views.up, name='up'),
    path('main2/down', app1.views.down, name='down'),
#	path('main2/<int:servo>/<int:angle>', app1.views.moveServo, name='moveServo'),
	
	#wheels	
    path('main2/front', app1.views.front, name='front'),
    path('main2/back', app1.views.back, name='back'),
    path('main2/cl_wise', app1.views.cl_wise, name='cl_wise'),
    path('main2/counter_cl', app1.views.counter_cl, name='counter_cl'),
    path('main2/stop', app1.views.stop, name='stop'),
    path('main2/speed_up', app1.views.speed_up, name='speed_up'),
    path('main2/speed_down', app1.views.speed_down, name='speed_down'),

	#dance
	path('main2/dance_1', app1.views.dance_1, name='dance_1'),
	path('main2/dance_2', app1.views.dance_2, name='dance_2'),

    #camera
	path('stream/', app1.views.stream, name='stream'),
	path('playback/', app1.views.playback, name='playback'),
	path('playback/<slug:select_image>/', app1.views.playback_show, name='playback_show'),

	path('delete_edit/<int:abc>/', app1.views.delete_edit, name='delete_edit'),
#	path('edit_name/<int:abc>/', app1.views.edit_name, name='edit_name'),
	
#login
	path('login/', app1.views.login, name ='login'),	
	path('logout/', app1.views.logout, name ='logout'),	

#acoustic

	path('from_robot/', app1.views.from_robot, name ='from_robot'),	
	path('to_robot/', app1.views.to_robot, name ='to_robot'),	
	path('speak/', app1.views.genAudioStreamResponse, name ='speak'),	
	
#	url(r'^playback/(?P<select_image>\w+)/$', views.playback_show, name='playback_show'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




