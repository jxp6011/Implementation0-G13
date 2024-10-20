from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters
from django.core.validators import MinValueValidator

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(
        max_length=15, 
        unique=True, 
        null=True,
        validators=[validate_no_special_characters],
        # error_message={"unique": ""}
    )
    whatsapp_id = models.CharField(
        max_length=20, 
        null=True,
        validators=[validate_no_special_characters],
        )
    address = models.CharField(
        max_length=50, 
        null=True,
        validators=[validate_no_special_characters],
        )
    
    profile_pic = models.ImageField(default='default_profile_pic.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return self.email




class Post(models.Model):
    title = models.CharField(max_length=60)

    item_price = models.IntegerField(validators=[MinValueValidator(1)])

    CONDITION_CHOICES = [
        ('New', 'New'),
        ('Very Good', 'Very Good'),
        ('Good', 'Good'),
        ('Fine', 'Fine'),
        ('Bad', 'Bad'),
    ]
    item_condition = models.CharField(max_length=10, choices=CONDITION_CHOICES, default=None)

    item_details = models.TextField(blank=True)

    image1 = models.ImageField(upload_to='item_pics')

    image2 = models.ImageField(upload_to='item_pics', blank=True)

    image3 = models.ImageField(upload_to='item_pics', blank=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    dt_created = models.DateTimeField(auto_now_add=True)

    dt_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    is_sold = models.BooleanField(default=False)




