from django.conf.urls import url
from pools import views

urlpatterns = [
    url(r'^$',views.index)
]