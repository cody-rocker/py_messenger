import os

from nose.tools import eq_

class TestCarrierExchange(object):

    def test_load_carrier_xml(self):
        # setup the test
        from messenger.carrier_exchange import CarrierExchange
        exchange = CarrierExchange()
        # run the test
        carrier_elements = exchange.load_carrier_xml()
        assert len(carrier_elements) > 0
        eq_(os.path.exists(exchange.data_path), True)
        eq_(carrier_elements[0].attrib["name"], 'Test')
        eq_(carrier_elements[0].findtext("SmsExchange"), 'txt.test.com')
        eq_(carrier_elements[0].findtext("MmsExchange"), 'mms.test.com')

    def test_parse_carrier_list(self):
        # setup the test
        from messenger.carrier_exchange import CarrierExchange
        exchange = CarrierExchange()
        # run the test
        carrier_elements = exchange.load_carrier_xml()
        carrier_list = exchange.parse_carrier_list(carrier_elements)
        assert len(carrier_list) > 0
        assert 'Test' in carrier_list.keys()
        eq_(carrier_list['Test'].network, 'Test')
        eq_(carrier_list['Test'].sms, 'txt.test.com')
        eq_(carrier_list['Test'].mms, 'mms.test.com')

