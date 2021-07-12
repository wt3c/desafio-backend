from django.urls import path, re_path
from ..desafio import views

# from desafio.views import ...


urlpatterns = [re_path(r'^$', views.homepage, name='homepage'),
               re_path(r'objdocumento/(?P<pk>.*)/|$', views.objDocumento.as_view(), name='objDocumento')]
