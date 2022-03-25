from email.policy import default
from django.test import TestCase
from myapi.models import User, Device, MedHistory, Allergies, Medications, Operation, Measurement, Measurements


# Create your tests here.
class UserTestCase(TestCase):

    def setUp(self):
        # Create two objects, one with default ALL, one with specified last/first/address
        User.objects.create(firstName="d", lastName="b", birthDate='9/21/99')
        User.objects.create(firstName="Johnny")

    def test_user_creation(self):
        definedUser = User.objects.get(firstName="d")
        defaultUser = User.objects.get(firstName="Johnny")
        self.assertEqual(definedUser.lastName, "b")


class DeviceTestCase(TestCase):

    def setUp(self):
        # Create two objects with different SKUs and test retrieval
        Device.objects.create(deviceSKU="theTester", modelNum="01")
        Device.objects.create(deviceSKU="HRMonitor", modelNum="3934")

    def test_device_creation(self):
        Device1 = Device.objects.get(deviceSKU="theTester")
        Device2 = Device.objects.get(deviceSKU="HRMonitor")
        self.assertEqual(Device1.modelNum, "01")
        self.assertEqual(Device2.modelNum, "3934")


class AllergiesTestCase(TestCase):

    def setUp(self):
        # Create two objects with different allergens/severity, and test retrieval
        Allergies.objects.create(allergy="Peanuts", severity='2')
        Allergies.objects.create()

    def test_allergy_creation(self):
        definedAllergy = Allergies.objects.get(allergy="Peanuts")
        defaultAllergy = Allergies.objects.get(allergy="None")
        self.assertEqual(definedAllergy.severity, "2")
        self.assertEqual(defaultAllergy.severity, "1")


class MedicationsTestCase(TestCase):

    def setUp(self):
        Medications.objects.create(isValid=True)
        Medications.objects.create()
        pass

    def test_medication_creation(self):
        definedMed = Medications.objects.get(isValid=True)
        defaultMed = Medications.objects.get(isValid=False)
        self.assertEqual(definedMed.isValid, True)
        self.assertEqual(defaultMed.isValid, False)
        pass


class OperationTestCase(TestCase):

    def setUp(self):
        Operation.objects.create(type="2")
        Operation.objects.create()
        pass

    def test_operation_creation(self):
        definedOp = Operation.objects.get(type="2")
        defaultOP = Operation.objects.get(type="5")
        self.assertEqual(definedOp.type, "2")
        self.assertEqual(defaultOP.type, "5")
        pass


class MeasurementTestCase(TestCase):

    def setUp(self):
        Measurement.objects.create(height="200cm", weight="90kg")
        Measurement.objects.create()
        pass

    def test_measurement_creation(self):
        definedMeasurement = Measurement.objects.get(height="200cm")
        defaultMeasurement = Measurement.objects.get(height="0cm")
        self.assertEqual(definedMeasurement.height, "200cm")
        self.assertEqual(defaultMeasurement.height, "0cm")
        pass