from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class Admission(models.Model):
    admission_date = models.DateField(auto_now_add=True)
    discharge_date = models.DateField(auto_now_add=True, null=True)
    # patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    # doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    # hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


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
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
