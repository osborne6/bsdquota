
"python wrapper for NetBSD's quota program"

__version__ = '0.1'
__author__ = 'John Osborne'

import re

def return_non_empty(txt_list):
    "remove empty elements"
    newlist = list()
    for l in txt_list:
        if l is not '':
            newlist.append(l)
    return newlist


def stats_list_to_dict(statlist):
    "Assumes we don't have a listed grace period in the quota output; quota at sdf doesn't seem to"
    head = [ 'blocks', 'b_quota', 'b_limit', 'files', 'f_quota', 'f_limit' ]
    newdict = dict()
    for k, v in zip(head, statlist):
        newdict[k] = v
    return newdict

def exec_quota():
    pass


def parse_quote_output(quota_file_name):
    "This could use some fixing up"
    f = open(quota_file_name,'rb')
    lines = f.readlines()
    f.close()

    lines = [ l[:-1] for l in lines ]
    header = list()
    fs_list = list()
    stats_list = list()
    quota_title = None

    for l in lines:
        if re.search(r'  File', l):
            head_tmp = re.sub(r'( ){1,}', '\t', l)
            header = return_non_empty( head_tmp.split('\t') )
        elif re.search(r'^/', l):
            fs_list.append(l)
        elif re.search(r'^Disk',l):
            quota_title = l
        else:
            stat_tmp = re.sub(r'( ){1,}','\t', l)
            stats_list.append( stats_list_to_dict( return_non_empty(stat_tmp.split('\t') ) ) )

    quota_struct = dict()
    for fsi in range(0,len(fs_list)):
        quota_struct[ fs_list[fsi] ] = stats_list[fsi]

    return quota_struct


if __name__ == "__main__":
    import sys
    print parse_quote_output(sys.argv[1])

