from django.conf.urls import url
from . import views


urlpatterns=[

url(r'^$', views.login, name='login'),
url(r'^Usuario/new',views.new_Usuario, name="new_Usuario")

]