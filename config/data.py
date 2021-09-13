import json
from typing import List, Set, Dict, Union, Any, Callable, Tuple
import cerberus as cer # type: ignore
import json
from operator import itemgetter

def _init()->Dict[str,Dict[str,str]]:
    with open('./config/config.json') as config_file:
        conf = json.load(config_file)
    def add_prop(value):
        value['required']= True
        return value
        
    schema:Dict[str,Dict[str,str]] = {
        "i_name":{
            'type': 'string'
            },
        "o_name":{
            'type': 'string'
            },
        "freq_th":{
            'type': 'float'
            },
        "conf_th":{
            'type': 'float'
            },
        "auto":{
            'type': 'boolean'
            },
        "passes":{
            'type': 'integer'
            }
    }
    schema = {k:add_prop(v)  for (k,v) in schema.items()}
    v = cer.Validator()
    if not v.validate(conf, schema):
        print("Config is not valid")
        exit()
    return conf

i_name, o_name, freq_th, conf_th, auto, passes = itemgetter("i_name", "o_name","freq_th","conf_th", "auto", "passes")(_init())
