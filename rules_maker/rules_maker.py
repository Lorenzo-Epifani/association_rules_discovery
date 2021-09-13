from typing import List, Set, Dict, Union, Any, Callable, Tuple
import config.data as conf
from itertools import chain, combinations
from apriori_pcy.utils import get_support
from pprint import pprint
import pandas as pd # type: ignore

def get_subsets(summary_entry:Dict[str,Any],bask_list:List[Any]):
    itemset = summary_entry['itemset']
    support_supset = summary_entry['support']
    s = list(itemset)
    return [
                {
                    "if_a":set(subs),
                    "then_b":itemset.difference(set(subs),),
                    "confidence":support_supset/get_support(set(subs),bask_list)
                } 
                for subs in chain.from_iterable(combinations(s, r) 
                for r in range(len(s)+1))
            ][1:-1]


def find_rules(summary:Dict[int,Dict[str,Any]],bask_list:List[Any])->None:
    result:List[Dict[str,Any]] = []
    for entry in summary.values():
        result = [*result,*get_subsets(entry,bask_list)]

    df = pd.DataFrame(result)
    df.to_csv(f'Association_Rules.csv', index=False)
    