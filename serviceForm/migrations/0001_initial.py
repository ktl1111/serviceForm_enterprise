# Generated by Django 2.1.15 on 2022-01-04 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('areaid', models.AutoField(db_column='AREAID', primary_key=True, serialize=False)),
                ('areaname', models.CharField(db_column='AREANAME', max_length=10)),
            ],
            options={
                'db_table': 'AREA',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('categoryid', models.AutoField(db_column='CATEGORYID', primary_key=True, serialize=False)),
                ('categoryname', models.CharField(db_column='CATEGORYNAME', max_length=10)),
                ('enabled', models.BooleanField(blank=True, db_column='ENABLED', null=True)),
            ],
            options={
                'db_table': 'CATEGORY',
            },
        ),
        migrations.CreateModel(
            name='ContractType',
            fields=[
                ('contractid', models.AutoField(db_column='CONTRACTID', primary_key=True, serialize=False)),
                ('contractname', models.CharField(db_column='CONTRACTNAME', max_length=10)),
            ],
            options={
                'db_table': 'CONTRACT_TYPE',
            },
        ),
        migrations.CreateModel(
            name='Factory',
            fields=[
                ('facid', models.CharField(db_column='FACID', max_length=10, primary_key=True, serialize=False)),
                ('facname', models.CharField(db_column='FACNAME', max_length=10)),
            ],
            options={
                'db_table': 'FACTORY',
            },
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('hospitalid', models.IntegerField(db_column='HOSPITALID', primary_key=True, serialize=False)),
                ('hospitalname', models.CharField(db_column='HOSPITALNAME', max_length=50)),
                ('hospitalnameabbr', models.CharField(db_column='HOSPITALNAMEABBR', max_length=10)),
                ('areaid', models.IntegerField(db_column='AREAID')),
                ('cityarea', models.CharField(blank=True, db_column='CITYAREA', max_length=10, null=True)),
                ('addr', models.CharField(blank=True, db_column='ADDR', max_length=50, null=True)),
                ('zcode', models.IntegerField(blank=True, db_column='ZCODE', null=True)),
                ('enabled', models.BooleanField(blank=True, db_column='ENABLED', null=True)),
            ],
            options={
                'db_table': 'HOSPITAL',
            },
        ),
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('machineid', models.IntegerField(db_column='MACHINEID', primary_key=True, serialize=False)),
                ('machinename', models.CharField(db_column='MACHINENAME', max_length=50)),
                ('hospitalid', models.IntegerField(db_column='HOSPITALID')),
            ],
            options={
                'db_table': 'MACHINE',
            },
        ),
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partsid', models.CharField(db_column='PARTSID', max_length=50)),
                ('partsgpname', models.CharField(blank=True, db_column='PARTSGPNAME', max_length=50, null=True)),
                ('facid', models.CharField(blank=True, db_column='FACID', max_length=10, null=True)),
                ('partsname', models.CharField(blank=True, db_column='PARTSNAME', max_length=50, null=True)),
            ],
            options={
                'db_table': 'PARTS',
            },
        ),
        migrations.CreateModel(
            name='ServiceSheet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sheetid', models.IntegerField(db_column='SHEETID')),
                ('empid', models.IntegerField(db_column='EMPID')),
                ('areaid', models.IntegerField(db_column='AREAID')),
                ('categoryid', models.IntegerField(db_column='CATEGORYID')),
                ('stateid', models.IntegerField(db_column='STATEID')),
                ('date', models.DateField(db_column='DATE')),
                ('machinestop', models.BooleanField(db_column='MACHINESTOP')),
                ('hospitalid', models.IntegerField(db_column='HOSPITALID')),
                ('receiver', models.CharField(db_column='RECEIVER', max_length=10)),
                ('mensent', models.CharField(db_column='MENSENT', max_length=10)),
                ('contractid', models.IntegerField(db_column='CONTRACTID')),
                ('machinename', models.CharField(db_column='MACHINENAME', max_length=50)),
                ('machineid', models.CharField(db_column='MACHINEID', max_length=10)),
                ('callcont', models.CharField(db_column='CALLCONT', max_length=50)),
                ('brokenitems', models.CharField(db_column='BROKENITEMS', max_length=50)),
                ('partsid', models.IntegerField(db_column='PARTSID')),
                ('calltime', models.TimeField(db_column='CALLTIME')),
                ('arrivetime', models.TimeField(db_column='ARRIVETIME')),
                ('fixingtime', models.TimeField(db_column='FIXINGTIME')),
                ('repairtime', models.TimeField(db_column='REPAIRTIME')),
                ('repairdur', models.FloatField(db_column='REPAIRDUR')),
                ('machinestpdur', models.FloatField(db_column='MACHINESTPDUR')),
                ('repaircont', models.TextField(db_column='REPAIRCONT')),
                ('note', models.TextField(db_column='NOTE')),
            ],
            options={
                'db_table': 'SERVICE_SHEET',
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('stateid', models.AutoField(db_column='STATEID', primary_key=True, serialize=False)),
                ('statename', models.CharField(db_column='STATENAME', max_length=10)),
            ],
            options={
                'db_table': 'STATE',
            },
        ),
        migrations.CreateModel(
            name='T023T',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('matkl', models.IntegerField(blank=True, db_column='MATKL', null=True)),
                ('wgbez', models.CharField(blank=True, db_column='WGBEZ', max_length=50, null=True)),
            ],
            options={
                'db_table': 'T023T',
            },
        ),
    ]
