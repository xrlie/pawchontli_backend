from django.db import models
from django.contrib.auth.models import User
from versatileimagefield.fields import VersatileImageField, PPOIField

## Types of relations
# Association --> Pet : 1 to N
# Association --> Address : 1 to 1
# Adopter     --> Address : 1 to 1
# Adopter     --> AdoptionForm : 1 to N

# Create your models here.


class Association(models.Model) :
  """ Association Model """
  user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name='associations')
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
    return f'{self.user.username}. Contact:{self.first_name_contact} {self.last_name_contact}'

class Adopter(models.Model) :
  """ Adopter Model """
  user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE, related_name='adopters')
  phone = models.CharField(max_length=20, null=True)
  state = models.CharField(max_length=50, null=True)
  city = models.CharField(max_length=50, null=True)
  zip_code = models.CharField(max_length=20, null=True)
  neighbourhood = models.CharField(max_length=50, null=True)
  street_and_number = models.CharField(max_length=20, null=True)
  # story= models.TextField(max_length=2000)
  image = models.ImageField(null=True, blank=True)
 
  def __str__(self) :
    return f'{self.user.username}'

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
  STATUS_FORM = (
    ('Pending','Pending'),
    ('Approved','Approved'),
    ('Rejected','Rejected'),
  )
  status = models.CharField(max_length=50, choices=STATUS_FORM, default='Pending')

  # Relations
  adopter = models.ForeignKey(Adopter, on_delete=models.CASCADE, related_name='adoption_forms')
  pet= models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='adoption_pets')
  def __str__(self) :
    return f'Adoption Form created at {self.created_at}'
