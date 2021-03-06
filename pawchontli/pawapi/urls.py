from django.urls import path, include
from .views import (
  # Associations View's
  ListAssociationsAPIView,
  CreateAssociationsAPIView,
  RetrieveAssociationsAPIView,
  UpdateAssociationsAPIView,
  DestroyAssociationsAPIView,
  # Adopter View's
  ListAdoptersAPIView,
  CreateAdoptersAPIView,
  RetrieveAdoptersAPIView,
  UpdateAdoptersAPIView,
  DestroyAdoptersAPIView,
  # Pet View's
  ListPetsAPIView,
  CreatePetsAPIView,
  RetrievePetsAPIView,
  UpdatePetsAPIView,
  DestroyPetsAPIView,
  # Address View's
  ListAddressesAPIView,
  CreateAddressesAPIView,
  RetrieveAddressesAPIView,
  UpdateAddressesAPIView,
  DestroyAddressesAPIView,
  # Adoption View's
  ListAdoptionFormsAPIView,
  CreateAdoptionFormsAPIView,
  RetrieveAdoptionFormsAPIView,
  UpdateAdoptionFormsAPIView,
  DestroyAdoptionFormsAPIView,
  # Relation View's
  RetrieveAssociationPetsAPIView,
  RetrieveAdopterPetsAPIView,
  RetrieveAdopterAdoptionFormsAPIView,
  # Image handler
  AssociationsViewSet,
  AdoptersViewSet,
  PetsViewSet,
)
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register(r'associations', AssociationsViewSet)
# router.register(r'adopters', AdoptersViewSet)
# router.register(r'pets', PetsViewSet)

urlpatterns = [
  ## Image URL's
  # path('', include(router.urls)),
  ## Associations URL's
  path('associations/', ListAssociationsAPIView.as_view(), name='list-associations'),
  path('associations/create/', CreateAssociationsAPIView.as_view(), name='create-associations'),
  path('associations/<int:pk>/', RetrieveAssociationsAPIView.as_view(), name='retrieve-associations'),
  path('associations/<int:pk>/update/', UpdateAssociationsAPIView.as_view(), name='update-associations'),
  path('associations/<int:pk>/destroy/', DestroyAssociationsAPIView.as_view(), name='destroy-associations'),
  ## Adopter URL's
  path('adopters/', ListAdoptersAPIView.as_view(), name='list-adopters'),
  path('adopters/create/', CreateAdoptersAPIView.as_view(), name='create-adopters'),
  path('adopters/<int:pk>/', RetrieveAdoptersAPIView.as_view(), name='retrieve-adopters'),
  path('adopters/<int:pk>/update/', UpdateAdoptersAPIView.as_view(), name='update-adopters'),
  path('adopters/<int:pk>/destroy/', DestroyAdoptersAPIView.as_view(), name='destroy-adopters'),
  ## Pet URL's
  path('pets/', ListPetsAPIView.as_view(), name='list-pets'),
  path('pets/create/', CreatePetsAPIView.as_view(), name='create-pets'),
  path('pets/<int:pk>/', RetrievePetsAPIView.as_view(), name='retrieve-pets'),
  path('pets/<int:pk>/update/', UpdatePetsAPIView.as_view(), name='update-pets'),
  path('pets/<int:pk>/destroy/', DestroyPetsAPIView.as_view(), name='destroy-pets'),
  ## Address URL's
  path('addresses/', ListAddressesAPIView.as_view(), name='list-addresses'),
  path('addresses/create/', CreateAddressesAPIView.as_view(), name='create-addresses'),
  path('addresses/<int:pk>/', RetrieveAddressesAPIView.as_view(), name='retrieve-addresses'),
  path('addresses/<int:pk>/update/', UpdateAddressesAPIView.as_view(), name='update-addresses'),
  path('addresses/<int:pk>/destroy/', DestroyAddressesAPIView.as_view(), name='destroy-addresses'),
  ## Adoption Form URL's
  path('adoption_forms/', ListAdoptionFormsAPIView.as_view(), name='list-adoption-forms'),
  path('adoption_forms/create/', CreateAdoptionFormsAPIView.as_view(), name='create-adoption-forms'),
  path('adoption_forms/<int:pk>/', RetrieveAdoptionFormsAPIView.as_view(), name='retrieve-adoption-forms'),
  path('adoption_forms/<int:pk>/update/', UpdateAdoptionFormsAPIView.as_view(), name='update-adoption-forms'),
  path('adoption_forms/<int:pk>/destroy/', DestroyAdoptionFormsAPIView.as_view(), name='destroy-adoption-forms'),
  ## Relations URL's
  path('associations/<int:pk>/pets/', RetrieveAssociationPetsAPIView.as_view(), name='retrieve-association-pets'),
  path('adopters/<int:pk>/pets/', RetrieveAdopterPetsAPIView.as_view(), name='retrieve-adopter-pets'),
  path('adopters/<int:pk>/adoption_forms/', RetrieveAdopterAdoptionFormsAPIView.as_view(), name='retrieve-adopter-adoption-forms'),
]