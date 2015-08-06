# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Area(models.Model):
    id_area = models.AutoField(db_column='ID_Area', unique=True, primary_key=True)  
    # Field name made lowercase.
    site = models.ForeignKey('Site', db_column='Site_ID')  
    # Field name made lowercase.
    areanr = models.CharField(db_column='areaNR', max_length=45, blank=True, null=True)  
    # Field name made lowercase.

    class Meta:
        db_table = 'Area'
        unique_together = (('id_area', 'site'),)
        #had to replace "ID_Area" and 'Site_ID' against the field names
        #because while migrating the error occured: 
        #"'ID_Area' refers to the non-existent field 'ID_Area'""


class Period(models.Model):
    id_period = models.AutoField(db_column='ID_Period', primary_key=True)  # Field name made lowercase.
    chronological_system = models.CharField(max_length=100, blank=True, null=True)
    period = models.CharField(max_length=100, blank=True, null=True)
    absolute_date_from = models.CharField(max_length=100, blank=True, null=True)
    absolute_date_to = models.CharField(max_length=100, blank=True, null=True)
    dating_method = models.CharField(max_length=100, blank=True, null=True)
    dated_by = models.CharField(max_length=100, blank=True, null=True)
    c14_calibrated = models.CharField(db_column='C14_calibrated', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c14_absolute_from = models.CharField(db_column='C14_absolute_from', max_length=100, blank=True, null=True)  # Field name made lowercase.
    c14_absolute_to = models.CharField(db_column='C14_absolute_to', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reference_ch = models.CharField(db_column='reference_CH', max_length=100, blank=True, null=True)  # Field name made lowercase.
    comment_ch = models.CharField(db_column='comment_CH', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Period'


class ResearchEvent(models.Model):
    id_research = models.AutoField(db_column='ID_Research', primary_key=True)  # Field name made lowercase.
    research_type = models.CharField(max_length=100, blank=True, null=True)
    institution = models.CharField(max_length=100, blank=True, null=True)
    year_of_activity_start_year = models.CharField(max_length=100, blank=True, null=True)
    year_of_activity_end_year = models.CharField(max_length=100, blank=True, null=True)
    project_name = models.CharField(max_length=100, blank=True, null=True)
    project_id = models.CharField(db_column='project_ID', max_length=100, blank=True, null=True)  # Field name made lowercase.
    project_leader = models.CharField(max_length=100, blank=True, null=True)
    reference_rh = models.CharField(db_column='reference_RH', max_length=100, blank=True, null=True)  # Field name made lowercase.
    comment_rh = models.CharField(db_column='comment_RH', max_length=100, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        db_table = 'Research_Event'


class Site(models.Model):
    id_sites = models.AutoField(db_column='ID_Site', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=350, blank=True, null=True,
        help_text="Name of a place in which evidence of past activity is preserved and which represents a part of the archaeological record.")
    region = models.CharField(max_length=50, blank=True,
        null=True, help_text="Geographical area where the site is located.")
    province = models.CharField(max_length=50, blank=True,
        null=True, help_text="Name of the state province where site is located.")
    country = models.CharField(max_length=50, blank=True,
        null=True, help_text="Name of the state where site is located.")
    description = models.CharField(max_length=400, blank=True, null=True,
        help_text="Free text summary account on the site.")
    topography = models.CharField(max_length=50, blank=True, null=True,
        help_text="Description of surface shape and features.")
    gps_data_coordinate_system = models.CharField(db_column='GPS_data_coordinate_system',
        max_length=50, blank=True, null=True,
        help_text="Name of system uniquely determining the position of the site.")  # Field name made lowercase.
    gps_data_n = models.CharField(db_column='GPS_data_N', max_length=50,
        blank=True, null=True, help_text="North value of coordinate.")  # Field name made lowercase.
    gps_data_e = models.CharField(db_column='GPS_data_E', max_length=50,
        blank=True, null=True, help_text="East value of coordinate.")  # Field name made lowercase.
    gps_data_z = models.CharField(db_column='GPS_data_Z', max_length=50,
        blank=True, null=True, help_text="Z value of coordinate (elevation).")  # Field name made lowercase.
    coordinate_source = models.CharField(max_length=100, blank=True, null=True,
        help_text="Bibliographic and web-based references to publications and other relevant information on the site.")
    reference_site = models.CharField(db_column='reference_SITE', max_length=100,
        blank=True, null=True, 
        help_text="Bibliographic and web-based references to publications and other relevant information on the site.")  # Field name made lowercase.
    class Meta:
        db_table = 'Site'


class Finds(models.Model):
    id_finds = models.AutoField(db_column='ID_finds', primary_key=True)  # Field name made lowercase.
    type = models.CharField(max_length=100, blank=True, null=True)
    material = models.CharField(max_length=100, blank=True, null=True)
    reference = models.CharField(max_length=100, blank=True, null=True)
    comment = models.CharField(max_length=100, blank=True, null=True)
    interpretationid_interpretation = models.IntegerField(db_column='InterpretationID_Interpretation')  # Field name made lowercase.
    period_id_period = models.ForeignKey(Period, db_column='Period_ID_Period')  # Field name made lowercase.
    research_event_id_research = models.ForeignKey(ResearchEvent, db_column='Research_Event_ID_Research')  # Field name made lowercase.
    area_id_area = models.ForeignKey(Area, db_column='Area_ID_Area', related_name='ID_Area')  # Field name made lowercase.
    area_site = models.ForeignKey(Area, db_column='Area_Site_ID', related_name='Site')  # Field name made lowercase.
#here I had to add 'related'
    class Meta:
        db_table = 'finds'
