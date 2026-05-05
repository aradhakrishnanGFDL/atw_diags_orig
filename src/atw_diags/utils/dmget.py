#for simple dmget usage, just use this !dmget {file}
#use following to wrap the dmget call for each path in the catalog
import os

def dmgetmagic(x):
    cmd = 'dmget %s'% str(x) 
    return os.system(cmd)

#usage dmstatus = cat.df["path"].apply(dmgetmagic)