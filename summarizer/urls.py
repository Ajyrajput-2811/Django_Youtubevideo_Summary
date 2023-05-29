from django.urls import path
from summarizer import views


urlpatterns = [
     path('',views.home,name='home'),
    path('summary/<int:pk>/',views.summary,name='summary'),
    path('api/',views.get_summary,name='get_summary'),
    

]