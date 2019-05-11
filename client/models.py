from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _

from utils.constants import SYSTEM_USER_GROUP, NORMALUSER

ACTIVE, INACTIVE, PENDING = 'AC', 'IN', 'PE'
STATUS_CHOICE = (
    (ACTIVE, _('Active')),
    (INACTIVE, _('Inactive')),
    (PENDING, _('Pending')))


class Profile(models.Model):
    """Client profile"""
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, verbose_name=_('user'),
                             related_name='profile')
    user_type = models.CharField(verbose_name=_('profile type'), max_length=100, choices=SYSTEM_USER_GROUP,
                                 default=NORMALUSER)
    status = models.CharField(max_length=30, choices=STATUS_CHOICE, default=PENDING, verbose_name='status')

    def __str__(self):
        return self.user.email + '-' + self.get_user_type_display() + '-' + self.get_status_display()
