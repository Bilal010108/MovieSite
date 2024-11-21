from .models import Movie
from django_filters import FilterSet


class MovieFilter(FilterSet):
    class Meta:
        model = Movie
        fields = {
            'year': ['gt', 'lt'],
            'country': ['exact'],
            'janre': ['exact'],
            'status_movie': ['exact'],
            'actor': ['exact'],
            'director': ['exact']
        }
