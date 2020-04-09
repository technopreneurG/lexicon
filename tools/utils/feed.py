import yaml
import os

#read-feeds: read files from the given path and convert to python dictionary
#usage: read_feeds('./lexicon-xyz/data/')
def read_feeds(path):
    i=0
    l = []
    for entry in sorted(os.scandir(path), key=lambda x: (x.name)):
        if not entry.name.startswith('.') and entry.is_file() and entry.name.endswith('.yml'):
            print(f"Processing: {entry.name}")
            data = yaml.load(open(path + entry.name, 'r'), Loader=yaml.FullLoader) #todo: handle : in the value
            l.append(data['lexicon'])
    return l

