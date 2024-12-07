from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils.translation import gettext_lazy as _

class UserManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password=None):
        """
        Creates and returns a regular user with an email, first name, and last name.
        """
        if not email:
            raise ValueError("Users must have an email address")
        if not first_name:
            raise ValueError("Users must have a first name")
        if not last_name:
            raise ValueError("Users must have a last name")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, password):
        """
        Creates and returns a superuser with an email, first name, last name, and password.
        """
        user = self.create_user(
            email=email,
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True  # Make the superuser staff by default
        user.is_superuser = True  # Mark as superuser
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']  # These fields are required for the user creation

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """
        Check if the user has a specific permission.
        This method can be extended with custom permission checks.
        """
        return True

    def has_module_perms(self, app_label):
        """
        Check if the user has permissions to access a specific app module.
        """
        return True

    @property
    def is_staff(self):
        """
        Check if the user is a staff member.
        """
        return self.is_admin

    class Meta:
        permissions = [
            ('can_view_dashboard', _('Can view dashboard')),
        ]

class EmailRecord(models.Model):
    subject = models.CharField(max_length=255)
    body = models.TextField()
    recipient = models.EmailField()
    sent_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)  # True for success, False for failure

    def _str_(self):
        return f"Email to {self.recipient} - {self.subject}"

class Feedback(models.Model):
    name = models.CharField(max_length=100, help_text="Name of the person giving feedback")
    email = models.EmailField(help_text="Email address of the person giving feedback")
    feedback = models.TextField(help_text="Feedback message provided by the user")
    submitted_at = models.DateTimeField(auto_now_add=True, help_text="Timestamp when the feedback was submitted")

    def _str_(self):
        return f"{self.name} ({self.email}) - {self.submitted_at.strftime('%Y-%m-%d %H:%M:%S')}"
