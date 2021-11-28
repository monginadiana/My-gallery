from django.conf.urls import url,include
from media import views

urlpatterns=[

    url('^$', views.index, name= 'index'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^image/(\d+)', views.image, name ='image')
]

