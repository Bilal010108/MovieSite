from .models import *
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model =Profile
        fields =  ('username', 'email', 'password', 'first_name', 'last_name', 'age',
                  'phone_number', 'status')
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = Profile.objects.create_user(**validated_data)
        return user
    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }





class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError('Неверные учетные данные')

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }






class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['country_name']


class DirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Director
        fields = ['director_name']




class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['actor_name']

class JanreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Janre
        fields = '__all__'


class MovieLanguagesLangSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieLanguages
        fields = '__all__'

class MomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moments
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'



class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class FavoriteMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteMovie
        fields = '__all__'


class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = '__all__'


class MovieListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'description', 'movie_trailer', 'movie_image']

    def get_average_rating(self, obj):
        return obj.get_average_rating()


class MovieDetailSerializer(serializers.ModelSerializer):
 class Meta:
        model = Movie
        fields = ['movie_name','country','director','actor','janre','types','description',
                  'movie_time',  'movie_trailer', 'movie_image','status_movie','year']

 def get_average_rating(self, obj):
        return obj.get_average_rating()


