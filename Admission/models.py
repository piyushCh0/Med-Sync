from django.db import models

# Create your models here.


class Admission(models.Model):
    admission_date = models.DateField(auto_now_add=True)
    discharge_date = models.DateField(auto_now_add=True, null=True)


class Bed(models.Model):
    BED_ICU = 'ICU'
    BED_GENERAL_WARD = 'GW'
    BED_PRIVATE = 'P'
    BED_CHOICES = [
        (BED_ICU, 'Intensive Care Unit'),
        (BED_GENERAL_WARD, 'General Ward'),
        (BED_PRIVATE, 'Private')
    ]

    bed_number = models.CharField(max_length=3)
    room_number = models.CharField(max_length=6)
    is_occupied = models.BooleanField()
    bed_type = models.CharField(
        max_length=3, choices=BED_CHOICES, default=BED_GENERAL_WARD)
