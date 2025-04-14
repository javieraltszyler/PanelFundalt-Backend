from django.core.management.base import BaseCommand
from apps.beneficiaries.models import Beneficiary
from apps.assistances.models import Assistance
from datetime import date


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        beneficiaries = [
            Beneficiary(dni="11112222", first_name="Lucía", last_name="Martínez", nickname="Lu", birthdate=date(1990, 4, 12), phone_number="111-222-3333", location="Under the oak tree near the church", is_fixed_or_transitory_place=False, receives_subsidies=True, subsidies_details="Disability pension", health_info="Chronic back pain"),
            Beneficiary(dni="22223333", first_name="Diego", last_name="Suárez", nickname=None, birthdate=date(1982, 11, 3), location="Market entrance", reference_phone_number="222-333-4444", phone_number="333-444-5555", life_center="Hope Center", health_info="Psychological support required"),
            Beneficiary(dni="33334444", first_name=None, last_name="Gómez", nickname="Pato", birthdate=date(1975, 9, 27), location="Beside old train tracks", receives_subsidies=False, contact_info="Facebook: pato.gomez75"),
            Beneficiary(dni="44445555", first_name="Esteban", last_name="Morales", nickname=None, birthdate=date(2001, 6, 10), location="Back alley near 5th Ave", is_fixed_or_transitory_place=True, health_info="Asthma; needs inhaler"),
            Beneficiary(dni="55556666", first_name="Verónica", last_name=None, nickname="Vero", birthdate=date(1994, 2, 28), location="Near Plaza Mayor", phone_number="444-555-6666", receives_subsidies=True, subsidies_details="Food stamps", life_center="Community Shelter", contact_info="Sister’s phone: 555-666-7777"),
        ]

        beneficiaries = Beneficiary.objects.bulk_create(beneficiaries)
        print(f"Beneficiaries properly saved: {beneficiaries}")

        assistances = [
            Assistance(
                beneficiary=Beneficiary.objects.get(dni="11112222"),
                author="Field Worker A",
                assistance_type="Health Check",
                geolocation="40.712776, -74.005974",
                address="Corner of Main St and 1st Ave",
                address_reference="Near the church entrance",
                extended_assistance=True,
                extended_assistance_details="Scheduled follow-up in 2 weeks",
                notes="Complained about persistent back pain; given referral."
            ),
            Assistance(
                beneficiary=Beneficiary.objects.get(dni="22223333"),
                author="Volunteer B",
                assistance_type="Food Kit",
                geolocation="40.735657, -74.172366",
                address="Market Square",
                address_reference="Near main gate",
                extended_assistance=False,
                notes="Given standard food kit, including canned goods and water."
            ),
            Assistance(
                beneficiary=Beneficiary.objects.get(dni="33334444"),
                author="Support Worker C",
                assistance_type="Mental Health Referral",
                geolocation="40.758896, -73.985130",
                address="Old train tracks area",
                address_reference="Abandoned warehouse side",
                extended_assistance=True,
                extended_assistance_details="Follow-up with psychologist scheduled",
                notes="Appeared anxious, accepted help for mental support."
            ),
            Assistance(
                beneficiary=Beneficiary.objects.get(dni="44445555"),
                author="Mobile Clinic Team",
                assistance_type="Medical Supplies",
                geolocation="40.730610, -73.935242",
                address="5th Ave back alley",
                address_reference="Next to the bakery dumpster",
                extended_assistance=False,
                notes="Received inhaler and basic hygiene kit."
            ),
            Assistance(
                beneficiary=Beneficiary.objects.get(dni="55556666"),
                author="NGO Volunteer",
                assistance_type="Clothing Donation",
                geolocation="40.748817, -73.985428",
                address="Plaza Mayor",
                address_reference="Statue side",
                extended_assistance=False,
                notes="Provided warm clothes and socks."
            ),
        ]

        assistances = Assistance.objects.bulk_create(assistances)
        print(f"Assistances properly saved: {assistances}")
