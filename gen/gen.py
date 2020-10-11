import re 
import unicodedata

"""
Reads in taigi_pojhanlo.dict.yaml and removes all lines
with Chinese characters or capital letters. 

Resources: 
- https://github.com/rime/home/wiki/CustomizationGuide
- https://github.com/rime/home/wiki/RimeWithSchemata
- https://github.com/LEOYoon-Tsaw/Rime_collections/blob/master/Rime_description.md
"""
with open('taigi_pojhanlo.dict.yaml') as f: 
    with open('taigi_poj.dict.yaml', 'w') as output: 
        output.write(
"""# Rime dictionary
# encoding: utf-8
#
# Taigi POJ
#
#   William Pan <wpan@berkeley.edu>
#

---
name: taigi_poj
version: "2020.10.03"
sort: by_weight
use_preset_vocabulary: false
...
    
""") 
        for line in f: 
            if not re.search('[\u4e00-\u9fff]', line): 
                output.write(line)