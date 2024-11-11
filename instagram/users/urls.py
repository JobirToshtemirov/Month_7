from django.urls import path
from .views import CreateUserModelView


urlpatterns = [

    path('signup/', CreateUserModelView.as_view()),

]