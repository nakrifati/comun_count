from django.conf.urls import url
from count_page import views


urlpatterns = [

    url(r'', views.count_page, name='count_page'),

]

