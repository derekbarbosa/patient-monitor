from django.db import models
#00 - admin
#01 - pcp
#02 - patient
#03 - etc
#1xx - device
import uuid

# Create your models here.
class UserManager(models.Manager):
    def create_user(self,role):
        user = self.create(role=role)
        return user

class User(models.Model):
    objects = UserManager()
    role = ""
    id = models.UUIDField(
        'UID',
        primary_key = True,
        default = uuid.uuid4,
        editable = False
        )

    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    birthDate = models.CharField(max_length=10)
    address = models.CharField(max_length=60)
    phoneNumber = models.CharField(max_length=10)
    #photoID = models.ImageField()
    ## Insert "cyclical support": https://stackoverflow.com/questions/8466726/django-circular-model-reference

    SEXES = (
        ('M', 'Male'),
        ('F', 'Female')
    )
    sex = models.CharField(max_length=1, choices=SEXES)

    def __str__(self):
        return self.firstName + ' ' + self.lastName

class Device(models.Model):
    id = models.UUIDField(
        'DID',
        primary_key = True,
        default = uuid.uuid4,
        editable = False
    )

    deviceSKU = models.CharField(max_length=30)
    modelNum = models.CharField(max_length=30)
    serialNum = models.CharField(max_length=30)
    isAssigned = models.BooleanField(default=False)
   
    def __str__(self):
        return self.deviceSKU + ':' + self.id


