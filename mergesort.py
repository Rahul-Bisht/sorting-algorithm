iAr=[7,5,3,9,12,11,20,30,50,40,1000,60,70]


  
def merge(l,r):
    out=[]
    while(len(l)!=0 and len(r)!=0):
        if(l[0]>r[0]):
            out.append(r[0])
            r.remove(r[0])
        else:
            out.append(l[0])
            l.remove(l[0])
        
    while(len(l)!=0):
            out.append(l[0])
            l.remove(l[0])
    while(len(r)!=0):
            out.append(r[0])
            r.remove(r[0])
    print(out)
    return out
   
def sort(alist):
    max=len(alist)   
    if(max==1):
        return alist
    offset=0
    
    mid=(offset+max)//2

    l=alist[:mid]
    r=alist[mid:]
    l=sort(l)
    r=sort(r)
    return merge(l,r)

sort(iAr)

