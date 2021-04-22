from django.contrib.auth.models import User

from rest_framework import generics, filters
from .models import Association, Adopter, Pet, Address, AdoptionForm, Image

## We import this additional model to implement the image handling
from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import (
  # Association Serializers
  AssociationsListSerializer,
  AssociationsSerializer,
  AssociationsRegistSerializer,
  # Adopter Serializers
  AdoptersListSerializer,
  AdoptersSerializer,
  # Pet Serializers
  PetsListSerializer,
  PetsSerializer,
  # Address Serializers
  AddressesListSerializer,
  AddressesSerializer,
  # Adoption Form Serializers
  AdoptionFormsSerializer,
  # Relations Serializers
  AssociationPetsSerializer,
  AdopterPetsSerializer,
  AdopterAdoptionFormsSerializer,
  # Image Serializers
  AssociationsImagesSerializer,
)

# Create your views here.

### Image handler Views
class UpdateAssociationsImagesAPIView(generics.UpdateAPIView) :
  queryset = Image.objects.all()
  serializer_class = AssociationsImagesSerializer

class AssociationsViewSet(ReadOnlyModelViewSet) :
  queryset = Association.objects.all()
  serializer_class = AssociationsSerializer
class AdoptersViewSet(ReadOnlyModelViewSet) :
  queryset = Adopter.objects.all()
  serializer_class = AdoptersSerializer
class PetsViewSet(ReadOnlyModelViewSet) :
  queryset = Pet.objects.all()
  serializer_class = PetsSerializer

## Association Views
class ListAssociationsAPIView(generics.ListAPIView) :
  queryset = Association.objects.all()
  serializer_class = AssociationsListSerializer

class CreateAssociationsAPIView(generics.CreateAPIView) :
  queryset = Association.objects.all()
  serializer_class = AssociationsRegistSerializer

class RetrieveAssociationsAPIView(generics.RetrieveAPIView) :
  queryset = Association.objects.all()
  serializer_class = AssociationsSerializer

class UpdateAssociationsAPIView(generics.UpdateAPIView) :
  queryset = Association.objects.all()
  serializer_class = AssociationsSerializer

class DestroyAssociationsAPIView(generics.DestroyAPIView) :
  queryset = Association.objects.all()
  serializer_class = AssociationsSerializer

## Adopter View's
class ListAdoptersAPIView(generics.ListAPIView) :
  queryset = Adopter.objects.all()
  serializer_class = AdoptersListSerializer

class CreateAdoptersAPIView(generics.CreateAPIView) :
  queryset = Adopter.objects.all()
  serializer_class = AdoptersSerializer

class RetrieveAdoptersAPIView(generics.RetrieveAPIView) :
  queryset = Adopter.objects.all()
  serializer_class = AdoptersSerializer

class UpdateAdoptersAPIView(generics.UpdateAPIView) :
  queryset = Adopter.objects.all()
  serializer_class = AdoptersSerializer

class DestroyAdoptersAPIView(generics.DestroyAPIView) :
  queryset = Adopter.objects.all()
  serializer_class = AdoptersSerializer

## Pet View's
class ListPetsAPIView(generics.ListAPIView) :
  queryset = Pet.objects.all()
  serializer_class = PetsListSerializer

class CreatePetsAPIView(generics.CreateAPIView) :
  queryset = Pet.objects.all()
  serializer_class = PetsSerializer

class RetrievePetsAPIView(generics.RetrieveAPIView) :
  queryset = Pet.objects.all()
  serializer_class = PetsSerializer

class UpdatePetsAPIView(generics.UpdateAPIView) :
  queryset = Pet.objects.all()
  serializer_class = PetsSerializer

class DestroyPetsAPIView(generics.DestroyAPIView) :
  queryset = Pet.objects.all()
  serializer_class = PetsSerializer

## Address View's
class ListAddressesAPIView(generics.ListAPIView) :
  queryset = Address.objects.all()
  serializer_class = AddressesListSerializer

class CreateAddressesAPIView(generics.CreateAPIView) :
  queryset = Address.objects.all()
  serializer_class = AddressesSerializer

class RetrieveAddressesAPIView(generics.RetrieveAPIView) :
  queryset = Address.objects.all()
  serializer_class = AddressesSerializer

class UpdateAddressesAPIView(generics.UpdateAPIView) :
  queryset = Address.objects.all()
  serializer_class = AddressesSerializer

class DestroyAddressesAPIView(generics.DestroyAPIView) :
  queryset = Address.objects.all()
  serializer_class = AddressesSerializer

## Adoption Form View's
class ListAdoptionFormsAPIView(generics.ListAPIView) :
  queryset = AdoptionForm.objects.all()
  serializer_class = AdoptionFormsSerializer

class CreateAdoptionFormsAPIView(generics.CreateAPIView) :
  queryset = AdoptionForm.objects.all()
  serializer_class = AdoptionFormsSerializer

class RetrieveAdoptionFormsAPIView(generics.RetrieveAPIView) :
  queryset = AdoptionForm.objects.all()
  serializer_class = AdoptionFormsSerializer

class UpdateAdoptionFormsAPIView(generics.UpdateAPIView) :
  queryset = AdoptionForm.objects.all()
  serializer_class = AdoptionFormsSerializer

class DestroyAdoptionFormsAPIView(generics.DestroyAPIView) :
  queryset = AdoptionForm.objects.all()
  serializer_class = AdoptionFormsSerializer

## Relations View's
class RetrieveAssociationPetsAPIView(generics.RetrieveAPIView) :
  queryset = Association.objects.all()
  serializer_class = AssociationPetsSerializer

class RetrieveAdopterPetsAPIView(generics.RetrieveAPIView) :
  queryset = Adopter.objects.all()
  serializer_class = AdopterPetsSerializer

class RetrieveAdopterAdoptionFormsAPIView(generics.RetrieveAPIView) :
  queryset = Adopter.objects.all()
  serializer_class = AdopterAdoptionFormsSerializer