from django.test import TestCase
from django.urls import reverse


class TaxiSearchTest(TestCase):
    def test_search_driver(self):
        response = self.client.get(reverse("taxi:driver-list"), {"username": "adm"})
        self.assertEqual(response.status_code, 200)


    def test_search_car(self):
        response = self.client.get(reverse("taxi:car-list"), {"model": "tes"})
        self.assertEqual(response.status_code, 200)


    def test_search_manufacturer(self):
        response = self.client.get(reverse("taxi:manufacturer-list"), {"name": "bm"})
        self.assertEqual(response.status_code, 200)
