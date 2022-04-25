from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[  
    path(r'^$',views.index,name='index'),
    path(r'register/',views.register, name='registration'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path(r'^accounts/', include('registration.backends.simple.urls')),
    path(r'profile/', views.profile, name='profile'),
    path('createHood/', views.create_neighbourhood, name='createHood'),
    path('joinhood/<id>', views.join_neighbourhood, name='joinhood'),   
    path('leavehood/<id>', views.leave_neighbourhood, name='leavehood'),
    path('singleHood/<hood_id>', views.single_neighbourhood, name='singleHood'),
    path('<hood_id>/post/', views.create_post, name='post'),
    path('<hood_id>/business/', views.add_business, name='business'),
    path(r'^searchbusiness/', views.search_business, name='search'),
]