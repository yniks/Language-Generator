def PrimitiveParse(string):
    lines=string.split('\n')
    defs=list(map(lambda l:l.split("::="),lines))
    mp=dict()
    for dif in defs:
        if dif[0] in mp:mp[dif[0]].extend(dif[1].split("|"))
        else :mp[dif[0]]=dif[1].split("|")
    return mp