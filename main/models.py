from django.db import models

# Create your models here.


class State(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    abbrev = models.CharField(max_length=255, null=True, blank=True)
    pop = models.CharField(max_length=255, null=True, blank=True)
    state_map = models.ImageField(upload_to='state_map', null=True, blank=True)

    def __unicode__(self):
        return self.name


class StateCapital(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    pop = models.IntegerField(null=True, blank=True)
    #state = models.ForeignKey('main.State', null=True, blank=True)
    #state = models.ManyToManyField('main.State')
    state = models.OneToOneField('main.State', null=True, blank=True)

    def __unicode__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    county = models.CharField(max_length=100, null=True, blank=True)
    state = models.ForeignKey("main.State", null=True, blank=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    zip_code = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural='cities'

    def __unicode__(self):
        return '%s' % self.name
