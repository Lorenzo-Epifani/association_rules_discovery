from typing import List, Set, Dict, Union, Any, Callable, Tuple
import hashlib
import functools 
import re
import config.data as conf

def check_frequent(itemset:Set[str],bask_list:List[Any])->Dict[str,Any]:
    record:Dict[str,Any]
    
    support:int = get_support(itemset,bask_list)
    record = {
        'itemset':itemset,
        'is_frequent': True if support/len(bask_list)>=conf.freq_th else False,
        'frequency':support/len(bask_list),
        'support':support
    }
    
    return record


def my_hash(toHash:Any,mod:int=0)->int:
    tostring:str=f'{toHash}{type(toHash)}'
    hash_object = hashlib.md5(tostring.encode())
    digest:str = hash_object.hexdigest()
    chunked_hash=re.findall(r"(..)",digest)
    int_list=[int(elem,16) for elem in chunked_hash]
    result:int = functools.reduce((lambda x, y: 2*x + 3*y),int_list) 

    return result if mod<=0 else result%mod

def get_support(itemset:Set[str],bask_list:List[Any])->int:
    #mette una serie di true (presente nel basket) o false (non) in una lista per ogni 
    #elemento di itemset. se in questa lista sono tutti true(all()) mette 'placeholder' nella lista padre.
    #procedura ripetuta per ogni basket in bask_list.(quindi conto quanti basket contengono tutti gli item di itemset)
    support:int = len(['placeholder' for basket in bask_list if all([ True if item in basket.Item else False for item in itemset])])
    return support