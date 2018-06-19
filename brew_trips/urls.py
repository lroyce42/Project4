from django.urls import path
from . import views

urlpatterns = [
path('',views.home,name='home'),
# path('create/',views.create,name='create'),
path('brewmap/',views.brewmap,name='brewmap'),
path('<int:brewery_id>/delete/',views.delete, name='delete'),

# path('update/',views.update,name='update'),
]
