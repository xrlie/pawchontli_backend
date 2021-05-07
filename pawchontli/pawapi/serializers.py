from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Association, Adopter, Pet, AdoptionForm

# Serializers define the API representation

## User Serializer
class UsersSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = [
      'username',
      'first_name',
      'last_name',
      'email',
    ]

class AdoptersUsersSerializer(serializers.Serializer):
  username = serializers.CharField(max_length=255)
  first_name = serializers.CharField(max_length=255)
  last_name = serializers.CharField(max_length=255)
  email = serializers.EmailField()
  password = serializers.CharField(max_length=50)

class AssociationsUsersSerializer(serializers.Serializer):
  username = serializers.CharField(max_length=255)
  email = serializers.EmailField()
  password = serializers.CharField(max_length=50)


## Association Serializers
class AssociationsListSerializer(serializers.ModelSerializer) :
  user = UsersSerializer(many=False)
  class Meta:
    model = Association
    fields = [
      'id',
      'user',
      'first_name_contact',
      'last_name_contact',
    ]

class AssociationsSerializer(serializers.ModelSerializer) :
  user = UsersSerializer(many=False)
  class Meta:
    model = Association
    fields = '__all__'

class AssociationsRegistSerializer(serializers.ModelSerializer) :
  class Meta:
    model = Association
    fields = '__all__'

## Adopter Serializers
class AdoptersListSerializer(serializers.ModelSerializer) :
  user = UsersSerializer(many=False)
  class Meta:
    model = Adopter
    fields = [
      'id',
      'user',
      'image',
    ]

class AdoptersSerializer(serializers.ModelSerializer) :
  user = UsersSerializer(many=False)
  class Meta:
    model = Adopter
    fields = '__all__'

## Pet Serializers
class PetsListSerializer(serializers.ModelSerializer) :
  class Meta:
    model = Pet
    fields = [
      'id',
      'name',
      'species',
      'image',
    ]

class PetsSerializer(serializers.ModelSerializer) :
  class Meta:
    model = Pet
    fields = [
      'id',
      'name',
      'species',
      'age',
      'gender',
      'size',
      'character',
      'story',
      'special_needs',
      'association',
    ]

class ViewPetsSerializer(serializers.ModelSerializer) :
  association = AssociationsListSerializer(many=False)
  class Meta:
    model = Pet
    # fields = '__all__'
    fields = [
      'id',
      'name',
      'species',
      'age',
      'gender',
      'size',
      'character',
      'story',
      'special_needs',
      'image',
      'association',
    ]





## Adoption Forms Serializers
class AdoptionFormsSerializer(serializers.ModelSerializer) :
  adopter = AdoptersSerializer#(many=False)
  pet = ViewPetsSerializer#(many=False)
  
  class Meta:
    model = AdoptionForm
    fields = [
      'id',
      'amount_pets_today',
      'which_pets_today',
      'amount_pets_past',
      'story_pets_past',
      'everyone_agrees',
      'allowed_to_own',
      'if_change_address',
      'average_age',
      'place_of_sleep',
      'time_by_itself',
      'petcare_awareness',
      'pet_responsable',
      'veterinarian',
      'adopter',
      'pet',
      'created_at',
    ]

class ListAdoptionFormSerializer(serializers.ModelSerializer):
  adopter = serializers.StringRelatedField(many=False)    
  pet = serializers.StringRelatedField(many=False)  
  class Meta:
    model = AdoptionForm
    fields = [
      'id',
      'amount_pets_today',
      'which_pets_today',
      'amount_pets_past',
      'story_pets_past',
      'everyone_agrees',
      'allowed_to_own',
      'if_change_address',
      'average_age',
      'place_of_sleep',
      'time_by_itself',
      'petcare_awareness',
      'pet_responsable',
      'veterinarian',
      'adopter',
      'pet',
      'created_at',
    

    ]


class UpdateAdoptionFormsSerializer(serializers.ModelSerializer):
  class Meta:
    model = AdoptionForm
    fields = '__all__'


## Relations Serializers
class AssociationPetsSerializer(serializers.ModelSerializer) :
  user = UsersSerializer(many=False)
  pets = PetsListSerializer(many=True)

  class Meta:
    model = Association
    fields = [
      'id',
      'user',
      'pets',
    ]



class AdopterAdoptionFormsSerializer(serializers.ModelSerializer) :
  user = UsersSerializer(many=False)
  adoption_forms = AdoptionFormsSerializer

  class Meta:
    model = Adopter
    fields = [
      'id',
      'user',
      'adoption_forms',
    ]

class PetAdoptionFormsSerializer(serializers.ModelSerializer) :
  adoption_forms = AdoptionFormsSerializer

  class Meta:
    model= Pet
    fields = [
      'id',
      'name',
      'species',
    ]

## Prueba
class prueba(serializers.Serializer):
  association_id = serializers.CharField(max_length=50)
  name = serializers.CharField(max_length=255)
  species = serializers.CharField(max_length=50)
  gender = serializers.CharField(max_length=10)
  size = serializers.CharField(max_length=50)
  character = serializers.CharField(max_length=30)
  story = serializers.CharField(max_length=1000)
  special_needs = serializers.CharField(max_length=1000)
  image = serializers.ImageField()
  
  # association = AssociationsListSerializer(many=True)
  # class Meta:
  #   model = Pet
  #   fields = [
  #     'association',
  #     'id',
  #     'name',
  #     'species',
  #     'age',
  #     'gender',
  #     'size',
  #     'character',
  #     'story',
  #     'special_needs',
  #     'image',
  #   ]

## Pet creation from Association
# class AssociationCreatePetSerializer(serializers.ModelSerializer) :
#   pets = PetsSerializer(many=True)
#   class Meta:
#     model = Association
#     fields = [
#       'id',
#       'name',
#       'pets',
#     ]
#     def create(self, validated_data):
#       pets_data = validated_data.pop('pets')
#       album = Album.objects.get(self.reque)
#       for track_data in tracks_data:
#           Track.objects.create(album=album, **track_data)
#       return album