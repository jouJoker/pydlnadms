from unittest import TestCase

class PydlnadmsTest(TestCase):
    def test_etree(self):
        import xml.etree.ElementTree as etree
        a = etree.Element('hi')
        self.assertEqual(type(etree.tostring(a)), str)
