# -*- encoding: utf-8 -*-

from unittest import TestCase

import htmlentities


class DecodingTestCase(TestCase):

    def test_should_decode_basic_entities(self):
        self.assertEqual('&', htmlentities.decode('&amp;'))
        self.assertEqual('"', htmlentities.decode('&quot;'))
        self.assertEqual('<', htmlentities.decode('&lt;'))

    def test_should_decode_utf8_accents(self):
        self.assertEqual(u'é', htmlentities.decode('&eacute;'))
        self.assertEqual(u'ê', htmlentities.decode('&ecirc;'))

    def test_decode_complex_unicode_text(self):
        """This test fails because the regular expression does not recognize U&"""
        text = u"Übergroße Äpfel mit Würmern"

        # result string: &Uuml;bergro&szlig;e &Auml;pfel mit W&uuml;rmern

        result = htmlentities.decode(htmlentities.encode(text))

        self.assertEquals(result, text)
