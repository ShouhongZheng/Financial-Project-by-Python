# -*- coding: utf-8 -*-
"""
Created on Sat May 11 23:03:50 2019

@author: HP
"""

import numpy as np
def get_year_deltas(date_list,day_count=365.25):
    start=date_list[0]
    delta_list=[(date-start)/day_count for date in date_list]
    return np.array(delta_list)