from django.db import models
from django.core.validators import RegexValidator


class Beneficiary(models.Model):
    """
    Representa a un beneficiario
    """
    dni = models.CharField(
        max_length=10,  
        unique=True,
        blank=True,
        null=True,
        verbose_name="dni",
        validators=[RegexValidator(
            regex=r'^\d{6,10}$',  
            message='DNI must be between 6 and 10 digits'
        )]
    )
    author = models.BigIntegerField(
        blank=True,
        null=True,
    )
    author_details = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="author"
    )
    has_physical_dni = models.BooleanField(
        default=False,
        verbose_name="has physical dni"
    )
    first_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="first name"
    )   
    last_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="last name"
    )
    nickname = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="nickname"
    )
    birthdate = models.DateField(
        help_text="Please use the following format: <em>YYYY-MM-DD</em>",
        blank=True,
        null=True,
        verbose_name="birth date"
    )
    phone_number = models.CharField(
        max_length=100,
        help_text="format: XXX-XXX-XXXX",
        blank=True,
        null=True,
        verbose_name="phone"
    )
    reference_phone_number = models.TextField(
        help_text="Whose number is it?",
        blank=True,
        null=True,
        verbose_name="reference phone"
    )
    geolocation = models.CharField(
        help_text="Enter X, Y coordinates",
        max_length=100,
        blank=True,
        null=True,
        verbose_name="geolocation"
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
    sex = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="sex"
    )
    nationality = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="nationality"
    )
    is_fixed_or_transitory_place = models.BooleanField(
        default=False,
        verbose_name="transitory location"
    )
    life_center = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name="life center"
    )
    has_family_contact = models.TextField(
        default=False,
        help_text="Does this person any relationship or contact with family members? Specify",
        verbose_name="has family contact"
    )  
    subsidies = models.TextField(
        default=False,
        help_text="Does this person receives any subsidies or financial aid",
        verbose_name="subsidies"
    )  
    health_info = models.TextField(
        help_text="Describe any relevant health conditions, ongoing treatments, or recurring needs such as medication, psychological support, or mobility aids. This field is intended for background health information rather than specific assistances provided.",
        blank=True,
        null=True,
        verbose_name="health info"
    )

    class Meta:
        ordering = ("first_name",)
        verbose_name = "beneficiary"
        verbose_name_plural = "beneficiaries"

    def __str__(self):
        formatted_nickname = f"'{self.nickname}'" if self.nickname else None
        return " ".join(filter(None, [self.first_name, self.last_name, formatted_nickname])) or "Unnamed Beneficiary"

