from django.contrib import admin 
from django.urls import path 
from serverslide import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('lampspower/',views.lampspower,name="lampspower"),
    path('',views.lampspower,name="lampspower")
]