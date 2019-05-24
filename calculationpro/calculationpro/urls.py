#from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls import url
from calculationapp import views

urlpatterns = [
    url(r'^admin/',admin.site.urls),
    url(r'^$',views.input),
    url(r'^calculationapp/output$',views.output),
    url(r'^add$',views.add),
    url(r'^sub$',views.sub),
    url(r'^mul$',views.mul),
    url(r'^div$',views.div),
]
