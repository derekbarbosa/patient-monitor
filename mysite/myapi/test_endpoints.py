from cgitb import reset
from django.test import TestCase
import requests

class GetTestCase(TestCase):

    def test_get_root(self):
        r = requests.get("http://54.175.53.184:8000/")
        assert r.ok
    def test_get_users(self):
        r = requests.get("http://54.175.53.184:8000/users")
        assert r.ok
    def test_get_devices(self):
        r = requests.get("http://54.175.53.184:8000/device")
        assert r.ok
    def test_get_medhistory(self):
        r = requests.get("http://54.175.53.184:8000/medhistory")
        assert r.ok
    def test_get_allergies(self):
        r = requests.get("http://54.175.53.184:8000/allergies")
        assert r.ok
    def test_get_medications(self):
        r = requests.get("http://54.175.53.184:8000/medications")
        assert r.ok
    def test_get_operations(self):
        r = requests.get("http://54.175.53.184:8000/operation")
        assert r.ok
    def test_get_measurements(self):
        r1 = requests.get("http://54.175.53.184:8000/measurements")
        r2 = requests.get("http://54.175.53.184:8000/measurement")
        assert r1.ok
        assert r2.ok