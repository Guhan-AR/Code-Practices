from home import views
from django.urls import path , include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'people',views.Peopleviewset,basename='people')
urlpatterns = router.urls

urlpatterns = [
    path('',include(router.urls)),
    path('register/',views.RegisterAPI.as_view()),
    path('index/',views.index),
    path('person/',views.person),
    path('persons/',views.PersonAPI.as_view()),
    path('login/',views.login),
    path('loginn/',views.LoginAPI.as_view()),
]