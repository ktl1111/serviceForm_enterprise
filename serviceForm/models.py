import datetime

from django.db import models


# Create your models here.
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.


class Area(models.Model):
    areaid = models.AutoField(db_column='AREAID', primary_key=True)  # Field name made lowercase.
    areaname = models.CharField(db_column='AREANAME', max_length=10)  # Field name made lowercase.

    def __str__(self):
        return self.areaname

    class Meta:
        # managed = False
        db_table = 'AREA'


class Category(models.Model):
    categoryid = models.AutoField(db_column='CATEGORYID', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CATEGORYNAME', max_length=10)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='ENABLED', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.categoryname

    class Meta:
        # managed = False
        db_table = 'CATEGORY'

class MachineName(models.Model):
    machinenameid = models.IntegerField(db_column='MACHINENAMEID', primary_key=True)  # Field name made lowercase.
    machinename = models.CharField(db_column='MACHINENAME', max_length=10)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='ENABLED', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.machinename

    class Meta:
        # managed = False
        db_table = 'MACHINENAME'


class ContractType(models.Model):
    contractid = models.AutoField(db_column='CONTRACTID', primary_key=True)  # Field name made lowercase.
    contractname = models.CharField(db_column='CONTRACTNAME', max_length=10)  # Field name made lowercase.

    def __str__(self):
        return self.contractname

    class Meta:
        # managed = False
        db_table = 'CONTRACT_TYPE'


class Factory(models.Model):
    facid = models.CharField(db_column='FACID', primary_key=True, max_length=10)  # Field name made lowercase.
    facname = models.CharField(db_column='FACNAME', max_length=10)  # Field name made lowercase.

    def __str__(self):
        return self.facid

    class Meta:
        # managed = False
        db_table = 'FACTORY'


class Hospital(models.Model):
    hospitalid = models.IntegerField(db_column='HOSPITALID', primary_key=True)  # Field name made lowercase.
    hospitalname = models.CharField(db_column='HOSPITALNAME', max_length=50)  # Field name made lowercase.
    hospitalnameabbr = models.CharField(db_column='HOSPITALNAMEABBR', max_length=10)  # Field name made lowercase.
    areaid = models.IntegerField(db_column='AREAID')  # Field name made lowercase.
    cityarea = models.CharField(db_column='CITYAREA', max_length=10, blank=True,
                                null=True)  # Field name made lowercase.
    addr = models.CharField(db_column='ADDR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zcode = models.IntegerField(db_column='ZCODE', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='ENABLED', blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.hospitalname

    class Meta:
        # managed = False
        db_table = 'HOSPITAL'


class Machine(models.Model):
    machineid = models.IntegerField(db_column='MACHINEID', primary_key=True)  # Field name made lowercase.
    machinename = models.CharField(db_column='MACHINENAME', max_length=50)  # Field name made lowercase.
    hospitalid = models.IntegerField(db_column='HOSPITALID')  # Field name made lowercase.

    def __str__(self):
        return str(self.machineid)

    class Meta:
        # managed = False
        db_table = 'MACHINE'


class Parts(models.Model):
    partsid = models.CharField(db_column='PARTSID', max_length=50, primary_key=True)  # Field name made lowercase.
    partsgpname = models.CharField(db_column='PARTSGPNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    facid = models.CharField(db_column='FACID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    partsname = models.CharField(db_column='PARTSNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.partsgpname

    class Meta:
        # managed = False
        db_table = 'PARTS'


class ServiceSheet(models.Model):
    sheetid = models.IntegerField(db_column='SHEETID')  # Field name made lowercase.
    empid = models.IntegerField(db_column='EMPID')  # Field name made lowercase.
    areaid = models.IntegerField(db_column='AREAID')  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='CATEGORYID')  # Field name made lowercase.
    stateid = models.IntegerField(db_column='STATEID')  # Field name made lowercase.
    date = models.DateField(db_column='DATE')  # Field name made lowercase.
    machinestop = models.BooleanField(db_column='MACHINESTOP')  # Field name made lowercase.
    hospitalid = models.IntegerField(db_column='HOSPITALID')  # Field name made lowercase.
    receiver = models.CharField(db_column='RECEIVER', max_length=10)  # Field name made lowercase.
    mensent = models.CharField(db_column='MENSENT', max_length=10)  # Field name made lowercase.
    contractid = models.IntegerField(db_column='CONTRACTID')  # Field name made lowercase.
    machinename = models.CharField(db_column='MACHINENAME', max_length=50)  # Field name made lowercase.
    machineid = models.CharField(db_column='MACHINEID', max_length=10)  # Field name made lowercase.
    callcont = models.CharField(db_column='CALLCONT', max_length=50)  # Field name made lowercase.
    brokenitems = models.CharField(db_column='BROKENITEMS', max_length=50)  # Field name made lowercase.
    partsid = models.IntegerField(db_column='PARTSID')  # Field name made lowercase.
    calltime = models.TimeField(db_column='CALLTIME')  # Field name made lowercase.
    arrivetime = models.TimeField(db_column='ARRIVETIME')  # Field name made lowercase.
    fixingtime = models.TimeField(db_column='FIXINGTIME')  # Field name made lowercase.
    repairtime = models.TimeField(db_column='REPAIRTIME')  # Field name made lowercase.
    repairdur = models.FloatField(db_column='REPAIRDUR')  # Field name made lowercase.
    machinestpdur = models.FloatField(db_column='MACHINESTPDUR')  # Field name made lowercase.
    repaircont = models.TextField(db_column='REPAIRCONT')  # Field name made lowercase.
    note = models.TextField(db_column='NOTE')  # Field name made lowercase.

    class Meta:
        # managed = False
        db_table = 'SERVICE_SHEET'


class WorkState(models.Model):
    stateid = models.AutoField(db_column='STATEID', primary_key=True)  # Field name made lowercase.
    statename = models.CharField(db_column='STATENAME', max_length=10)  # Field name made lowercase.

    def __str__(self):
        return self.statename

    class Meta:
        # managed = False
        db_table = 'STATE'


class T023T(models.Model):
    matkl = models.IntegerField(db_column='MATKL', blank=True, null=True)  # Field name made lowercase.
    wgbez = models.CharField(db_column='WGBEZ', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.wgbez

    class Meta:
        # managed = False
        db_table = 'T023T'
