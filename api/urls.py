from django.urls import path,include
from rest_framework.routers import DefaultRouter
from APP import views

# router=DefaultRouter()
# router.register(r'family',views.familylist.as_view(),basename="family-list")
# router.register(r'child',views.childlist.as_view(),basename="child-list")
# urlpatterns=router.urls

urlpatterns = [
    # path("",include('router.urls')),
    path("family",views.familylist.as_view()),
    path("child",views.childlist.as_view()),
]
