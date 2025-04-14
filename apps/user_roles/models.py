from django.db import models

class UserRole(models.Model):
    """
    Representa a un rol de usuario
    """
    name = models.CharField(
        max_length=100,
        verbose_name="role"
    )
    description = models.TextField(
        verbose_name="description"
    )

    class Meta:
        ordering = ("name",)
        verbose_name = "user role"
        verbose_name_plural = "user roles"

    def __str__(self):
        return f"Role: {self.name}"
