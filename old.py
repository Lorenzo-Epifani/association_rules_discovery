import pandas as pd # type: ignore
import datetime, time
import json
Date_t = datetime.date
import functools
from typing import List, Set, Dict, Union, Any, Callable, Tuple
from dataclasses import dataclass
import uuid
uuid_gen=uuid.uuid4
Uuid_t = uuid.UUID


######################################
df = pd.read_csv ('dataset.csv')
#receipt=Dict[str,Union[str,Set,Date]]
######################################

@dataclass
class Receipt:
    _iid: Uuid_t
    _items: List[str]
    _time: Date_t
    _weekend: bool


##############################################################################
######
######  print(row.index.tolist())
######
######  DF ROW STRUCTURE
######  ['Transaction', 'Item', 'date_time', 'period_day', 'weekday_weekend']
######
##############################################################################


def store_merge(df_rows:List[Any],itemset: List[Receipt]) -> None:
    '''
    merge given "df_rows" in an itemset, then add the and it them in the "itemset" list
    ''' 
    iid =uuid_gen()
    time: Date_t = df_rows[0]['date_time']
    weekend: bool = True if df_rows[0]['weekday_weekend']=='weekend' else False
    items:List[str] = [] 
    for row in df_rows:
        items.append(row['Item'])
    receipt:Receipt=Receipt(iid,items,time,weekend)
    itemset.append(receipt)






#####init
temp_row_list:List[Any]=[]
my_itemset:List[Receipt]=[]
flag:bool=True
temp_time:int=0
#########


#####Handler
def same(_row:Any)->None:
    global temp_row_list
    temp_row_list.append(_row)


def different(_row:Any)->None:
    global temp_row_list,my_itemset
    store_merge(temp_row_list,my_itemset)
    temp_row_list=[_row]
    pass

handler:Dict[bool,Callable]={
    True: same,
    False: different
}
##########

for index, row in df.iterrows():
    new_date:Date_t = datetime.datetime.strptime(row.date_time, '%d-%m-%Y %H:%M')
    row.date_time = int(time.mktime(new_date.timetuple()))
    flag= True if (abs(temp_time-row.date_time)<=60 or len(temp_row_list)==0) else False
    handler[flag](row)
    temp_time=temp_row_list[-1].date_time

new_df=pd.DataFrame(my_itemset)

new_df.to_csv('file_name.csv', index=False)