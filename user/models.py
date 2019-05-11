from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, BaseUserManager
from django.core import validators
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from instabot.settings import LANGUAGES, EN
from utils.constants import TIMEZONE_CHOICES


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, username, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        now = timezone.now()
        # if not username:
        #     raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username=None, password=None, **extra_fields):
        return self._create_user(email, username, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, None, password, True, True, **extra_fields)


class InstaUser(AbstractBaseUser, PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username, password are required. Other fields are optional.
    """
    username = models.CharField(_('Username'), max_length=30, unique=True,
                                help_text=_('Required. 30 characters or fewer. Letters, digits and '
                                            '@/./+/-/_ only.'),
                                validators=[
                                    validators.RegexValidator(
                                        r'^[a-zA-Z0-9_.]{4,30}$',
                                        _('Enter a valid username. '
                                          'Username accepts a-z, A-Z, 0-9, . and _'), 'invalid'),
                                ],
                                error_messages={
                                    'unique': _("A user with the username already exists."),
                                }, null=True, blank=True)
    email = models.EmailField(_('Email'), unique=True, error_messages={
        'unique': _("A user with the email already exists."),
    })
    language = models.CharField(_('Language'), max_length=3, choices=LANGUAGES, default=EN)
    user_tz = models.CharField(_('Timezone'), max_length=100, choices=TIMEZONE_CHOICES, default=settings.TIME_ZONE)
    first_name = models.CharField(_('First name'), max_length=100, blank=True)
    last_name = models.CharField(_('Last name'), max_length=100, blank=True)
    image = models.ImageField(_('Image'), blank=True, null=True, upload_to='user/')
    is_staff = models.BooleanField(_('Staff'), default=False,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('Active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('Joined'), default=timezone.now)

    objects = UserManager()
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name
