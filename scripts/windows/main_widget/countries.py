"""
MIT License

Copyright (c) 2021 B.Jothin kumar

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Author: Jothin kumar (https://jothin.tech)
Github repository of this project: https://github.com/Jothin-kumar/time-widget
"""
import pytz


class Country:
    def __init__(self, iso3166_code: str):
        self.full_name = pytz.country_names[iso3166_code]
        self.iso3166_code = iso3166_code
        self.timezones = pytz.country_timezones(iso3166_code)


countries = [
    Country(iso3166_code='AF'),
    Country(iso3166_code='AX'),
    Country(iso3166_code='AL'),
    Country(iso3166_code='DZ'),
    Country(iso3166_code='AS'),
    Country(iso3166_code='AD'),
    Country(iso3166_code='AO'),
    Country(iso3166_code='AI'),
    Country(iso3166_code='AQ'),
    Country(iso3166_code='AG'),
    Country(iso3166_code='AR'),
    Country(iso3166_code='AM'),
    Country(iso3166_code='AW'),
    Country(iso3166_code='AU'),
    Country(iso3166_code='AT'),
    Country(iso3166_code='AZ'),
    Country(iso3166_code='BS'),
    Country(iso3166_code='BH'),
    Country(iso3166_code='BD'),
    Country(iso3166_code='BB'),
    Country(iso3166_code='BY'),
    Country(iso3166_code='BE'),
    Country(iso3166_code='BZ'),
    Country(iso3166_code='BJ'),
    Country(iso3166_code='BM'),
    Country(iso3166_code='BT'),
    Country(iso3166_code='BO'),
    Country(iso3166_code='BQ'),
    Country(iso3166_code='BA'),
    Country(iso3166_code='BW'),
    Country(iso3166_code='BR'),
    Country(iso3166_code='IO'),
    Country(iso3166_code='VG'),
    Country(iso3166_code='BN'),
    Country(iso3166_code='BG'),
    Country(iso3166_code='BF'),
    Country(iso3166_code='BI'),
    Country(iso3166_code='KH'),
    Country(iso3166_code='CM'),
    Country(iso3166_code='CA'),
    Country(iso3166_code='CV'),
    Country(iso3166_code='KY'),
    Country(iso3166_code='CF'),
    Country(iso3166_code='TD'),
    Country(iso3166_code='CL'),
    Country(iso3166_code='CN'),
    Country(iso3166_code='CX'),
    Country(iso3166_code='CC'),
    Country(iso3166_code='CO'),
    Country(iso3166_code='KM'),
    Country(iso3166_code='CD'),
    Country(iso3166_code='CG'),
    Country(iso3166_code='CK'),
    Country(iso3166_code='CR'),
    Country(iso3166_code='CI'),
    Country(iso3166_code='HR'),
    Country(iso3166_code='CU'),
    Country(iso3166_code='CW'),
    Country(iso3166_code='CY'),
    Country(iso3166_code='CZ'),
    Country(iso3166_code='DK'),
    Country(iso3166_code='DJ'),
    Country(iso3166_code='DM'),
    Country(iso3166_code='DO'),
    Country(iso3166_code='EC'),
    Country(iso3166_code='EG'),
    Country(iso3166_code='SV'),
    Country(iso3166_code='GQ'),
    Country(iso3166_code='ER'),
    Country(iso3166_code='EE'),
    Country(iso3166_code='ET'),
    Country(iso3166_code='FO'),
    Country(iso3166_code='FK'),
    Country(iso3166_code='FJ'),
    Country(iso3166_code='FI'),
    Country(iso3166_code='FR'),
    Country(iso3166_code='GF'),
    Country(iso3166_code='PF'),
    Country(iso3166_code='TF'),
    Country(iso3166_code='GA'),
    Country(iso3166_code='GM'),
    Country(iso3166_code='GE'),
    Country(iso3166_code='DE'),
    Country(iso3166_code='GH'),
    Country(iso3166_code='GI'),
    Country(iso3166_code='GR'),
    Country(iso3166_code='GL'),
    Country(iso3166_code='GD'),
    Country(iso3166_code='GP'),
    Country(iso3166_code='GU'),
    Country(iso3166_code='GT'),
    Country(iso3166_code='GG'),
    Country(iso3166_code='GN'),
    Country(iso3166_code='GW'),
    Country(iso3166_code='GY'),
    Country(iso3166_code='HT'),
    Country(iso3166_code='VA'),
    Country(iso3166_code='HN'),
    Country(iso3166_code='HK'),
    Country(iso3166_code='HU'),
    Country(iso3166_code='IS'),
    Country(iso3166_code='IN'),
    Country(iso3166_code='ID'),
    Country(iso3166_code='IR'),
    Country(iso3166_code='IQ'),
    Country(iso3166_code='IE'),
    Country(iso3166_code='IM'),
    Country(iso3166_code='IL'),
    Country(iso3166_code='IT'),
    Country(iso3166_code='JM'),
    Country(iso3166_code='JP'),
    Country(iso3166_code='JE'),
    Country(iso3166_code='JO'),
    Country(iso3166_code='KZ'),
    Country(iso3166_code='KE'),
    Country(iso3166_code='KI'),
    Country(iso3166_code='KP'),
    Country(iso3166_code='KR'),
    Country(iso3166_code='KW'),
    Country(iso3166_code='KG'),
    Country(iso3166_code='LA'),
    Country(iso3166_code='LV'),
    Country(iso3166_code='LB'),
    Country(iso3166_code='LS'),
    Country(iso3166_code='LR'),
    Country(iso3166_code='LY'),
    Country(iso3166_code='LI'),
    Country(iso3166_code='LT'),
    Country(iso3166_code='LU'),
    Country(iso3166_code='MO'),
    Country(iso3166_code='MG'),
    Country(iso3166_code='MW'),
    Country(iso3166_code='MY'),
    Country(iso3166_code='MV'),
    Country(iso3166_code='ML'),
    Country(iso3166_code='MT'),
    Country(iso3166_code='MH'),
    Country(iso3166_code='MQ'),
    Country(iso3166_code='MR'),
    Country(iso3166_code='MU'),
    Country(iso3166_code='YT'),
    Country(iso3166_code='MX'),
    Country(iso3166_code='FM'),
    Country(iso3166_code='MD'),
    Country(iso3166_code='MC'),
    Country(iso3166_code='MN'),
    Country(iso3166_code='ME'),
    Country(iso3166_code='MS'),
    Country(iso3166_code='MA'),
    Country(iso3166_code='MZ'),
    Country(iso3166_code='MM'),
    Country(iso3166_code='NA'),
    Country(iso3166_code='NR'),
    Country(iso3166_code='NP'),
    Country(iso3166_code='NL'),
    Country(iso3166_code='NC'),
    Country(iso3166_code='NZ'),
    Country(iso3166_code='NI'),
    Country(iso3166_code='NE'),
    Country(iso3166_code='NG'),
    Country(iso3166_code='NU'),
    Country(iso3166_code='NF'),
    Country(iso3166_code='MK'),
    Country(iso3166_code='MP'),
    Country(iso3166_code='NO'),
    Country(iso3166_code='OM'),
    Country(iso3166_code='PK'),
    Country(iso3166_code='PW'),
    Country(iso3166_code='PS'),
    Country(iso3166_code='PA'),
    Country(iso3166_code='PG'),
    Country(iso3166_code='PY'),
    Country(iso3166_code='PE'),
    Country(iso3166_code='PH'),
    Country(iso3166_code='PN'),
    Country(iso3166_code='PL'),
    Country(iso3166_code='PT'),
    Country(iso3166_code='PR'),
    Country(iso3166_code='QA'),
    Country(iso3166_code='RE'),
    Country(iso3166_code='RO'),
    Country(iso3166_code='RU'),
    Country(iso3166_code='RW'),
    Country(iso3166_code='BL'),
    Country(iso3166_code='SH'),
    Country(iso3166_code='KN'),
    Country(iso3166_code='LC'),
    Country(iso3166_code='MF'),
    Country(iso3166_code='PM'),
    Country(iso3166_code='VC'),
    Country(iso3166_code='WS'),
    Country(iso3166_code='SM'),
    Country(iso3166_code='ST'),
    Country(iso3166_code='SA'),
    Country(iso3166_code='SN'),
    Country(iso3166_code='RS'),
    Country(iso3166_code='SC'),
    Country(iso3166_code='SL'),
    Country(iso3166_code='SG'),
    Country(iso3166_code='SX'),
    Country(iso3166_code='SK'),
    Country(iso3166_code='SI'),
    Country(iso3166_code='SB'),
    Country(iso3166_code='SO'),
    Country(iso3166_code='ZA'),
    Country(iso3166_code='GS'),
    Country(iso3166_code='SS'),
    Country(iso3166_code='ES'),
    Country(iso3166_code='LK'),
    Country(iso3166_code='SD'),
    Country(iso3166_code='SR'),
    Country(iso3166_code='SJ'),
    Country(iso3166_code='SZ'),
    Country(iso3166_code='SE'),
    Country(iso3166_code='CH'),
    Country(iso3166_code='SY'),
    Country(iso3166_code='TW'),
    Country(iso3166_code='TJ'),
    Country(iso3166_code='TZ'),
    Country(iso3166_code='TH'),
    Country(iso3166_code='TL'),
    Country(iso3166_code='TG'),
    Country(iso3166_code='TK'),
    Country(iso3166_code='TO'),
    Country(iso3166_code='TT'),
    Country(iso3166_code='TN'),
    Country(iso3166_code='TR'),
    Country(iso3166_code='TM'),
    Country(iso3166_code='TC'),
    Country(iso3166_code='TV'),
    Country(iso3166_code='UG'),
    Country(iso3166_code='UA'),
    Country(iso3166_code='AE'),
    Country(iso3166_code='GB'),
    Country(iso3166_code='US'),
    Country(iso3166_code='UM'),
    Country(iso3166_code='VI'),
    Country(iso3166_code='UY'),
    Country(iso3166_code='UZ'),
    Country(iso3166_code='VU'),
    Country(iso3166_code='VE'),
    Country(iso3166_code='VN'),
    Country(iso3166_code='WF'),
    Country(iso3166_code='EH'),
    Country(iso3166_code='YE'),
    Country(iso3166_code='ZM'),
    Country(iso3166_code='ZW')
]


def get_country_by_iso3166_code(iso3166_code):
    for country in countries:
        if country.iso3166_code == iso3166_code:
            return country
    return None