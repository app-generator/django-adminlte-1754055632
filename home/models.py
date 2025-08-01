# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    my_test = models.CharField(max_length=255, null=True, blank=True)
    one_test = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Blank(models.Model):

    #__Blank_FIELDS__
    name_user = models.CharField(max_length=255, null=True, blank=True)
    number_user = models.IntegerField(null=True, blank=True)
    adress_state = models.CharField(max_length=255, null=True, blank=True)
    adress_city = models.CharField(max_length=255, null=True, blank=True)
    adress_street = models.CharField(max_length=255, null=True, blank=True)
    mama_name = models.CharField(max_length=255, null=True, blank=True)
    number_mama = models.IntegerField(null=True, blank=True)
    index = models.IntegerField(null=True, blank=True)
    name_friends = models.CharField(max_length=255, null=True, blank=True)

    #__Blank_FIELDS__END

    class Meta:
        verbose_name        = _("Blank")
        verbose_name_plural = _("Blank")



#__MODELS__END
