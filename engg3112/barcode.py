import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'engg3112.settings')
django.setup()

import cv2, time, requests
from pyzbar.pyzbar import decode
from expiryfinder import get_product_details
from pantry.models import FoodItem
import pygame
import time
from datetime import date, timedelta

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("success.mp3")

def two_weeks_from_now():
    """Return a date two weeks from today."""
    return date.today() + timedelta(weeks=2)

def create_food_item(name, amount, quantity):
    """
    Create a new FoodItem or update the quantity if it already exists.
    
    Args:
        name (str): The name of the food item.
        amount (str): The amount with units (e.g., "160g").
        quantity (int): The number of items to add.
        
    Returns:
        FoodItem: The saved FoodItem instance.
    """
    # Attempt to get the existing food item by name and amount
    food_item, created = FoodItem.objects.get_or_create(
        name=name,
        amount=amount,
        defaults={
            'quantity': quantity,
            'expiry_date': two_weeks_from_now()
        }
    )

    # If the item already exists, increment the quantity
    if not created:
        food_item.quantity += quantity
        food_item.save()
    
    return food_item

# capture webcam 
cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, frame = cap.read()
    # flip the image like mirror image 
    frame  = cv2.flip(frame,1)
    detectedBarcode = decode(frame)
    if not detectedBarcode:
        print("No Barcodes Detected")
    else:
        for barcode in detectedBarcode:
            if barcode.data != "":
                print(get_product_details(barcode.data))
                name, qty, expiry_date = get_product_details(barcode.data)
                create_food_item(name, qty, 1)
                cv2.putText(frame,str(barcode.data),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,255),2)
                pygame.mixer.music.play()
                time.sleep(2)

    cv2.imshow('scanner' , frame)
    if cv2.waitKey(1) == ord('q'):
        break


