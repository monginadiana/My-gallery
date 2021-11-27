from django.conf.urls import url,include
from media import views

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^media/$',views.index,name= 'index'),
    url(r'^search/', views.search_results, name='search_results')
]

