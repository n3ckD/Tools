#!/usr/bin/python

# Description
# Simple script to read list of miners from SANS API (https://isc.sans.edu/api/threatlist/miner/)

from datetime import date, timedelta
import requests as req
import xml.etree.ElementTree as ET

# Return the isoformat dates from 'd' days back until today
# Returns: YYYY-MM-DD, YYYY-MM-DD
def getDates(d = 0):
    date1 = (date.today() - timedelta(days = d)).isoformat()
    date2 = date.today().isoformat()
    return date1, date2

# Retrieve the XML from the threatfeed between date1 and date2
# Returns: XML data as a string
def getXML(feed, date1, date2):
    feed, date1, date2 = feed, date1, date2
    print "Processing for dates %s to %s." % (date1, date2)

    xml_data = req.get('https://isc.sans.edu/api/threatlist/'+feed+'/'+date1+'/'+date2+'/')
    return xml_data.text

# Parse XML data to retrieve relevant information
# Returns: List of lists containing ip, firstseen, lastseen
def parseXML(xml_data):
    xmlList = []
    tree = ET.XML(xml_data)
    for child in tree.iter(tag='miner'):
       entry = [child[0].text, child[1].text, child[2].text]
       xmlList.append(entry)
    return xmlList

# Formats feed data for printing
# Prints: Feed information as string
def printFeed(feed_data):
    feed_data = feed_data
    for miner in feed_data:
        print "IP: %s\tFirstSeen: %s\tLastSeen: %s" % (miner[0], miner[1], miner[2])
    print "List contains %s entries" % (len(feed_data))

if __name__ == '__main__':
    days_back = 14
    feed = 'miner'
    xml_data = getXML(feed, *(getDates(days_back)))
    feed_data = parseXML(xml_data)
    printFeed(feed_data)
