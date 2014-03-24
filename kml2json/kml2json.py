#!/usr/bin/env python
# -*- coding: utf-8 -*-
from lxml import etree, objectify

class kmlobject(object):
   def __init__(self, kmlfile):
      self.kmlfile = kmlfile
      self.root = self.__get_root()

   def __get_root(self):
      """ Get the root of the KML object """
      with open(self.kmlfile) as kmlfile:
         return self.parse(kmlfile).getroot()

   def parse(self,fileobject,  schema=None): 
       """Parses a file object 
       This function parses a KML file object, and optionally validates it against 
       a provided schema. """ 
       if schema: 
           # with validation 
           parser = objectify.makeparser(schema = schema.schema, strip_cdata=False) 
           return objectify.parse(fileobject, parser=parser) 
       else: 
           # without validation 
           return objectify.parse(fileobject)
