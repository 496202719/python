
import time
import os 
import pandas as pd 
import json
import demjson
from pandas.io.json import json_normalize


class Writexls():

    def __init__(self,folder:str):
        self.folder = input('请输入文件夹名:');
        # if not self.folder:
        #     self.folder =  time.strftime("%Y-%m-%d",time.localtime())
        print(f'目标文件为 : {self.folder}') ;
    def get_data_list(self):
        names_list = os.listdir(self.folder);
        print(f'获取 {self.folder} 文件夹下 {len(names_list)} 个文件');
        return names_list;
    def get_data(self):
        names_list=self.get_data_list();
        for name in names_list:
            data_str = open(f'{self.folder}/{name}',encoding = 'utf8').read();
            s=data_str.replace('10.3.184.${v_ip}','10.3.184.${IP}')\
            .replace('manage_org_code','managecom_org_code');
       
            with open(f'{self.folder}/{name}', 'w+',encoding = 'utf8') as f:
                
                f.write(s);

            # list=pd.read_json(data_str)
            # list= json.load(data_str)
            # str = f.readline()
            
            
        
if __name__ == '__main__':
    start=Writexls(None);
    start.get_data();
