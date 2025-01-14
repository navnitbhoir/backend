from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('employee', 'Employee'),
        ('admin', 'Admin'),
        ('manager', 'Manager'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='employee')

    email = models.EmailField(unique=True)  # Ensure email is unique
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] 

    # Define related_name to avoid conflicts
    groups = models.ManyToManyField(
        Group,
        related_name="custom_user_groups",  # Change the related name
        blank=True,
        help_text="The groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="custom_user_permissions",  # Change the related name
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return f"{self.username} ({self.role})"
