# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Area(models.Model):
    areaid = models.AutoField(db_column='AREAID', primary_key=True)  # Field name made lowercase.
    areaname = models.CharField(db_column='AREANAME', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AREA'


class Category(models.Model):
    categoryid = models.AutoField(db_column='CATEGORYID', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CATEGORYNAME', max_length=10)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='ENABLED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CATEGORY'


class ContractType(models.Model):
    contractid = models.AutoField(db_column='CONTRACTID', primary_key=True)  # Field name made lowercase.
    contractname = models.CharField(db_column='CONTRACTNAME', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CONTRACT_TYPE'


class Factory(models.Model):
    facid = models.CharField(db_column='FACID', primary_key=True, max_length=10)  # Field name made lowercase.
    facname = models.CharField(db_column='FACNAME', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'FACTORY'


class Hospital(models.Model):
    hospitalid = models.AutoField(db_column='HOSPITALID', primary_key=True)  # Field name made lowercase.
    hospitalname = models.CharField(db_column='HOSPITALNAME', max_length=50)  # Field name made lowercase.
    hospitalnameabbr = models.CharField(db_column='HOSPITALNAMEABBR', max_length=10)  # Field name made lowercase.
    areaid = models.ForeignKey(Area, models.DO_NOTHING, db_column='AREAID')  # Field name made lowercase.
    cityarea = models.CharField(db_column='CITYAREA', max_length=10, blank=True, null=True)  # Field name made lowercase.
    addr = models.CharField(db_column='ADDR', max_length=50, blank=True, null=True)  # Field name made lowercase.
    zcode = models.IntegerField(db_column='ZCODE', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='ENABLED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HOSPITAL'


class Machine(models.Model):
    machineid = models.IntegerField(db_column='MACHINEID', primary_key=True)  # Field name made lowercase.
    machinename = models.CharField(db_column='MACHINENAME', max_length=50)  # Field name made lowercase.
    hospitalid = models.ForeignKey(Hospital, models.DO_NOTHING, db_column='HOSPITALID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MACHINE'


class Machinename(models.Model):
    machinenameid = models.AutoField(db_column='MACHINENAMEID', primary_key=True)  # Field name made lowercase.
    machinename = models.CharField(db_column='MACHINENAME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='ENABLED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MACHINENAME'


class Parts(models.Model):
    partsid = models.CharField(db_column='PARTSID', max_length=50)  # Field name made lowercase.
    partsgpname = models.CharField(db_column='PARTSGPNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.
    facid = models.ForeignKey(Factory, models.DO_NOTHING, db_column='FACID', blank=True, null=True)  # Field name made lowercase.
    partsname = models.CharField(db_column='PARTSNAME', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
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
        managed = False
        db_table = 'SERVICE_SHEET'


class State(models.Model):
    stateid = models.AutoField(db_column='STATEID', primary_key=True)  # Field name made lowercase.
    statename = models.CharField(db_column='STATENAME', max_length=10)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'STATE'


class T023T(models.Model):
    matkl = models.IntegerField(db_column='MATKL', blank=True, null=True)  # Field name made lowercase.
    wgbez = models.CharField(db_column='WGBEZ', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'T023T'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
