from django.db import models
from apps.beneficiaries.models import Beneficiary



class Assistance(models.Model):
    """
    Representa una asistencia vinculada a un beneficiario
    """
    beneficiary = models.ForeignKey(
        Beneficiary,
        on_delete=models.CASCADE,
        related_name="assistances"
    )
    author = models.CharField(
        max_length=100,
        verbose_name="author"
    )
    is_first_assistance = models.BooleanField(
        default=False,
        verbose_name="is first assistance"
    )
    address = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="address"
    )
    address_reference = models.TextField(
        blank=True,
        null=True,
        verbose_name="address reference"
    )
    geolocation = models.CharField(
        help_text="Enter X, Y coordinates",
        max_length=100,
        blank=True,
        null=True,
        verbose_name="geolocation"
    )
    assistance_type = models.TextField(
        blank=True,
        null=True,
        verbose_name="assistance type"
    )
    extended_assistance = models.BooleanField(
        default=False,
        verbose_name="follow-up needed"
    )
    extended_assistance_details = models.TextField(
        blank=True,
        null=True,
        verbose_name="follow-up details"
    )
    notes = models.TextField(
        help_text="Additional details or observations about the assistance provided",
        blank=True,
        null=True,
        verbose_name="notes"
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
        ordering = ("created_at",)
        verbose_name = "assistance"
        verbose_name_plural = "assistances"

    def __str__(self):
        return f"Assistance: {self.beneficiary.first_name} {self.beneficiary.last_name} \'{self.beneficiary.nickname}\' - {self.assistance_type} ({self.created_at})"



