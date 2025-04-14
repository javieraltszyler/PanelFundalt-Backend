from django.db import models
from django.core.validators import RegexValidator

class Organization(models.Model):
    """
    Representa a una organización
    """
    name = models.CharField(
        max_length=100,
        verbose_name="name"
    )
    description = models.TextField(
        verbose_name="description"
    )
    purpose = models.CharField(
        max_length=200,
        verbose_name="purpose"
    )
    cuit = models.CharField(
        max_length=13,
        unique=True,
        verbose_name="CUIT",
        help_text="Formato: XX-XXXXXXXX-X o XXXXXXXXXXX",
        validators=[RegexValidator(
            regex=r'^(\d{2}-\d{8}-\d{1}|\d{11})$',
            message='CUIT debe tener formato XX-XXXXXXXX-X o 11 dígitos sin guiones'
        )]
    )
    address = models.CharField(
        max_length=100,
        verbose_name="address"
    )
    geolocation = models.CharField(
        help_text="Enter X, Y coordinates",
        max_length=100,
        blank=True,
        null=True,
        verbose_name="geolocation"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="creation time"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="update time"
    )


    class Meta:
            ordering = ("name",)
            verbose_name = "organization"
            verbose_name_plural = "organizations"

    def __str__(self):
        return f"Organization: {self.name}"  