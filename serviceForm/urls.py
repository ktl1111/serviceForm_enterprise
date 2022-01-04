from django.urls import path
from serviceForm import views

app_name = 'serviceForm'
urlpatterns = [
    path('category/', views.category, name='category'),
    path('categoryCreate/', views.categoryCreate, name='categoryCreate'),
    path('categoryUpdate/<int:categoryid>/', views.categoryUpdate, name='categoryUpdate'),
    path('categoryDelete/<int:categoryid>/', views.categoryDelete, name='categoryDelete'),
    path('categoryRead/<int:categoryid>/', views.categoryRead, name='categoryRead'),
    path('form/', views.form, name='form'),
    path('newForm/', views.newForm, name='newForm'),
    # path('hospital/', views.hospital, name='hospital'),
]