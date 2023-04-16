from django.urls import path,include
from APP import views
urlpatterns = [
    path("family",views.familylist.as_view()),
    path("child",views.childlist.as_view()),
]
