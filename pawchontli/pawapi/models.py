from django.db import models
from versatileimagefield.fields import VersatileImageField, PPOIField

## Types of relations
# Association --> Pet : 1 to N
# Association --> Address : 1 to 1
# Adopter     --> Address : 1 to 1
# Adopter     --> AdoptionForm : 1 to N

# Create your models here.


class Association(models.Model) :
  """ Association Model """
  email = models.EmailField(unique=True)
  name = models.CharField(max_length=255)
  first_name_contact = models.CharField(max_length=255)
  last_name_contact = models.CharField(max_length=255)
  phone = models.CharField(max_length=20, unique=True)
  donation_link = models.CharField(max_length=255)
  web_address = models.CharField(max_length=255)
  state = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  zip_code = models.CharField(max_length=20)
  neighbourhood = models.CharField(max_length=50)
  street_and_number = models.CharField(max_length=20)
  story = models.TextField(max_length=1000)
  image = models.ImageField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)



  def __str__(self) :
    return f'{self.name}. Contact:{self.first_name_contact} {self.last_name_contact} at {self.email_contact}'

class Adopter(models.Model) :
  """ Adopter Model """
  email = models.EmailField(unique=True)
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  birthdate = models.DateField()
  phone = models.CharField(max_length=20)
  state = models.CharField(max_length=50)
  city = models.CharField(max_length=50)
  zip_code = models.CharField(max_length=20)
  neighbourhood = models.CharField(max_length=50)
  street_and_number = models.CharField(max_length=20)
  story= models.TextField(max_length=2000)
  image = models.ImageField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  #Relation



  def __str__(self) :
    return f'{self.first_name} {self.last_name}'

class Pet(models.Model) :
  name = models.CharField(max_length=255)

  PET_SPECIES = (
    ('cat', 'Cat'),
    ('dog', 'Dog'),
  )
  species = models.CharField(max_length=50, choices=PET_SPECIES, default='dog')
  age = models.CharField(max_length=40)
  
  # The declaration of these variables is for human readability purposes 
  MALE = 'M'
  FEMALE = 'F'
  PET_GENDER = (
    (MALE, 'Male'),
    (FEMALE, 'Female'),
  )
  gender = models.CharField(max_length=10, choices=PET_GENDER, default=FEMALE)

  SMALL = 'S'
  MEDIUM = 'M'
  LARGE = 'L'
  PET_SIZE = (
    (SMALL, 'Small'),
    (MEDIUM, 'Medium'),
    (LARGE, 'Large'),
  )
  size = models.CharField(max_length=50, choices=PET_SIZE, default=SMALL)

  PLAYFUL = 'P'
  SHY = 'S'
  INDEPENDENT = 'I'
  FRIENDLY = 'F'
  NAUGHTY = 'N'
  LAZY = 'L'
  PET_CHARACTER = (
    (PLAYFUL, 'Playful'),
    (SHY, 'Shy'),
    (INDEPENDENT, 'Independent'),
    (FRIENDLY, 'Friendly'),
    (NAUGHTY, 'Naughty'),
    (LAZY, 'Lazy'),
  )
  character = models.CharField(max_length=30, choices=PET_CHARACTER, default=PLAYFUL)
  story = models.TextField(max_length=1000)
  special_needs = models.TextField(max_length=1000)
  image = models.ImageField(null=True, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)

  # Relations
  association = models.ForeignKey(Association, on_delete=models.PROTECT, related_name='pets')


  def __str__(self) :
    return f'{self.name}, {self.character} {self.size} {self.gender} {self.species}'

class AdoptionForm (models.Model) :
  amount_pets_today = models.CharField(max_length=10)
  which_pets_today = models.CharField(max_length=255)
  amount_pets_past = models.CharField(max_length=10)
  story_pets_past = models.TextField(max_length=1000)
  everyone_agrees = models.BooleanField(default=False)
  allowed_to_own = models.BooleanField(default=False)
  if_change_address = models.TextField(max_length=1000)
  average_age = models.CharField(max_length=255)
  place_of_sleep = models.TextField(max_length=1000)
  time_by_itself = models.TextField(max_length=1000)
  petcare_awareness = models.TextField(max_length=1000)
  pet_responsable = models.TextField(max_length=1000)
  veterinarian = models.TextField(max_length=500)
  created_at = models.DateTimeField(auto_now_add=True)

  # Relations
  adopter = models.ForeignKey(Adopter, on_delete=models.CASCADE, related_name='adoption_forms')
  pet= models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='adoption_pets')
  def __str__(self) :
    return f'Adoption Form created at {self.created_at}'
