from django.test import TestCase, Client
from django.urls import reverse
from django.shortcuts import redirect
from delights_app.models import *
from datetime import datetime
import json

 
class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.purchase_url = reverse('purchasecreate', args = [1])
        self.item1 = MenuItem.objects.create(
            name = 'menuitem1',
            price = 2.0
        )
        self.purchase1 = Purchase.objects.create(
            menu_item = self.item1,
            timestamp = datetime.now()
        )
        

    def test_PurchaseCreate(self):
        
        response = self.client.post(self.purchase_url)
        self.assertEquals(response.status_code, 302)
        self.assertEquals(self.purchase1.menu_item.name, 'menuitem1') 
        