from faker import Faker
from faker.providers import internet

fake = Faker()
fake.add_provider(internet)

"""
We might come across a situation where we need to generate some test data or use some 'dummy data in our analysis.
One way to get dummy data is by using the Faker library ('pip install faker').
This script will generate fake data for various categories for you very quickly when you need to.
Please check this [link](https://faker.readthedocs.io/en/latest/fakerclass.html) for more details.
"""

# Localized providers:
# ar_EG - Arabic (Egypt)
# ar_PS - Arabic (Palestine)
# ar_SA - Arabic (Saudi Arabia)
# bg_BG - Bulgarian
# bs_BA - Bosnian
# cs_CZ - Czech
# de_DE - German
# dk_DK - Danish
# el_GR - Greek
# en_AU - English (Australia)
# en_CA - English (Canada)
# en_GB - English (Great Britain)
# en_IN - English (India)
# en_NZ - English (New Zealand)
# en_US - English (United States)
# es_ES - Spanish (Spain)
# es_MX - Spanish (Mexico)
# et_EE - Estonian
# fa_IR - Persian (Iran)
# fi_FI - Finnish
# fr_FR - French
# hi_IN - Hindi
# hr_HR - Croatian
# hu_HU - Hungarian
# hy_AM - Armenian
# it_IT - Italian
# ja_JP - Japanese
# ka_GE - Georgian (Georgia)
# ko_KR - Korean
# lt_LT - Lithuanian
# lv_LV - Latvian
# ne_NP - Nepali
# nl_NL - Dutch (Netherlands)
# no_NO - Norwegian
# pl_PL - Polish
# pt_BR - Portuguese (Brazil)
# pt_PT - Portuguese (Portugal)
# ro_RO - Romanian
# ru_RU - Russian
# sl_SI - Slovene
# sv_SE - Swedish
# tr_TR - Turkish
# uk_UA - Ukrainian
# zh_CN - Chinese (China)
# zh_TW - Chinese (Taiwan)

# Generating fake persons data
for _ in range(10):
    # Generating fake name
    print(fake.name())
    # Generating fake email
    print(fake.email())
    # Generating fake url
    print(fake.url())
    # Generating a fake IP Address provider
    print(fake.ipv4_private())
    # Generating fake country name
    print(fake.country())
    # Generating fake lat and lon
    print(fake.latitude(), fake.longitude())
    # Generating fake address
    print(fake.address()+"\n")


# Generating fake json profiles
for _ in range(10):
    # Generating fake profile
    print(fake.profile())


# Generating fake German names and addresses
fake = Faker('de_DE')
for _ in range(10):
    # Generating fake German name
    print(fake.name())
    # Generating fake German address
    print(fake.address()+"\n")


# Generating fake Brazilian names and addresses
fake = Faker('pt_BR')
for _ in range(10):
    # Generating fake Brazilian name
    print(fake.name())
    # Generating fake Brazilian address
    print(fake.address()+"\n")


# Generating fake quotes
for _ in range(10):
    # Generating fake text
    print("\'" + fake.text() + "\'")
    print("\t" + fake.name() + "\n")
