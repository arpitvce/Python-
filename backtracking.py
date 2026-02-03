def permut(s,used,path):
    if len(s)==len(path):
        print("".join(path))
        return
    for i in range(len(s)):
        if used[i]:
            continue
        used[i]=True
        path.append(s[i])
        permut(s,used,path)
        path.pop()
        used[i]=False
permut("ABCD",[False]*len("ABCD"),[])

