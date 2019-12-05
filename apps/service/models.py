# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Belongings(models.Model):
    services = models.ForeignKey('Services', models.DO_NOTHING)
    things = models.ForeignKey('Things', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'belongings'

class Details(models.Model):
    description = models.TextField()
    task = models.ForeignKey('Task', models.DO_NOTHING)
    services = models.ForeignKey('Services', models.DO_NOTHING)
    mechanics = models.ForeignKey('Mechanics', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'details'


class MechanicsHasSkills(models.Model):
    mechanics = models.ForeignKey(Mechanics, models.DO_NOTHING)
    skills_idskils = models.ForeignKey('Skills', models.DO_NOTHING, db_column='skills_idskils')

    class Meta:
        managed = False
        db_table = 'mechanics_has_skills'

class Refvehicle(models.Model):
    brand = models.CharField(max_length=45)
    model = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'refvehicle'


class Services(models.Model):
    indate = models.DateTimeField(db_column='inDate')  # Field name made lowercase.
    outdate = models.DateTimeField(db_column='outDate')  # Field name made lowercase.
    vehicles = models.ForeignKey('Vehicles', models.DO_NOTHING)
    receptionist = models.ForeignKey(Receptionist, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'services'


class Skills(models.Model):
    idskils = models.AutoField(primary_key=True)
    skill = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'skills'


class Task(models.Model):
    task = models.CharField(max_length=100)
    estimatedtime = models.CharField(db_column='estimatedTime', max_length=45)  # Field name made lowercase.
    tag = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'task'


class Tasksbyref(models.Model):
    price = models.FloatField()
    tdescription = models.TextField()
    refvehicle = models.ForeignKey(Refvehicle, models.DO_NOTHING)
    task = models.ForeignKey(Task, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tasksbyref'


class Things(models.Model):
    item = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'things'


class Vehicles(models.Model):
    licenseplate = models.CharField(db_column='licensePlate', max_length=10)  # Field name made lowercase.
    refvehicle = models.ForeignKey(Refvehicle, models.DO_NOTHING)
    customers = models.ForeignKey(Customers, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'vehicles'
