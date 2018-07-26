# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

sec_para_split_list = [[12,'P','1000-PARA',1,58,75],[12,'P','1001-PARA',2,76,152],[12,'S','1003-SEC',3,153,225],[12,'P','1004-PARA',4,226,300]]
perflist =[[12,'1000-PARA','P','1001-PARA',70],[12,'1004-PARA','P','1003-SEC',265]]



#para_sec_id_lookup(sec_para_split_list,perflist)

import sys
import time
import json
import datetime
import pandas as pd

try:   
    print(sys.argv[1])
	config = read.json(sys.argv[1])
	print(config["Config-files"]["source-path"])
    for perform in perflist:
        
        for sec_para in sec_para_split_list:
            if (sec_para[2] == perform[1]):
                perform[1] = sec_para[3]
                     
            if (sec_para[2] == perform[3]):
                perform[3] = sec_para[3]
                perform[2] = sec_para[1]
                ts = time.time()
                print(ts)
                st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
                print(st)
                perform.append(st)
    df = pd.DataFrame(perflist,columns=(['pgm-id','parent-node','child-type','child-node','trigger-line','timestamp']))
	
except IndexError:
    pass
    
finally:
#    print(perflist)            
     print(df)
	
    