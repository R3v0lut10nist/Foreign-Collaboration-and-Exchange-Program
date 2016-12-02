from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email,first_name,last_name,address,mobilenumber,is_college,subject,programme, password=None,nationality=''):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            address=address,
            mobilenumber=mobilenumber,
            nationality=nationality,
            subject=subject,
            programme=programme,
            
        )
        user.is_college=is_college
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,first_name,address,mobilenumber, password,subject='CSE',programme='Btech',nationality='',last_name='',is_college=False):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            address=address,
            mobilenumber=mobilenumber,
            password=password,
            nationality=nationality,
            is_college=is_college,
            subject=subject,
            programme=programme
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    CSE = "CS"
    Trical = "EE"
    Tronics = "EC"
    Mech = "MC"
    Chem = "CE"
    Civil = "CV"
    Biochem="BM"
    Pharma="PH"
    Math="MT"
    Subject_choices = (
        (CSE, 'CS'),
        (Trical, 'EE'),
        (Tronics, 'EC'),
        (Mech, 'MC'),
        (Chem, 'CE'),
        (Civil, 'CV'),
        (Biochem,'BM'),
        (Pharma,'PH'),
        (Math,"MT"),

    )
    Btech='Btech'
    Mtech='Mtech'
    Phd='Phd'
    Programme_choices=((Btech,'Btech'),(Mtech,'Mtech'),(Phd,'Phd'))
    programme=models.CharField(max_length=5,choices=Programme_choices,default=Btech)
    subject = models.CharField(max_length=2, choices=Subject_choices, default=CSE)
    #/date_of_birth = models.DateField(blank=True,)
    #mobilenumber = RegexValidator(regex=r'^\d{10}$', message="Phone number must be entered in the format: '999999999'. 10 digits allowed.")
    phone_regex = RegexValidator(regex=r'^\d{10}$', message="Phone number must be entered in the format: '999999999'. 10 digits allowed.")
    mobilenumber = models.CharField(max_length=10,validators=[phone_regex],blank=False)
    #mobilenumber=models.IntegerField(unique=True,default=None)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    address=models.TextField(default=None)
    first_name=models.CharField(max_length=20,default=None)
    last_name=models.CharField(max_length=10,default=None)
    nationality=models.CharField(max_length=20,default=None,blank=True,null=True)
    is_college=models.BooleanField(default=False)
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['mobilenumber','first_name','address','nationality','last_name']

    def get_full_name(self):
        # The user is identified by their email address
        return self.first_name+self.last_name

    def get_short_name(self):
        # The user is identified by their email address
        return self.first_name

    def __str__(self):              # __unicode__ on Python 2
        return self.first_name+self.last_name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

    @property
    def is_a_college(self):
        return self.is_college    