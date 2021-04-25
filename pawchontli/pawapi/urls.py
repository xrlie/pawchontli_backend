from django.urls import path, include
from django.contrib.auth import views as auth_views

from .views import (
  # User View
  CreateUserAPIView,
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
  # Adoption View's
  ListAdoptionFormsAPIView,
  CreateAdoptionFormsAPIView,
  RetrieveAdoptionFormsAPIView,
  UpdateAdoptionFormsAPIView,
  DestroyAdoptionFormsAPIView,
  # Relation View's
  RetrieveAssociationPetsAPIView,
  RetrieveAdopterAdoptionFormsAPIView,
  RetrievePetAdoptionFormsAPIView,
)




urlpatterns = [
  ## User Login 
  path('login/', CreateUserAPIView.as_view(), name='user-login'),
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
  ## Adoption Form URL's
  path('adoption_forms/', ListAdoptionFormsAPIView.as_view(), name='list-adoption-forms'),
  path('adoption_forms/create/', CreateAdoptionFormsAPIView.as_view(), name='create-adoption-forms'),
  path('adoption_forms/<int:pk>/', RetrieveAdoptionFormsAPIView.as_view(), name='retrieve-adoption-forms'),
  path('adoption_forms/<int:pk>/update/', UpdateAdoptionFormsAPIView.as_view(), name='update-adoption-forms'),
  path('adoption_forms/<int:pk>/destroy/', DestroyAdoptionFormsAPIView.as_view(), name='destroy-adoption-forms'),
  ## Relations URL's
  path('associations/<int:pk>/pets/', RetrieveAssociationPetsAPIView.as_view(), name='retrieve-association-pets'),
  path('pets/<int:pk>/adoption_forms/', RetrievePetAdoptionFormsAPIView.as_view(), name='retrieve-pets-adoption-forms'),
  path('adopters/<int:pk>/adoption_forms/', RetrieveAdopterAdoptionFormsAPIView.as_view(), name='retrieve-adopter-adoption-forms'),
]