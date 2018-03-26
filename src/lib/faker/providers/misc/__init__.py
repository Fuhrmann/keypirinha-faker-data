# coding=utf-8

from __future__ import unicode_literals
import hashlib
import string
import uuid
import os
import sys

from .. import BaseProvider


class Provider(BaseProvider):
    # Locales supported by Linux Mint from `/usr/share/i18n/SUPPORTED`
    language_locale_codes = {
        'aa': ('DJ', 'ER', 'ET'), 'af': ('ZA',), 'ak': ('GH',), 'am': ('ET',),
        'an': ('ES',), 'apn': ('IN',),
        'ar': ('AE', 'BH', 'DJ', 'DZ', 'EG', 'EH', 'ER', 'IL', 'IN',
               'IQ', 'JO', 'KM', 'KW', 'LB', 'LY', 'MA', 'MR', 'OM',
               'PS', 'QA', 'SA', 'SD', 'SO', 'SS', 'SY', 'TD', 'TN',
               'YE'),
        'as': ('IN',), 'ast': ('ES',), 'ayc': ('PE',), 'az': ('AZ', 'IN'),
        'be': ('BY',), 'bem': ('ZM',), 'ber': ('DZ', 'MA'), 'bg': ('BG',),
        'bhb': ('IN',), 'bho': ('IN',), 'bn': ('BD', 'IN'), 'bo': ('CN', 'IN'),
        'br': ('FR',), 'brx': ('IN',), 'bs': ('BA',), 'byn': ('ER',),
        'ca': ('AD', 'ES', 'FR', 'IT'), 'ce': ('RU',), 'ckb': ('IQ',),
        'cmn': ('TW',), 'crh': ('UA',), 'cs': ('CZ',), 'csb': ('PL',),
        'cv': ('RU',), 'cy': ('GB',), 'da': ('DK',),
        'de': ('AT', 'BE', 'CH', 'DE', 'LI', 'LU'), 'doi': ('IN',),
        'dv': ('MV',), 'dz': ('BT',), 'el': ('GR', 'CY'),
        'en': ('AG', 'AU', 'BW', 'CA', 'DK', 'GB', 'HK', 'IE', 'IN', 'NG',
               'NZ', 'PH', 'SG', 'US', 'ZA', 'ZM', 'ZW'),
        'eo': ('US',),
        'es': ('AR', 'BO', 'CL', 'CO', 'CR', 'CU', 'DO', 'EC', 'ES', 'GT',
               'HN', 'MX', 'NI', 'PA', 'PE', 'PR', 'PY', 'SV', 'US', 'UY', 'VE'
               ), 'et': ('EE',), 'eu': ('ES', 'FR'), 'fa': ('IR',),
        'ff': ('SN',), 'fi': ('FI',), 'fil': ('PH',), 'fo': ('FO',),
        'fr': ('CA', 'CH', 'FR', 'LU'), 'fur': ('IT',), 'fy': ('NL', 'DE'),
        'ga': ('IE',), 'gd': ('GB',), 'gez': ('ER', 'ET'), 'gl': ('ES',),
        'gu': ('IN',), 'gv': ('GB',), 'ha': ('NG',), 'hak': ('TW',),
        'he': ('IL',), 'hi': ('IN',), 'hne': ('IN',), 'hr': ('HR',),
        'hsb': ('DE',), 'ht': ('HT',), 'hu': ('HU',), 'hy': ('AM',),
        'ia': ('FR',), 'id': ('ID',), 'ig': ('NG',), 'ik': ('CA',),
        'is': ('IS',), 'it': ('CH', 'IT'), 'iu': ('CA',), 'iw': ('IL',),
        'ja': ('JP',), 'ka': ('GE',), 'kk': ('KZ',), 'kl': ('GL',),
        'km': ('KH',), 'kn': ('IN',), 'ko': ('KR',), 'kok': ('IN',),
        'ks': ('IN',), 'ku': ('TR',), 'kw': ('GB',), 'ky': ('KG',),
        'lb': ('LU',), 'lg': ('UG',), 'li': ('BE', 'NL'), 'lij': ('IT',),
        'ln': ('CD',), 'lo': ('LA',), 'lt': ('LT',), 'lv': ('LV',),
        'lzh': ('TW',), 'mag': ('IN',), 'mai': ('IN',), 'mg': ('MG',),
        'mhr': ('RU',), 'mi': ('NZ',), 'mk': ('MK',), 'ml': ('IN',),
        'mn': ('MN',), 'mni': ('IN',), 'mr': ('IN',), 'ms': ('MY',),
        'mt': ('MT',), 'my': ('MM',), 'nan': ('TW',), 'nb': ('NO',),
        'nds': ('DE', 'NL'), 'ne': ('NP',), 'nhn': ('MX',),
        'niu': ('NU', 'NZ'), 'nl': ('AW', 'BE', 'NL'), 'nn': ('NO',),
        'nr': ('ZA',), 'nso': ('ZA',), 'oc': ('FR',), 'om': ('ET', 'KE'),
        'or': ('IN',), 'os': ('RU',), 'pa': ('IN', 'PK'),
        'pap': ('AN', 'AW', 'CW'), 'pl': ('PL',), 'ps': ('AF',),
        'pt': ('BR', 'PT'), 'quz': ('PE',), 'raj': ('IN',), 'ro': ('RO',),
        'ru': ('RU', 'UA'), 'rw': ('RW',), 'sa': ('IN',), 'sat': ('IN',),
        'sc': ('IT',), 'sd': ('IN', 'PK'), 'se': ('NO',), 'shs': ('CA',),
        'si': ('LK',), 'sid': ('ET',), 'sk': ('SK',), 'sl': ('SI',),
        'so': ('DJ', 'ET', 'KE', 'SO'), 'sq': ('AL', 'ML'), 'sr': ('ME', 'RS'),
        'ss': ('ZA',), 'st': ('ZA',), 'sv': ('FI', 'SE'), 'sw': ('KE', 'TZ'),
        'szl': ('PL',), 'ta': ('IN', 'LK'), 'tcy': ('IN',), 'te': ('IN',),
        'tg': ('TJ',), 'th': ('TH',), 'the': ('NP',), 'ti': ('ER', 'ET'),
        'tig': ('ER',), 'tk': ('TM',), 'tl': ('PH',), 'tn': ('ZA',),
        'tr': ('CY', 'TR'), 'ts': ('ZA',), 'tt': ('RU',), 'ug': ('CN',),
        'uk': ('UA',), 'unm': ('US',), 'ur': ('IN', 'PK'), 'uz': ('UZ',),
        've': ('ZA',), 'vi': ('VN',), 'wa': ('BE',), 'wae': ('CH',),
        'wal': ('ET',), 'wo': ('SN',), 'xh': ('ZA',), 'yi': ('US',),
        'yo': ('NG',), 'yue': ('HK',), 'zh': ('CN', 'HK', 'SG', 'TW'),
        'zu': ('ZA',)
    }

    def boolean(self, chance_of_getting_true=50):
        return self.generator.random.randint(1, 100) <= chance_of_getting_true

    def null_boolean(self):
        return {
            0: None,
            1: True,
            -1: False
        }[self.generator.random.randint(-1, 1)]

    def binary(self, length=(1 * 1024 * 1024)):
        """ Returns random binary blob.

        Default blob size is 1 Mb.
        """
        blob = [self.generator.random.randrange(256) for o in range(length)]
        return bytes(blob) if sys.version_info[0] >= 3 else bytearray(blob)

    def md5(self, raw_output=False):
        """
        Calculates the md5 hash of a given string
        :example 'cfcd208495d565ef66e7dff9f98764da'
        """
        res = hashlib.md5(str(self.generator.random.random()).encode('utf-8'))
        if raw_output:
            return res.digest()
        return res.hexdigest()

    def sha1(self, raw_output=False):
        """
        Calculates the sha1 hash of a given string
        :example 'b5d86317c2a144cd04d0d7c03b2b02666fafadf2'
        """
        res = hashlib.sha1(str(self.generator.random.random()).encode('utf-8'))
        if raw_output:
            return res.digest()
        return res.hexdigest()

    def sha256(self, raw_output=False):
        """
        Calculates the sha256 hash of a given string
        :example '85086017559ccc40638fcde2fecaf295e0de7ca51b7517b6aebeaaf75b4d4654'
        """
        res = hashlib.sha256(
            str(self.generator.random.random()).encode('utf-8'))
        if raw_output:
            return res.digest()
        return res.hexdigest()

    def locale(self):
        language_code = self.language_code()
        return language_code + '_' + self.random_element(
            Provider.language_locale_codes[language_code]
        )

    def language_code(self):
        return self.random_element(Provider.language_locale_codes.keys())

    def uuid4(self):
        """
        Generates a random UUID4 string.
        """
        # Based on http://stackoverflow.com/q/41186818
        return str(uuid.UUID(int=self.generator.random.getrandbits(128)))

    def password(
            self,
            length=10,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True):
        """
        Generates a random password.
        @param length: Integer. Length of a password
        @param special_chars: Boolean. Whether to use special characters !@#$%^&*()_+
        @param digits: Boolean. Whether to use digits
        @param upper_case: Boolean. Whether to use upper letters
        @param lower_case: Boolean. Whether to use lower letters
        @return: String. Random password
        """
        choices = ""
        required_tokens = []
        if special_chars:
            required_tokens.append(
                self.generator.random.choice("!@#$%^&*()_+"))
            choices += "!@#$%^&*()_+"
        if digits:
            required_tokens.append(self.generator.random.choice(string.digits))
            choices += string.digits
        if upper_case:
            required_tokens.append(
                self.generator.random.choice(string.ascii_uppercase))
            choices += string.ascii_uppercase
        if lower_case:
            required_tokens.append(
                self.generator.random.choice(string.ascii_lowercase))
            choices += string.ascii_lowercase

        assert len(
            required_tokens) <= length, "Required length is shorter than required characters"

        # Generate a first version of the password
        chars = [self.generator.random.choice(choices) for x in range(length)]

        # Pick some unique locations
        random_indexes = set()
        while len(random_indexes) < len(required_tokens):
            random_indexes.add(
                self.generator.random.randint(0, len(chars) - 1))

        # Replace them with the required characters
        for i, index in enumerate(random_indexes):
            chars[index] = required_tokens[i]

        return ''.join(chars)
