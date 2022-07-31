import phonenumbers


from phonenumbers import geocoder

# get user input as phone number and add + in front of string
number = f"+{input()}"
ch_number = phonenumbers.parse(number, "CH")
print(geocoder.country_name_for_number(ch_number, "en"))
print(geocoder.description_for_number(ch_number, "en"))
print(phonenumbers.parse(number, "CH"))

from phonenumbers import carrier
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en"))
print(service_number)

from phonenumbers import timezone
gb_number = phonenumbers.parse(number, "GB")
print(timezone.time_zones_for_number(gb_number))