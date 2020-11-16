from django.urls import path
from demo_app.views import index

urlpatterns = (
    path('', index, name='index'),
)
