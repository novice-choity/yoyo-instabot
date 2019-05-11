# common timezone from pytz
import datetime

import pytz
from django.utils.translation import ugettext_lazy as _

TIMEZONE_CHOICES = [(t, t) for t in pytz.common_timezones]

# System user groups
ADMINUSER = 'au'
NORMALUSER = 'nu'

SYSTEM_USER_GROUP = (
    (ADMINUSER, _('Admin')),
    (NORMALUSER, _('User')),
)

# For list of years
CURRENT_YEAR = datetime.datetime.now().year

START_YEAR = CURRENT_YEAR - 50
END_YEAR = CURRENT_YEAR + 50

YEARS = [(year, _(str(year))) for year in range(START_YEAR, END_YEAR)]
