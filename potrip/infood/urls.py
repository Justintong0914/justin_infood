from django.urls import path, re_path
from infood.views import infood_view
from.import views
from django.urls import include, path


urlpatterns = [
     
     path('',views.infood_view),

]