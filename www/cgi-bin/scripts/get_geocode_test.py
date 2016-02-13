#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib
from xml.etree.ElementTree import parse

def adr2geo(adr):
    latlng = []
    api = "http://www.geocoding.jp/api/?v=1.1&q=%s" % (urllib.quote(adr.encode('utf-8')))
    xml = parse(urllib.urlopen(api)).getroot()

    lat = xml.find('coordinate/lat').text
    lng = xml.find('coordinate/lng').text
    latlng = [lat, lng]
    return latlng

def main():
    print adr2geo(u'大津市')

if __name__ == '__main__':
    main()
