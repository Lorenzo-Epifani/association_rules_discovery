import pandas as pd # type: ignore
import datetime, time
Date_t = datetime.date
import functools
import uuid
uuid_gen=uuid.uuid4
from typing import List, Set, Dict, Union, Any, Callable, Tuple

####################################################################################
######                                                                        ######  
######  print(row.index.tolist())                                             ######
######                                                                        ######  
######  DF ROW STRUCTURE                                                      ######
######  ['Transaction', 'Item', 'date_time', 'period_day', 'weekday_weekend'] ######
######                                                                        ######  
####################################################################################

def str_date_to_sec(string_date:str)-> int:
    return int(time.mktime(datetime.datetime.strptime(string_date, '%d-%m-%Y %H:%M').timetuple()))


def reducer(x,y)->List[Any]:
    y.date_time = str_date_to_sec(y.date_time)
    y.Transaction = uuid_gen()
    y.Item = {y.Item}

    if len(x)==0:
        return [y]

    if abs(x[-1].date_time-y.date_time) <= 60:   #same
        x[-1].date_time = y.date_time
        x[-1].Item = x[-1].Item.union(y.Item)

    else:   #different
        x.append(y)
    return x
        
def make_basket_list(in_file:str,out_file:str)-> Tuple[Set[str], List[Any]]:

    df:Any = pd.read_csv(f'{in_file}')
    rows: List[Any] = []
    my_item_universe: Set[str] = set()

    for index,row in df.iterrows():
        rows.append(row)
        my_item_universe.add(row.Item)

    my_basket_list:List[Any]=functools.reduce(reducer,rows,[])

    new_df=pd.DataFrame(my_basket_list)
    new_df.to_csv(f'{out_file}', index=False)

    return (my_item_universe, my_basket_list)