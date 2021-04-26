from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.dispatch import receiver
from django.db.models.signals import post_save

from rest_framework import generics, filters
from .models import Association, Adopter, Pet, AdoptionForm

## We import this additional model to implement the image handling
from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import (
    # User Serializer
    UsersSerializer,
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
    ViewPetsSerializer,
    # Adoption Form Serializers
    AdoptionFormsSerializer,
    # Relations Serializers
    AssociationPetsSerializer,
    PetAdoptionFormsSerializer,
    AdopterAdoptionFormsSerializer,
)

# Create your views here.

### User Authentication
class CreateUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = []

@receiver(post_save, sender=User)
def adopter_profile(sender, instance, created, **kwargs):
  if created:
    Adopter.objects.create(
        email=instance.email, 
        first_name=instance.username,
      )


class CustomAuthToken(ObtainAuthToken):
  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(
        data=request.data, context={"request": request}
    )
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data["user"]
    token, created = Token.objects.get_or_create(user=user)
    return Response({"token": token.key, "user_id": user.pk, "email": user.email})


## Association Views
class ListAssociationsAPIView(generics.ListAPIView):
    queryset = Association.objects.all()
    serializer_class = AssociationsListSerializer


class CreateAssociationsAPIView(generics.CreateAPIView):
    queryset = Association.objects.all()
    serializer_class = AssociationsRegistSerializer


class RetrieveAssociationsAPIView(generics.RetrieveAPIView):
    queryset = Association.objects.all()
    serializer_class = AssociationsSerializer


class UpdateAssociationsAPIView(generics.UpdateAPIView):
    queryset = Association.objects.all()
    serializer_class = AssociationsSerializer


class DestroyAssociationsAPIView(generics.DestroyAPIView):
    queryset = Association.objects.all()
    serializer_class = AssociationsSerializer


## Adopter View's
class ListAdoptersAPIView(generics.ListAPIView):
    queryset = Adopter.objects.all()
    serializer_class = AdoptersListSerializer
    permission_classes = []



class CreateAdoptersAPIView(generics.CreateAPIView):
    queryset = Adopter.objects.all()
    serializer_class = AdoptersSerializer
    permission_classes = []



class RetrieveAdoptersAPIView(generics.RetrieveAPIView):
    queryset = Adopter.objects.all()
    serializer_class = AdoptersSerializer


class UpdateAdoptersAPIView(generics.UpdateAPIView):
    queryset = Adopter.objects.all()
    serializer_class = AdoptersSerializer


class DestroyAdoptersAPIView(generics.DestroyAPIView):
    queryset = Adopter.objects.all()
    serializer_class = AdoptersSerializer


## Pet View's
class ListPetsAPIView(generics.ListAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsListSerializer


class CreatePetsAPIView(generics.CreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer


class RetrievePetsAPIView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = ViewPetsSerializer


class UpdatePetsAPIView(generics.UpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer


class DestroyPetsAPIView(generics.DestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer


## Adoption Form View's
class ListAdoptionFormsAPIView(generics.ListAPIView):
    queryset = AdoptionForm.objects.all()
    serializer_class = AdoptionFormsSerializer


class CreateAdoptionFormsAPIView(generics.CreateAPIView):
    queryset = AdoptionForm.objects.all()
    serializer_class = AdoptionFormsSerializer


class RetrieveAdoptionFormsAPIView(generics.RetrieveAPIView):
    queryset = AdoptionForm.objects.all()
    serializer_class = AdoptionFormsSerializer


class UpdateAdoptionFormsAPIView(generics.UpdateAPIView):
    queryset = AdoptionForm.objects.all()
    serializer_class = AdoptionFormsSerializer


class DestroyAdoptionFormsAPIView(generics.DestroyAPIView):
    queryset = AdoptionForm.objects.all()
    serializer_class = AdoptionFormsSerializer


## Relations View's
class RetrieveAssociationPetsAPIView(generics.RetrieveAPIView):
    queryset = Association.objects.all()
    serializer_class = AssociationPetsSerializer


class RetrieveAdopterAdoptionFormsAPIView(generics.RetrieveAPIView):
    queryset = Adopter.objects.all()
    serializer_class = AdopterAdoptionFormsSerializer


class RetrievePetAdoptionFormsAPIView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetAdoptionFormsSerializer
