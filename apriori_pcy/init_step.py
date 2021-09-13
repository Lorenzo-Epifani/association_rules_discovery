from typing import List, Set, Dict, Union, Any, Callable, Tuple
import config.data as conf
from apriori_pcy.loop_steps import step_2_filter
from apriori_pcy.utils import my_hash 


def initialize(item_univ:Set[str], bask_list:List[Any])->None:
    dict_hash_item:Dict[int,Set[str]]
    dict_hash_item = {my_hash({item}):{item} for item in item_univ}    
    step_2_filter(dict_hash_item,bask_list,conf.passes)