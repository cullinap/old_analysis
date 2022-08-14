#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from dateutil import rrule
from datetime import datetime, timedelta


# In[2]:


class DataLoad:
    
    """
    Allows you to upload the detailed cost report and perform a varity of operations 
    
    Load data (processes the data):
    1. input data as such: data = DataLoad('X-XX-XXX_mon.xls')
    2. to view the data: data.load_data().head()
    
    Burn rate
    """
    
    
    def __init__(self, file_name, labor_type=None, start_date=None, end_date=None, code=None):
        self.data = file_name
        self.labor_type = labor_type
        self.start_date = start_date
        self.end_date = end_date
        self.code = code
       
    def load_data(self):
        DATA_PATH = os.path.join(os.getcwd(),'data')
        data = pd.read_excel(os.path.join(DATA_PATH, self.data))
        new_index = data.reset_index()
        new_header = new_index.iloc[1] #identify a new header
        new_data = new_index[2:] #chop off top two rows
        new_data_index = new_data.reset_index(drop=True) #reset again
        new_data_clean = new_data_index.fillna('') #drop nan
        new_data_clean.columns = new_header

        return new_data_clean
    
    def burn_rate(self):
        data = self.load_data()
        descrip_1 = data['Description'].iloc[:,0] #reconfigure description 1
        descrip_2 = data['Description'].iloc[:,1] #reconfigure description 2
        df_d      = data[(data['Stamp'] > self.start_date)                        & (data['Stamp'] <= self.end_date)] #set the date range
        df_d1c    = df_d.groupby(descrip_2)['Amount'].sum() #groupby & sum by value

        return df_d1c.reindex(self.labor_type) #return groupset
        return df_d1c.reindex(self.labor_type).sum() #returns sum of groupset
    
    def total_cost(self):
        data = self.load_data()
        df_d = data[(data['Stamp'] > self.start_date)                        & (data['Stamp'] <= self.end_date)]
        total = df_d['Amount'].sum()
        #total = data['Amount'].sum()
        return total
    
    def tot_costcode(self):
        data = self.load_data()
        grouped = data.groupby('Extra')['Amount'].sum()
        return grouped
        


# In[21]:


#various labor combinations 
carpenters = ['Carpenter Foreman', 'Carpenter', 'Dockbuilder', 'Timberman']
laborers = ['Labor Foreman', 'Laborer']
operators  = ['Operator']
pipe_fit   = ['Pipeliner']
just_labor = ['Carpenter Foreman', 'Carpenter', 'Dockbuilder', 'Timberman',                          'Labor Foreman', 'Laborer', 'Operator', 'Pipeliner']
all_labor  = ['Carpenter Foreman', 'Carpenter', 'Dockbuilder', 'Timberman',                          'Labor Foreman', 'Laborer', 'Operator', 'Pipeliner',                             'Superintendent', 'Project Manager', 'Project Engineer',                                 'Field Engineer', 'Senior Project Manager', 'Sr Project Manager',                                     'Asst Project Manager', 'Project Analyst']


# In[17]:


class CostAnalyzer:
    
    def __init__(self, file_name, labor_type=None, start_date=None, end_date=None, code=None, overhead=None):
        self.data = file_name
        self.labor_type = labor_type
        self.start_date = start_date
        self.end_date = end_date
        self.code = code
        self.overhead = overhead
        
    def load_data_mob(self):
        DATA_PATH = os.path.join(os.getcwd(),'data')
        data = pd.read_excel(os.path.join(DATA_PATH, self.data))
        new_index = data.reset_index()
        new_header = new_index.iloc[0]
        new_data = new_index[1:]
        new_data_index = new_data.reset_index(drop=True)
        new_data_clean = new_data_index.fillna('')
        new_data_clean.columns = new_header
        new_data_clean.columns.values[5] = "Foreman"
        new_data_clean.columns.values[2] = 'Name'
        new_data_clean.columns.values[6] = 'ST'
        new_data_clean.columns.values[3] = 'Date'
        #new_data_clean.columns.values[4] = 'Craft'
        
        return new_data_clean
    
    def manhour_rpt(self):
        data    = self.load_data_mob()
        job     = data['Code'].iloc[:,1] #identify the job
        st_tot  = data['ST'].sum()
        ot_tot  = data['OT'].sum()
        ot2_tot = data['2nd OT'].sum()
        total   = st_tot + ot_tot + ot2_tot
        man_cnt = len(data['Name'].unique())
        
        if self.overhead is None:
            overhead = int(input('How much overhead?'))
            total_oh = int(overhead) * 50
            
        total   = total_oh + total
        man_cnt = overhead + man_cnt
        
        d = {'BOND': [total, man_cnt]}
        mh_rpt = pd.DataFrame.from_dict(d, orient='index', columns=['Hours', 'count'])
        
        return mh_rpt
    
    def burn_rpt(self, st=None, ot=None, craft_cost=None, total=None):
        data   = self.load_data_mob()
        data.columns = ['#','Code', 'Name', 'Date', 'Craft', 'Foreman', 'ST', 'OT', '2nd OT', 'Cost']
        
        if st is not None:
            return data.groupby('Craft')['ST'].sum()
            
        if ot is not None:
            return data.groupby('Craft')['OT'].sum()
        
        if craft_cost is not None:
            return data.groupby('Craft')['Cost'].sum()
    


# In[ ]:




