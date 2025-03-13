from django.db import models
#if value is text and number = charfield

# Create your models here.
class Patient(models.Model):
  fullname = models.CharField(max_length=100)
  age = models.IntegerField()
  email = models.EmailField()
  message = models.TextField()

  def __str__(self):
    return self.fullname

class Doctor(models.Model):
  fullname = models.CharField(max_length=100)
  age = models.IntegerField()
  email = models.EmailField()
  department = models.CharField(max_length=100)
  status = models.CharField(max_length=100)
  qualification = models.CharField(max_length=100)
  def __str__(self):
    return self.fullname

class staff(models.Model):
  firstname = models.CharField(max_length=100)
  lastname = models.CharField(max_length=100)
  position = models.CharField(max_length=100)
  email = models.EmailField()
  phonenumber = models.CharField(max_length=100)
  hiredate = models.DateField()
  def __str__(self):
    return self.firstname

class ward(models.Model):
  name = models.CharField(max_length=100)
  totalbeds = models.IntegerField()
  availablebeds = models.IntegerField()
  def __str__(self):
    return self.name


class appointment(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  phone = models.CharField(max_length=10)
  date = models.DateField()
  department = models.CharField(max_length=100)
  doctor = models.CharField(max_length=100)
  message = models.TextField()
  def __str__(self):
    return self.name

class Transaction(models.Model):
    phone_number = models.CharField(max_length=15)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    status = models.CharField(max_length=20, choices=[('Success', 'Success'), ('Failed', 'Failed')])
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
      return f"{self.phone_number} - {self.amount} - {self.status}"

class cont(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField()
  subject = models.CharField(max_length=100)
  message = models.TextField()
  def __str__(self):
    return self.name
