from django.db import models


class Patient(models.Model):
    GENDER_MALE = 'M'
    GENDER_FEMALE = 'F'
    GENDER_CHOICES = [
        (GENDER_MALE, 'Male'),
        (GENDER_MALE, 'Female'),
    ]

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)
    date_of_birth = models.DateField(null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)


class Hospital(models.Model):
    name = models.CharField(max_length=255)
    total_beds = models.PositiveSmallIntegerField()
    contact = models.CharField(max_length=255)


class OPD(models.Model):
    department_name = models.CharField(max_length=255)
    hospital = models.ManyToManyField(Hospital, on_delete=models.CASCADE)


class Doctor(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    speciality = models.CharField(max_length=40)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    department = models.ForeignKey(OPD, on_delete=models.PROTECT)
