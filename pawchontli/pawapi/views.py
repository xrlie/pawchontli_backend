from django.contrib.auth.models import User
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.views import APIView

from rest_framework import generics, filters
from .models import Association, Adopter, Pet, AdoptionForm

## We import this additional model to implement the image handling
from rest_framework.viewsets import ReadOnlyModelViewSet

from .serializers import (
    # User Serializer
    AdoptersUsersSerializer,
    AssociationsUsersSerializer,
    # RegistAdoptersSerializer,
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
    UpdateAdoptionFormsSerializer,
    ListAdoptionFormSerializer,
    # Relations Serializers
    AssociationPetsSerializer,
    PetAdoptionFormsSerializer,
    AdopterAdoptionFormsSerializer,
    ## Prueba
    prueba,
)

# Create your views here.

### User Authentication
class CreateAdopterUserAPIView(APIView):
  serializer_class = AdoptersUsersSerializer
  permission_classes = []

  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(
        data=request.data, context={"request": request}
    )
    serializer.is_valid(raise_exception=True)
    user = User.objects.create(username=serializer.validated_data['username'], first_name=serializer.validated_data['first_name'],   last_name=serializer.validated_data['last_name'], email=serializer.validated_data['email'])
    user.set_password(serializer.validated_data['password'])
    user.save()
    adopter = Adopter.objects.create(user=user)
    return Response({"user_id": user.id, "adopter_id": adopter.id, "email": user.email})

class CreateAssociationUserAPIView(APIView):
  serializer_class = AssociationsUsersSerializer
  permission_classes = []

  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(
        data=request.data, context={"request": request}
    )
    serializer.is_valid(raise_exception=True)
    user = User.objects.create(username=serializer.validated_data['username'], email=serializer.validated_data['email'])
    user.set_password(serializer.validated_data['password'])
    user.save()
    association = Association.objects.create(user=user)
    return Response({"user_id": user.id, "association_id": association.id, "email": user.email})

class AssociationAuthToken(ObtainAuthToken):
  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(
      data=request.data, context={'request': request}
    )
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data["user"]
    token, created = Token.objects.get_or_create(user=user)
    return Response({"token":token.key, "association_id":user.associations.id, "email": user.email, "is_adopter":False})

class AdopterAuthToken(ObtainAuthToken):
  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(
      data=request.data, context={'request': request}
    )
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data["user"]
    token, created = Token.objects.get_or_create(user=user)
    return Response({"token":token.key, "adopter_id":user.adopters.id, "email": user.email, "is_adopter":True})

class CustomAuthToken(ObtainAuthToken):
  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(
        data=request.data, context={"request": request}
    )
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data["user"]
    token, created = Token.objects.get_or_create(user=user)
    return Response({"token": token.key, "user_id": user.pk, "email": user.email})

## Código prueba
class CreateAssociationsPetsAPIView(APIView) :
  # queryset = Association.objects.all()
  serializer_class = prueba
  permission_classes = []
  
  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(
        data=request.data, context={"request": request}
    )
    serializer.is_valid(raise_exception=True)
    association = Association.objects.get(id=serializer.validated_data['association_id'])
    serializer.validated_data.pop('association_id')
    pet = Pet.objects.create(association=association,**serializer.validated_data)
    return Response({"association_id": association.id, "pet_id": pet.id})


## Association Views
class ListAssociationsAPIView(generics.ListAPIView):
  queryset = Association.objects.all()
  serializer_class = AssociationsListSerializer
  permission_classes = []


class CreateAssociationsAPIView(generics.CreateAPIView):
    queryset = Association.objects.all()
    serializer_class = AssociationsRegistSerializer


class RetrieveAssociationsAPIView(generics.RetrieveAPIView):
    queryset = Association.objects.all()
    serializer_class = AssociationsSerializer
    permission_classes = []


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
    permission_classes = []


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
    permission_classes = []


class CreatePetsAPIView(generics.CreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer


class RetrievePetsAPIView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = ViewPetsSerializer
    permission_classes = []


class UpdatePetsAPIView(generics.UpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer


class DestroyPetsAPIView(generics.DestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer


## Adoption Form View's
class ListAdoptionFormsAPIView(generics.ListAPIView):
    # queryset = Pet.objects.all()
    serializer_class = ListAdoptionFormSerializer
    # permission_classes = []

    def get(self,request):
        association=Association.objects.get(user=request.user)
        pets=Pet.objects.filter(association=association).exclude(adoption_pets__isnull=True)
        queryset= AdoptionForm.objects.filter(pet__in=pets)
        # print([pet.adoption_pets for pet in queryset.all()])

        serializer=ListAdoptionFormSerializer(queryset, many=True)
       
        return Response(serializer.data)
    


        


class CreateAdoptionFormsAPIView(generics.CreateAPIView):
    queryset = AdoptionForm.objects.all()
    serializer_class = AdoptionFormsSerializer
    
    def post(self, request):
        request.data["adopter"]=request.user.id
        serializer=AdoptionFormsSerializer(data=request.data)
        print(request.user.id)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    
        

    
    


class RetrieveAdoptionFormsAPIView(generics.RetrieveAPIView):
    queryset = AdoptionForm.objects.all()
    serializer_class = AdoptionFormsSerializer
    permission_classes = []


class UpdateAdoptionFormsAPIView(generics.UpdateAPIView):
    queryset = AdoptionForm.objects.all()
    serializer_class = UpdateAdoptionFormsSerializer
    permission_classes = []


class DestroyAdoptionFormsAPIView(generics.DestroyAPIView):
    queryset = AdoptionForm.objects.all()
    serializer_class = AdoptionFormsSerializer


## Relations View's
class RetrieveAssociationPetsAPIView(generics.RetrieveAPIView):
    queryset = Association.objects.all()
    serializer_class = AssociationPetsSerializer
    permission_classes = []


class RetrieveAdopterAdoptionFormsAPIView(generics.RetrieveAPIView):
    queryset = Adopter.objects.all()
    serializer_class = AdopterAdoptionFormsSerializer


class RetrievePetAdoptionFormsAPIView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetAdoptionFormsSerializer
