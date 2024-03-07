import random
import json

# firstnames=['Alexandre','Hafida','Valentin','Sandro','Marina','Coraline','Fred','Christopher','Florent','Anthony','Adrien']
with open("pickme.json", "r") as rf:
    remove_firstnames = json.load(rf)

with open("pickme_extend.json", "r") as rf:
    extend_firstnames = json.load(rf)

if remove_firstnames == [] and len(extend_firstnames) == 11 :
    remove_firstnames = extend_firstnames.copy()
    extend_firstnames.clear()

pick_firstname=random.choice(remove_firstnames)
print(pick_firstname)

remove_firstnames.remove(pick_firstname)
extend_firstnames.insert(0,pick_firstname)
print(remove_firstnames)

with open("pickme_remove.json","w") as f:
    json.dump(remove_firstnames, f)

with open("pickme_extend.json","w") as f:
    json.dump(extend_firstnames, f)
