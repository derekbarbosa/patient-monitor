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

    firstName = models.CharField(max_length=30, )
    lastName = models.CharField(max_length=30, )
    birthDate = models.CharField(max_length=10, )
    address = models.CharField(max_length=60, )
    phoneNumber = models.CharField(max_length=10, )
    #photoID = models.ImageField()
    ## Insert "cyclical support": https://stackoverflow.com/questions/8466726/django-circular-model-reference

    SEXES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    )

    sex = models.CharField(max_length=1, choices=SEXES, default='O')

    def __str__(self):
        return self.firstName + ' ' + self.lastName


class Device(models.Model):
    uid = models.ForeignKey(User,
                            on_delete=models.CASCADE,
                            related_name="device",
                            default=None,
                            null=True)
    did = models.UUIDField('DID',
                           primary_key=True,
                           default=uuid.uuid4,
                           editable=False)
    deviceSKU = models.CharField(max_length=30)
    modelNum = models.CharField(max_length=30)
    serialNum = models.CharField(max_length=30)
    isAssigned = models.BooleanField(default=False)

    def __str__(self):
        return str(self.deviceSKU + ':' + str(self.uid))


class MedHistory(models.Model):
    uid = models.OneToOneField(User,
                               on_delete=models.CASCADE,
                               related_name="medHistory",
                               default=None,
                               null=True)

    def __str__(self):
        return str(self.uid)


class Allergies(models.Model):
    medhistory = models.ForeignKey(MedHistory,
                                   on_delete=models.CASCADE,
                                   related_name="allergies",
                                   default=None,
                                   null=True)
    allergy = models.CharField(max_length=30, default="None")
    SEVERITIES = (
        ('1', 'MILD'),
        ('2', 'SERIOUS'),
        ('3', 'URGENT'),
    )
    severity = models.CharField(max_length=1, choices=SEVERITIES, default='1')

    def __str__(self):
        return str(self.allergy + ' ' + 'Severity: ' + self.severity)


class Medications(models.Model):
    medhistory = models.ForeignKey(MedHistory,
                                   related_name='medications',
                                   on_delete=models.CASCADE,
                                   default=None,
                                   null=True)
    medId = models.UUIDField('medID',
                             primary_key=True,
                             default=uuid.uuid4,
                             editable=True)
    isValid = models.BooleanField(default=False)
    prescribedBy = models.ForeignKey(User,
                                     related_name="prescriber",
                                     on_delete=models.CASCADE,
                                     default=None,
                                     null=True)

    def __str__(self):
        return str(
            str(self.medId) + ' ' + 'Prescriber: ' + str(self.prescribedBy))


class Operation(models.Model):
    medhistory = models.ForeignKey(MedHistory,
                                   related_name='operations',
                                   on_delete=models.CASCADE,
                                   default=None,
                                   null=True)
    performedBy = models.ForeignKey(User,
                                    on_delete=models.CASCADE,
                                    default=None,
                                    null=True)
    OPERATIONS = (
        ('1', 'SURGICAL'),
        ('2', 'PHYSICAL EXAM'),
        ('3', 'SCAN'),
        ('4', 'THERAPY'),
        ('5', 'REHABILITATION'),
    )
    type = models.CharField(max_length=1, choices=OPERATIONS, default="5")

    def __str__(self):
        return str('Operation Type: ' + self.type + ' ' + 'Performed By: ' +
                   str(self.performedBy))


class Measurements(models.Model):
    medhistory = models.ForeignKey(MedHistory,
                                   related_name='measurements',
                                   on_delete=models.CASCADE,
                                   default=None,
                                   null=True)
    uid = models.OneToOneField(User,
                               on_delete=models.CASCADE,
                               default=None,
                               null=True)
    did = models.ForeignKey(Device,
                            on_delete=models.CASCADE,
                            default=None,
                            null=True)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(
            str(self.medhistory) + ' ' + str(self.uid) + ' ' + str(self.time))


class Measurement(models.Model):
    measurements = models.ForeignKey(Measurements,
                                     related_name='measurement',
                                     on_delete=models.CASCADE,
                                     default=None,
                                     null=True)
    height = models.CharField(max_length=30, default="0cm")
    weight = models.CharField(max_length=30, default="0kg")
    BMI = models.CharField(max_length=30, default="0")
    bloodPressure = models.CharField(max_length=30, default="0")
    bloodO2 = models.CharField(max_length=30, default="0")
    heartRate = models.CharField(max_length=30, default="0")
    temperature = models.CharField(max_length=30, default="0")

    def __str__(self):
        return str(
            str(self.measurements) + ' ' + self.height + ' ' + self.weight)
