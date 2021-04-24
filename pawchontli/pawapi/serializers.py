from rest_framework import serializers
from .models import Association, Adopter, Pet, AdoptionForm

# Serializers define the API representation

## Association Serializers
class AssociationsListSerializer(serializers.ModelSerializer) :
  class Meta:
    model = Association
    fields = [
      'id',
      'name',
      'email',
      'first_name_contact',
      'last_name_contact',
      'email_contact',
    ]

class AssociationsSerializer(serializers.ModelSerializer) :
  class Meta:
    model = Association
    fields = '__all__'

class AssociationsRegistSerializer(serializers.ModelSerializer) :
  class Meta:
    model = Association
    fields = '__all__'

## Adopter Serializers
class AdoptersListSerializer(serializers.ModelSerializer) :
  class Meta:
    model = Adopter
    fields = [
      'id',
      'first_name',
      'last_name',
    ]

class AdoptersSerializer(serializers.ModelSerializer) :
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
    ]

class PetsSerializer(serializers.ModelSerializer) :
  class Meta:
    model = Pet
    fields = '__all__'





## Adoption Forms Serializers
class AdoptionFormsSerializer(serializers.ModelSerializer) :
  class Meta:
    model = AdoptionForm
    fields = '__all__'



## Relations Serializers
class AssociationPetsSerializer(serializers.ModelSerializer) :
  pets = PetsListSerializer

  class Meta:
    model = Association
    fields = [
      'id',
      'name',
      'pets',
    ]



class AdopterAdoptionFormsSerializer(serializers.ModelSerializer) :
  adoption_forms = AdoptionFormsSerializer

  class Meta:
    model = Adopter
    fields = [
      'id',
      'first_name',
      'last_name',
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