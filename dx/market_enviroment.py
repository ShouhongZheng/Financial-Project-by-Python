# -*- coding: utf-8 -*-
"""


@author: HP
target:iniating the marketing arguments need to be evaluated
"""
class market_enviroment(object):
    def __init__(self,name,pricing_date):
        self.name=name
        self.pricing_date=pricing_date
        self.constants={}
        self.lists={}
        self.curves={}
    
    def add_constant(self,name,constant):
        self.constants[name]=constant
    def get_constant(self,key):
        return self.constants[key]
    def add_list(self,key,list_object):
        self.lists[key]=list_object
    def get_list(self,key):
        return self.lists[key]
    def add_curve(self,key,curve):
        self.curves[key]=curve
        
    def get_curve(self,key):
        return self.curves[key]
    def add_enviroment(self,env):
        for key in env.constants:
            self.constants[key]=env.constants[key]
        for key in env.lists:
            self.lists[key]=env.lists[key]
        for key in env.curves:
            self.curves[key]=env.curves[key]
