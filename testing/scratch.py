from ixml import XmlProcessor

import xml.etree.ElementTree as ET

with open('status.xml') as f:
    ixml = ET.fromstring(f.read())

a = XmlProcessor.get_role(ixml, "Input")