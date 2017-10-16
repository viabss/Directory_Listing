# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:49:50 2017

@author: Saurav.Bhattacharyya
"""
import os
import pandas as pd
import xlwt
from tempfile import TemporaryFile
book = xlwt.Workbook()
sheet1 = book.add_sheet('List')
drive = 'I:\\'
subFolder_1 = 'General'
subFolder_2 = 'ManufacturerExtraction'
subFolder_3 = 'Spec'
subFolder_3_output = 'TEST_999'

files= []
paths = os.path.join(drive,subFolder_1,subFolder_2,subFolder_3,subFolder_3_output)
files = os.listdir(paths)

for i,e in enumerate(files):
    sheet1.write(i,1,e)

output_file = 'List.xlx'
book.save(os.path.join(paths,output_file))
