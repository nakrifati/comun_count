from django.conf.urls import url
from count_page import views


urlpatterns = [

    url(r'', views.count_page, name='count_page'),
    url(r'add_com_action', views.add_com_action, name='add_com_action'),

]

