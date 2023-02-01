import re

def extract_matches(list:list(), pattern:str): 
    matchlist = [
            element for element in list if re.search(
                pattern,
                element,
                flags=re.IGNORECASE
            )
    ]
    return matchlist
