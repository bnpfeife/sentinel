import os.path

def build_keys(modified):
    '''
    '''
    # Iterate through each of the keys within the modified list and split
    # the extension from the path. The extension-less path replaces the
    # key used within the modified list. This identifies corresponding
    # destination files.
    return { os.path.splitext(_object[0])[0]:(_object[0], _object[1])
        for _object in modified }


def detect_missing(src, dst):
    '''
    '''
    return { k:v for (k,v) in src.items() if not k in dst }

def detect_modified(interval, src, cached):
    '''
    '''
    return { k:v for (k,v) in src.items()
        if k in cached and cached[k][1] + interval < v[1] }
