import generator
from dataclasses import dataclass
import apriori_pcy.init_step # type: ignore
from typing import List, Set, Dict, Union, Any, Callable, Tuple
import config.data as conf

print('INPUT FILENAME --####')
print(f'{conf.i_name} --->\n')

print('OUTPUT FILENAME --####')
print(f'{conf.o_name} <---\n')

print('FREQUENCY MODE --####')
print(f'{"Dynamic" if conf.auto else "Static"}\n')

print('FREQUENCY TH --####')
print(f'{conf.freq_th}\n')

print('Confidence TH --####')
print(f'{conf.conf_th}\n')

print('PASSES --####')
print(f'{conf.passes}')

print('Building baskets list...')
try:
    result:Tuple[Set[str], List[Any]]
    result = generator.make_basket_list(conf.i_name,conf.o_name)
except Exception as  e :
    print('An error occured while building the baskets list')
else:
    print(f'Basket list ---> {conf.o_name} ok')
    print('Done!')
    
apriori_pcy.init_step.initialize(*result)
