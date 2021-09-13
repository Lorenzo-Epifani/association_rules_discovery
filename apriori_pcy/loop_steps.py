from typing import List, Set, Dict, Union, Any, Callable, Tuple
from pprint import pprint
from rules_maker import rules_maker as _rm
from apriori_pcy.utils import my_hash,check_frequent
import config.data as conf


def step_3_generate(summary:Dict[int,Dict[str,Any]],bask_list:List[Any],rem_steps:int)->None:
    new_candidate_itemsets:Dict[int,Set[str]]
    new_candidate_itemsets = {my_hash(val):val for val in [v1['itemset'].union(v2['itemset'])  for v1 in summary.values()  for v2 in summary.values() if (len(v1['itemset']) +1 == len(v1['itemset'].union(v2['itemset'])))]}
    pprint('#########NEW CANDIDATES: #########')
    print(new_candidate_itemsets)
    step_2_filter(new_candidate_itemsets,bask_list,rem_steps-1)

def step_2_filter(candidate_itemsets:Dict[int,Set[str]], bask_list:List[Any],rem_passes:int)->None:
    summary:Dict[int,Dict[str,Any]]
    summary=dict()
    freq_th = 1/len(candidate_itemsets) if conf.auto == True else conf.freq_th
    limit:int=0
    pprint(f'########## REMAINING PASSES(s): {rem_passes}##########')
    pprint(f'########## F THRESHOLD: {freq_th}##########')
    summary={key:record for key,record in {key:check_frequent(itemset,bask_list) for key,itemset in candidate_itemsets.items()}.items() if record.get('is_frequent',False)}
    pprint('######### SUMMARY #########')
    pprint(summary)
    if rem_passes == 0:
        pprint(f'########## RULES DISCOVERY... ##########')
        _rm.find_rules(summary,bask_list)
        pprint(f'########## DONE ##########')
    else:
        step_3_generate(summary,bask_list,rem_passes)