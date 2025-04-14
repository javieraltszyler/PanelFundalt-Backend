# from django.test import TestCase
# from django.core.exceptions import ValidationError
# from datetime import date
# from .models import Beneficiary


# class BeneficiaryModelTest(TestCase):
#     """Test suite for the Beneficiary model"""

#     def setUp(self):
#         """Set up test data"""
#         self.beneficiary = Beneficiary.objects.create(
#             dni="12345678",
#             first_name="Juan",
#             last_name="Pérez",
#             nickname="Juanito",
#             birthdate=date(1990, 1, 1),
#             phone_number="123-456-7890",
#             location="Calle Principal 123"
#         )

#     def test_create_beneficiary(self):
#         """Test beneficiary creation with minimal data"""
#         beneficiary = Beneficiary.objects.create(
#             dni="87654321",
#             first_name="María",
#             last_name="González"
#         )
#         self.assertEqual(beneficiary.dni, "87654321")
#         self.assertEqual(beneficiary.first_name, "María")
#         self.assertEqual(beneficiary.last_name, "González")

#     def test_str_representation(self):
#         """Test the string representation of a beneficiary"""
#         # Full name with nickname
#         self.assertEqual(str(self.beneficiary), "Juan Pérez 'Juanito'")
        
#         # Without nickname
#         beneficiary = Beneficiary.objects.create(
#             first_name="Ana",
#             last_name="López"
#         )
#         self.assertEqual(str(beneficiary), "Ana López")
        
#         # Only first name
#         beneficiary = Beneficiary.objects.create(
#             first_name="Pedro"
#         )
#         self.assertEqual(str(beneficiary), "Pedro")
        
#         # No name
#         beneficiary = Beneficiary.objects.create()
#         self.assertEqual(str(beneficiary), "Unnamed Beneficiary")

#     def test_dni_validation(self):
#         """Test DNI validation"""
#         # Test invalid DNI formats
#         with self.assertRaises(ValidationError):
#             beneficiary = Beneficiary(dni="123")  # Too short
#             beneficiary.full_clean()
        
#         with self.assertRaises(ValidationError):
#             beneficiary = Beneficiary(dni="12345678901")  # Too long
#             beneficiary.full_clean()
        
#         with self.assertRaises(ValidationError):
#             beneficiary = Beneficiary(dni="123abc45")  # Contains letters
#             beneficiary.full_clean()
        
#         # Test valid DNI
#         beneficiary = Beneficiary(dni="123456789")
#         beneficiary.full_clean()  # Should not raise ValidationError

#     def test_optional_fields(self):
#         """Test that optional fields can be null or blank"""
#         beneficiary = Beneficiary.objects.create(
#             dni="11223344"
#         )
#         self.assertIsNone(beneficiary.birthdate)
#         self.assertIsNone(beneficiary.phone_number)
#         self.assertIsNone(beneficiary.contact_info)
#         self.assertIsNone(beneficiary.life_center)
#         self.assertIsNone(beneficiary.subsidies_details)
#         self.assertIsNone(beneficiary.health_info)

#     def test_boolean_field_defaults(self):
#         """Test default values for boolean fields"""
#         beneficiary = Beneficiary.objects.create(
#             dni="99887766"
#         )
#         self.assertFalse(beneficiary.is_fixed_or_transitory_place)
#         self.assertFalse(beneficiary.receives_subsidies)

#     def test_unique_dni(self):
#         """Test that DNI must be unique"""
#         Beneficiary.objects.create(dni="12121212")
#         with self.assertRaises(Exception):  # Could be IntegrityError or ValidationError
#             Beneficiary.objects.create(dni="12121212")

#     def test_max_length_validation(self):
#         """Test max length validation for CharField fields"""
#         long_string = "a" * 101  # 101 characters
#         with self.assertRaises(ValidationError):
#             beneficiary = Beneficiary(
#                 first_name=long_string,
#                 last_name="Test"
#             )
#             beneficiary.full_clean()

#     def test_subsidies_logic(self):
#         """Test the logic between receives_subsidies and subsidies_details"""
#         # When receives_subsidies is True, subsidies_details can be provided
#         beneficiary = Beneficiary.objects.create(
#             dni="44556677",
#             receives_subsidies=True,
#             subsidies_details="Recibe ayuda social"
#         )
#         self.assertTrue(beneficiary.receives_subsidies)
#         self.assertEqual(beneficiary.subsidies_details, "Recibe ayuda social")

#         # When receives_subsidies is False, subsidies_details can still be null
#         beneficiary = Beneficiary.objects.create(
#             dni="77665544",
#             receives_subsidies=False
#         )
#         self.assertFalse(beneficiary.receives_subsidies)
#         self.assertIsNone(beneficiary.subsidies_details)
