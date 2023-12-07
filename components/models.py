import csv

from django.db import models

# Create your models here.
class Component:
    def __init__(self, Material, StorageLocation, UserName, TimeOfEntry, MaterialDocument, PostingDate, Quantity,
                 UnitOfEntry, Amount, MaterialDescription, EntryDate, Supplier):
        self.Material = Material
        self.StorageLocation = StorageLocation
        self.Username = UserName
        self.TimeOfEntry = TimeOfEntry
        self.MaterialDocument = MaterialDocument
        self.PostingDate = PostingDate
        self.Quantity = Quantity
        self.UnitofEntry = UnitOfEntry
        self.Amount = Amount
        self.MaterialDescription = MaterialDescription
        self.EntryDate = EntryDate
        self.Supplier = Supplier



components = []

def get_all():
    return components.copy()

with open('components.csv', encoding='utf-8') as input_file:
    input_file.readline()
    reader = csv.reader('input_file', delimiter = ';', quoting= csv.QUOTE_NONNUMERIC)
    for row in reader:
        components.append(components(*row))
