# -*- coding: utf-8 -*-

### py_messenger
### GNU/GPL v2
### Author: Cody Rocker
### Author_email: cody.rocker.83@gmail.com
### 2016
#-----------------------------------
#   Requires:                    """
#    - Python 3                  """
#-----------------------------------
import os

from xml.etree.ElementTree import parse

class Carrier(object):

    def __init__(self, xml_element):
        self.network = xml_element.attrib["name"]
        self.sms = xml_element.findtext("SmsExchange")
        self.mms = xml_element.findtext("MmsExchange")

class CarrierExchange(object):
    """ Load a list of email exchange servers from an xml file
        to generate a lookup table (dict) of Carrier objects
    """

    def __init__(self):
        ## TODO: make this available in user directory
        self.carrier_list_xml = "data/carriers.xml"  # Location of carrier list inside package
        self.carriers = self.parse_carrier_list(self.load_carrier_xml())

    def load_carrier_xml(self):
        """ Return a list of xml 'Carrier' elements
            to be parsed into Carrier objects
        """
        path = os.path.abspath(__file__)
        dir_path = os.path.dirname(os.path.dirname(path))
        self.data_path = os.path.join(dir_path, self.carrier_list_xml)
        with open(self.data_path) as f:
            doc = parse(f)
        return [x for x in doc.findall('Carrier')]

    def parse_carrier_list(self, carrier_elements):
        """ Return a dictionary of Carrier objects can be referenced
            by the xml element Carrier name attribute.
        """
        carriers = {}
        for element in carrier_elements:
            carrier = Carrier(element)
            carriers[carrier.network] = carrier
        return carriers
