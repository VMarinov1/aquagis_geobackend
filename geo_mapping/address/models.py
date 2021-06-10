
from django.db import models


class CommonProps(models.Model):
    '''
    Common properties such as:
        - created_at - timestamp when given object has been created
        - last_edit_at - timestamp when given object has been last edited
        - remarks - text field with remarks
    '''
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    last_edit_at = models.DateTimeField()

    class Meta:
        abstract = True


class SpatialCoordinates(CommonProps):
    uid = models.IntegerField()
    latitude = models.DecimalField()
    longitude = models.DecimalField()
    altitude = models.DecimalField()

    def __str__(self):
        return f'{self.latitude} {self.longitude}'


class AdministrativeProps(CommonProps):
    uid = models.IntegerField()

    # get from local database (Administrative Boundaries -> Oblasti)
    oblast_name = models.CharField()
    oblast_code = models.CharField()
    oblast_version = models.CharField()

    # get from local database (Administrative Boundaries -> Obshtinni)
    obshtina_name = models.CharField()
    obshtina_code = models.CharField()
    obshtina_version = models.CharField()

    # get from local database (Administrative Boundaries -> Zemlishta)
    zemlishte_name = models.CharField()
    zemlishte_code = models.CharField()
    zemlishte_version = models.CharField()

    # get from local database (Administrative Boundaries -> ekatte)
    ekatte = models.CharField()

    # get from local database (Administrative Boundaries -> postcodes)
    postcode = models.CharField()

    # get from local database (Administrative Boundaries -> populated places)
    populated_place = models.CharField()

    # get from local database (Administrative Boundaries -> Quartals)
    quart = models.CharField()

    version = models.CharField()

    fulltext = models.CharField()

    coords = models.ForeignKey(to=SpatialCoordinates)

    def __str__(self):
        return f'{self.fulltext}'

    def save(self):
        pass


class Address(CommonProps):
    uid = models.IntegerField()
    address_string = models.CharField()
    address_county = models.CharField()
    address_city = models.CharField()
    address_ = models.CharField()

    address_coords = models.ForeignKey(to=AdministrativeProps)

    def __str__(self):
        return f'{self.address_string}'


class Parcel(CommonProps):
    uid = models.IntegerField()
    parcel_uid = models.CharField()

    coords = models.ForeignKey(to=AdministrativeProps)

    def __str__(self):
        return f'{self.parcel_uid}'


class GeoName(CommonProps):
    uid = models.IntegerField()
    geoname = models.CharField()

    coords = models.ForeignKey(to=AdministrativeProps)

    def __str__(self):
        return f'{self.geoname}'
