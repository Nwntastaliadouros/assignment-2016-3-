def plusminus(ld):
    test=[]
    sd=len(ld)
    test.append(ld[0]+1)
    for i in range(1,sd-1):        
        #test.append(ld[sd-i-1])
        test.append(ld[i])
    test.append(ld[sd-1]-1)
    return(test)
#############################
def reverseeuklid(ld):
    test=reversestring(ld)
    #####################################
    plusminus1=plusminus(test)
    if (plusminus1==ld):
        s1="It is a reverse Euclidean string"
    else:
        s1=""
    return(s1)
#####################
def showrythm():
    abclist=[]
    n=len(sys.argv[2])    
    k=sys.argv[2].count("1")
    for i in range(1,n):
        abclittle=[]
        abclittle.clear()
        lr=[]
        lr.clear()
        lr=euklid1(n,i)
        xx=makelrstring(lr)     ## make simple list
        rythm=makeerstring(xx)  ## find equivalent binary string e.g. 101010101010   
        cc=distance(sys.argv[2],rythm)
        abclittle.append(cc)
        abclittle.append(i)
        abclittle.append(xx)
        abclittle.append(rythm)
        abclist.append(abclittle)
        ## calculate distance
    s=sorted(abclist, key=itemgetter(0,1))      ## sortef list has been created
    ####################################
    print()
    for i in range(0,len(s)):
        aa=s[i][0]
        print("Distance = ",aa)
        bb=s[i][1]
        euklid3(s[i][2],s[i][3],n,bb)
    return
#####################################
def read_ison(second,first):        ## (9,4)
    ff="musical_rythms.json"
    f = open(ff, 'r')
    for line in f.readlines():
        if (len(line)>2):
            p1=(line.find("("))     ## where first ( stands
            p2=(line.find(","))     ## where first , stands
            p3=(line.find(")"))     ## where first ) stands
            f1=int(line[(p1+1):p2])
            f2=int(line[(p2+1):p3])
            if ((f1==first)and (f2==second)):
                return(line[14:])
    return("")
######################################
def vspace(xx):
    # It accepts the simple list xx - returns vector space
    ld=[]
    fn=0
    for i in range(1,len(xx)):        
        if (xx[i]==1):
            ld.append(i-fn)
            fn=i
    #######################
    if (xx[len(xx)-1]==1):
        ld.append(1)
    else:
        ddd=len(xx)-fn
        ld.append(ddd)
    return(ld)
########################
def distance(base,other):
    ll=len(base)
    nn=0
    for i in range(0,ll):
        a1=base[i:i+1]
        a2=other[i:i+1]
        if (a1!=a2):
            nn=nn+1
    return(nn)
########################
def euklid3(xx,rythm,n,k):        
    #######################################################
    ss="E("+str(k)+","+str(n)+") = ["+rythm+"] = ("
    ##################################        
    ld=vspace(xx)   ## virtual space in simple list
    ####################################
    ss=ss+makeerstring(ld)+") "
    ####################################
    dd=read_ison(n,k)
    ss=ss+dd
    ####################################
    aa=ss[0:-1]
    print(aa)
    s1=euklid(ld)
    if s1!="":
        print(s1)     ## Returns a string if it is an Euclidean string
    s2=reverseeuklid(ld)
    if s2!="":
        print(s2)
    return
###################################################
def euklid2(lr,n,k):       
    xx=makelrstring(lr)     ## make simple list
    rythm=makeerstring(xx)  ## find equivalent binary string e.g. 101010101010   
    #######################################################
    ss="E("+str(k)+","+str(n)+") = ["+rythm+"] = ("
    ##################################        
    ld=vspace(xx)   ## virtual space in simple list
    ####################################
    ss=ss+makeerstring(ld)+") "
    ####################################
    ss=ss+read_ison(n,k)
    ####################################        
    aa=ss[0:-1]
    print(aa)
    s1=euklid(ld)
    if s1!="":
        print(s1)     ## Returns a string if it is an Euclidean string
    s2=reverseeuklid(ld)
    if s2!="":
        print(s2)
    return
###################################################
def euklid1(n,k):
    if (n % k)==0:
        lr.clear()
        lp=[]      ## left pattern
        lp.append(1)
        rp=[]      ## second pattern
        rp.append(0)
        for i in range(0,int(k)):
            lr.append(lp)
            for j in range(0,int(n/k)-1):
                lr.append(rp)           
    else:
        lr.clear()
        kk=k        ## Number of first patterns e.g. 8
        rr=n-k      ## Number of second patterns
        lp=[]       ## left pattern
        rp=[]       ## second pattern
        lp.append(1)
        rp.append(0)   
        for i in range(0,int(k)):           
            lr.append(lp)        
        fp=deepcopy(lp)
        ##############################       
        for i in range(0,int(n-k)):
            lr.append(rp)                    
        sp=deepcopy(rp)   
        ######################################
        if rr==1:
            lr.clear()    
            lr.append(lp)      
            lr.append(rp)
            for i in range(0,int(n-2)):
                lr.append(lp)                            
        ######################################
        while (rr>1):
            if (rr>=kk):
                rr=rr-kk    ## new number of the second pattern
                lp.clear()         
                lp=fp+sp          
                lr.clear()    
                for i in range(0,int(kk)):                
                    lr.append(lp)      
                for i in range(0,int(rr)):                
                    lr.append(sp)            
                fp=deepcopy(lp)
                sp=deepcopy(sp)
                #######################
            else:       ##  rr<kk
                sptemp=deepcopy(lp)
                ##################
                lp.clear()         
                lp=fp+sp                           
                lr.clear()
                for i in range(0,int(rr)):                
                    lr.append(lp)       
                temp=rr
                rr=kk-rr
                kk=temp
                sp=deepcopy(sptemp)
                for i in range(0,int(rr)):                
                    lr.append(sp)            
                fp=deepcopy(lp)
                sp=deepcopy(sp)
            ######################  if has ended   
        #######################   while gas ended
    return(lr)
#########################################
def recrythm(ss):   ## It is a binary string
    n=len(ss)
    k=ss.count("1")
    lr=euklid1(n,k)
    if (ss==makeerstring(makelrstring(lr))):
        euklid2(lr,n,k)
    else:
        print("Not an Euclidean string.")
    return
##############################
def reversestring(ld):
    ##  find reverse
    re=[]
    sd=len(ld)
    for i in range(0,sd):
        re.append(ld[sd-i-1])    
    return(re)  # return reverse string in simple list
    #####################################    
def euklid(ld):
    ##  find reverse
    re=reversestring(ld)    ## reverse string in simple list
    #####################################
    test=plusminus(ld)      ## plusminus string in a simple list
    #####################################
    if (test==re):
        s1="It is a Euklidean string"
    else:
        s1=""
    return(s1)
#####################
def makelrstring(lr):
    xx=[]
    for i in range(0,len(lr)):
        xx=xx+lr[i]    
    return(xx)
############################
def makeerstring(lr):
    ## store the string
    xxx=""
    gg=[]
    for i in range(0,len(lr)):        
        gg=lr[i]
        xxx=xxx+str(gg)
    return (xxx)
##############################3
def euklidian(n,k):   
    # The single list or complicate list has been created in list lr
    lr=euklid1(n,k)
    euklid2(lr,n,k)    
#########################################################
def hamming_distance(s1, s2):   ## s1, s2 binary strings
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(bool(ord(ch1) - ord(ch2)) for ch1, ch2 in zip(s1, s2))
#########################################################
import sys
import operator
from operator import itemgetter
from copy import deepcopy
# ff=sys.argv[1]
#############################################################                
lr=[]       ## List that keep rythms
if (len(sys.argv))==5:
    n=int(sys.argv[2])   ## SLOTS  -  I will take this from command prompt
    k=int(sys.argv[4])   ## PULSES -  I will take this from command prompt
    euklidian(n,k)
if (len(sys.argv))==3:
    if sys.argv[1]=="-r":
        recrythm(sys.argv[2])
    if sys.argv[1]=="-l":
        showrythm()
#############################################################                
