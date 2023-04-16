from django.urls import path,include
from APP.views import *
from rest_framework import routers

my_router=routers.DefaultRouter()
my_router.register(r'family',familyviewset)
my_router.register(r'child',childviewset)
my_router.register(r'cow',cowviewset)
my_router.register(r'sheap',sheapviewset)
my_router.register(r'goat',goatviewset)
urlpatterns=my_router.urls

urlpatterns = [
    path("",include(my_router.urls)),
    path("family",familylist.as_view()),
    path("child",childlist.as_view()),
    path("cow",cowlist.as_view()),
    path("sheap",sheaplist.as_view()),
    path("goat",goatlist.as_view()),
]
