from  django.urls import path
from .views import *
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MovieFilter
from  rest_framework.filters import SearchFilter, OrderingFilter


urlpatterns =[

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),


    path('', MovieListViewSet.as_view({'get':'list','post': 'create'}), name='movie_list'),
    path('<int:pk>/', MovieDetailViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                              'delete': 'destroy'}), name='movie_detail'),

    path('profile/',ProfileViwSet.as_view({'get': 'list', 'post': 'create'}), name='movie_list'),
    path('profile/<int:pk/', ProfileViwSet.as_view({'get': 'retrieve', 'put': 'update',
                                                      'delete': 'destroy'}), name='movie_detail'),

    path('country/',CountryViewSet.as_view({'get':'list','post':'create'}), name='movie_detail'),
    path('country/<int:pk/', CountryViewSet.as_view({'get':'retrieve','put':'update',
                                                      'delete':'destroy'}), name = 'movie_detail'),

    path('director/', DirectorViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie_detail'),
    path('director/<int:pk/', DirectorViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                     'delete': 'destroy'}), name='movie_detail'),



    path('actor/', ActorViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie_detail'),
    path('actor/<int:pk/', ActorViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                     'delete': 'destroy'}), name='movie_detail'),



    path('janre/', JanreViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie_detail'),
    path('janre/<int:pk/', JanreViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                     'delete': 'destroy'}), name='movie_detail'),


    path('movie/', MovieViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie_detail'),
    path('movie/<int:pk/',MovieViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                     'delete': 'destroy'}), name='movie_detail'),

    path('movie_language/', MovieLanguagesViewSet.as_view({'get': 'list', }), name='movie_languages_list'),
    path('movie_language/<int:pk>/', MovieLanguagesViewSet.as_view({'get': 'retrieve', }), name='movie_languages_detail'),

    path('moments/', MomentsViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie_detail'),
    path('moments/<int:pk/',  MomentsViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                 'delete': 'destroy'}), name='movie_detail'),

    path('rating/', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie_detail'),
    path('rating  /<int:pk/', RatingViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                 'delete': 'destroy'}), name='movie_detail'),

    path('favorite/', FavoriteViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie_detail'),
    path('favorite  /<int:pk/', FavoriteViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                     'delete': 'destroy'}), name='movie_detail'),

    path('FavoriteMovie/', FavoriteMovieViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie_detail'),
    path('FavoriteMovie /<int:pk/',FavoriteMovieViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                      'delete': 'destroy'}), name='movie_detail'),

    path('history/', HistoryViewSet.as_view({'get': 'list', 'post': 'create'}), name='movie_detail'),
    path('history /<int:pk/', HistoryViewSet.as_view({'get': 'retrieve', 'put': 'update',
                                                     'delete': 'destroy'}), name='movie_detail'),
    ]












