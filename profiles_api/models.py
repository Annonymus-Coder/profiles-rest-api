from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager

class UserProfileManager(BaseUserManager):
    """Managet for user profiles"""
    def createUser(self,email,name,password=None):
        """Create new User profile"""
        if not email:
            raise ValueError("User must have an email adress")

        email = self.normalize_email(email)

        user = self.model(email=email ,name=name)
        

        user.setPassword(password)
        user.save(using=self.db)

        return user


    def createSuperuser(self,name,email,password):
        """Create superuser with given details""" 

        user = self.createUser(email,name,password)

        user.is_staff = True   
        user.save(using=self.db)

        return user



class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255,unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_fullname(self):
        """Retreive Full name of user"""
        return self.name

    def get_shortname(self):
        """Retreive short name"""
        return self.name
    
    def __str__(self):
        """String format of model"""
        return self.email