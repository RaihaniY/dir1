import os

def search(fname, path):
    'return the (first found) location of fname in path or None if it is not there'
    for item in os.listdir(path):
        fullItem = os.path.join(path, item)
        if os.path.isdir(fullItem):
            ans = search(fname, fullItem)
            if ans != None: 
                return ans
        elif item.lower() == fname.lower():
            return fullItem


def countFiles(path):
    'return the number of files found inside of path'
    count = 0
    for item in os.listdir(path):
        fullItem = os.path.join(path, item)
        if os.path.isdir(fullItem):
            val = countFiles(fullItem)
            count += val
        else: 
            count += 1
    return count

rules={} #Add whatever you are searching for in here

def scan(pathname, signatures):
    '''recursively scans all files contained, directly or
       indirectly, in the folder pathname'''
    for item in os.listdir(pathname): 
        if item[0] != '.': 
            fullItem = os.path.join(pathname, item) 
            if os.path.isdir(fullItem): 
                scan(fullItem, signatures) 
            elif os.path.isfile(fullItem): 
                f = open(fullItem, 'r') 
                s = f.read()
                for virus in signatures:
                    if s.find(signatures[virus]) >= 0:
                        print(f'{fullItem}, found virus {virus}')
                f.close()

