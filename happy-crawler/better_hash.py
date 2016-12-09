def hash_string(keyword, buckets):
    h = 0
    for c in keyword:
        h = (h + ord(c)) % buckets
    return h

def make_hashtable(nbuckets):
    table = []
    for unused in range(0, nbuckets):
        table.append([])
    return table
    #[[]] * nbuckets is wrong

def hashtable_get_bucket(htable, key):
    return htable[hash_string(key, len(htable))]

def hashtable_add(htable,key,value):
    return hashtable_get_bucket(htable, key).append([key, value]) 

def hashtable_lookup(htable,key):
    bucket = hashtable_get_bucket(htable, key)
    for entry in bucket:
        if entry[0] == key:
            return entry[1]
    return None

def hashtable_update(htable,key,value):
    bucket = hashtable_get_bucket(htable, key)
    for entry in bucket:
        if entry[0] == key:
            entry[1] = value
            return htable
    bucket.append([key, value])
    return htable