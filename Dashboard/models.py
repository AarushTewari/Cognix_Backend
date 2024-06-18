from django.db import models
import uuid
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

gender_choices = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others')
]
class UserProfile(models.Model):
    static_id = models.UUIDField(max_length=36, unique=True, default=uuid.uuid4, editable=False)
    auth_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name = 'app_user')
    # profile_pic = models.ImageField()
    name = models.CharField(max_length=30, null=True)
    weight = models.IntegerField()
    height = models.IntegerField()
    dateofbirth = models.DateField(null=True)
    age = models.IntegerField()
    phone = models.BigIntegerField(null=True, validators=[MinValueValidator(1000000000), MaxValueValidator(9999999999)])
    sex = models.CharField(max_length=30, choices=gender_choices, null=True)
    address = models.CharField(max_length=500, null = True)
    certificates = models.CharField(max_length=500, null = True)
    bio = models.CharField(max_length=500, null = True)
    is_instructor = models.BooleanField(default=False)
    #bank = models.ForeginKey(Bank, null = True)
    has_membership = models.BooleanField(default=False)
    

    
    
    # is_instructor = models.BooleanField(default=False)
    


chat_status = [
    ("Accepted", "Accepted"),
    ("Declined", "Declined"),
    ("Pending", "Pending")
]
class ChatRequest(models.Model):
    static_id = models.UUIDField(max_length=36, unique=True, default=uuid.uuid4, editable=False)
    sender = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="sender")
    reciever = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name="reciever")
    status = models.CharField(max_length=40, choices=chat_status, default="Pending")