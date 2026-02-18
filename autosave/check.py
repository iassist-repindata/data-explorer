import pandas as pd
import re

# open the file as bytes and check for rogue line breaks

with open("file.tsv", "r+b") as file:
    f = file.read()
    #print(f)
    match2rn = len(re.findall(b"\r\n\r\n",f))
    print(match2rn)
    if match2rn > 0:
        f = f.replace(b"\r\n\r\n",b"\r\n")
    else:
        pass
    match = len(re.findall(b"\r\n",f))
    matchn = len(re.findall(b"\n",f))
    matchr = len(re.findall(b"\r",f))
    # print(match, matchn, matchr)
    if match < matchn:
        f = f.replace(b"\n",b"") 
        matchr = len(re.findall(b"\r",f))
    

    elif matchr > match:
        f = f.replace(b"\r",b"")

    else: 
        pass
    
    f = f.decode("utf8")