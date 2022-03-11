from ast import operator
from tkinter import CASCADE
from django.db import models
from django.utils import timezone
#00 - admin
#01 - pcp
#02 - patient
#03 - etc
#1xx - device
import uuid


# Create your models here.
class UserManager(models.Manager):

    def create_user(self, role):
        user = self.create(role=role)
        return user


class User(models.Model):

    objects = UserManager()

    ROLES = (
        ('0', 'ADMIN'),
        ('1', 'PCP'),
        ('2', 'Patient'),
        ('3', 'Other'),
    )

    role = models.CharField(max_length=1, choices=ROLES, default='3')

    id = models.UUIDField('UID',
                          primary_key=True,
                          default=uuid.uuid4,
                          editable=False)

    firstName = models.CharField(max_length=30)
    lastName = models.CharField(max_length=30)
    birthDate = models.CharField(max_length=10)
    address = models.CharField(max_length=60)
    phoneNumber = models.CharField(max_length=10)
    #photoID = models.ImageField()
    ## Insert "cyclical support": https://stackoverflow.com/questions/8466726/django-circular-model-reference

    SEXES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    sex = models.CharField(max_length=1, choices=SEXES)

    def __str__(self):
        return self.firstName + ' ' + self.lastName


class Device(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE, default=uuid.uuid4)
    did = models.UUIDField('DID',
                           primary_key=True,
                           default=uuid.uuid4,
                           editable=False)
    deviceSKU = models.CharField(max_length=30)
    modelNum = models.CharField(max_length=30)
    serialNum = models.CharField(max_length=30)
    isAssigned = models.BooleanField(default=False)

    def __str__(self):
        return self.deviceSKU + ':' + self.uid


class MedHistory(models.Model):
    uid = models.OneToOneField(User,
                               on_delete=models.CASCADE,
                               default=uuid.uuid4)

    def __str__(self):
        return self.uid


class Allergies(models.Model):
    medhistory = models.ForeignKey(MedHistory,
                                   on_delete=models.CASCADE,
                                   default=uuid.uuid4)
    allergy = models.CharField(max_length=30)
    SEVERITIES = (
        ('1', 'MILD'),
        ('2', 'SERIOUS'),
        ('3', 'URGENT'),
    )
    severity = models.CharField(max_length=1, choices=SEVERITIES)

    def __str__(self):
        return self.allergy + ' ' + 'Severity: ' + self.severity


class Medications(models.Model):
    medhistory = models.ForeignKey(MedHistory,
                                   related_name='medications',
                                   on_delete=models.CASCADE,
                                   default=uuid.uuid4)
    medId = models.UUIDField('DID',
                             primary_key=True,
                             default=uuid.uuid4,
                             editable=False)
    isValid = models.BooleanField(default=False)
    prescribedBy = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.medId + ' ' + 'Prescriber: ' + self.prescribedBy


class Operation(models.Model):
    medhistory = models.ForeignKey(MedHistory,
                                   related_name='operations',
                                   on_delete=models.CASCADE,
                                   default=uuid.uuid4)
    performedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    OPERATIONS = (
        ('1', 'SURGICAL'),
        ('2', 'PHYSICAL EXAM'),
        ('3', 'SCAN'),
        ('4', 'THERAPY'),
        ('5', 'REHABILITATION'),
    )
    type = models.CharField(max_length=1, choices=OPERATIONS)

    def __str__(self):
        return 'Operation Type: ' + self.type + ' ' + 'Performed By: ' + self.performedBy


class Measurements(models.Model):
    medhistory = models.ForeignKey(MedHistory,
                                   related_name='measurements',
                                   on_delete=models.CASCADE,
                                   default=uuid.uuid4)
    uid = models.OneToOneField(User,
                               on_delete=models.CASCADE,
                               default=uuid.uuid4)
    did = models.ForeignKey(Device,
                            on_delete=models.CASCADE,
                            default=uuid.uuid4)
    time = models.DateTimeField(default=timezone.now)


class Measurement(models.Model):
    measurements = models.ForeignKey(Measurements,
                                     related_name='measurement',
                                     on_delete=models.CASCADE,
                                     default=uuid.uuid4)
    height = models.CharField(max_length=30)
    weight = models.CharField(max_length=30)
    BMI = models.CharField(max_length=30)
    bloodPressure = models.CharField(max_length=30)
    bloodO2 = models.CharField(max_length=30)
    heartRate = models.CharField(max_length=30)
    temperature = models.CharField(max_length=30)
