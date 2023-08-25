import phonenumbers
from phonenumbers import carrier, geocoder, timezone

number = input()

ch_number = phonenumbers.parse(number, 'CH')
print(ch_number)
print(geocoder.description_for_number(ch_number, 'en'))

ch_number = phonenumbers.parse(number, 'RO')
print(carrier.name_for_number(ch_number, 'en'))

ch_number = phonenumbers.parse(number)
time_zone = timezone.time_zones_for_number(ch_number)
print(time_zone)