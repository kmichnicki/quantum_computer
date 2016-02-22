import math

# This script simulates a quantum computer by applying
# unitary transformations, represented as matrices, to
# a quantum state, represented as a complex valued vector. 

# the convention is that the kets are labelled |...,q2,q1> so |001>
# corresponds to q1=1,q2=0,q3=0.

def X(i,vector):
    newvector=len(vector)*[0.0]
    for key in range(len(vector)):
        bb=bin(key)[2:]
        bb=bb[::-1]
 
        if len(bb)<i:
            newvector[key+2**(i-1)]=vector[key]
        elif bb[i-1]=='0':
            newvector[key+2**(i-1)]=vector[key]
        else:
            newvector[key-2**(i-1)]=vector[key]

    return newvector

def Z(i,vector):
    newvector=len(vector)*[0.0]
    for key in range(len(vector)):
        bb=bin(key)[2:]
        bb=bb[::-1]
 
        if len(bb)<i:
            newvector[key]=vector[key]
        elif bb[i-1]=='0':
            newvector[key]=vector[key]
        else:
            newvector[key]=-vector[key]

    return newvector

def T(i,vector):
    newvector=len(vector)*[0.0]
    for key in range(len(vector)):
        bb=bin(key)[2:]
        bb=bb[::-1]
 
        if len(bb)<i:
            newvector[key]=vector[key]
        elif bb[i-1]=='0':
            newvector[key]=vector[key]
        else:
            newvector[key]=(math.e**(complex(0.0,1.0)*math.pi/4.0))*vector[key]

    return newvector

def H(i,vector):
    v1=X(i,vector)

    v2=Z(i,vector)
    newvector=[0]*len(vector)
    for key in range(len(vector)):
        newvector[key]=(1/math.sqrt(2))*(v1[key]+v2[key])
        

    return newvector


def C(cc,tt,vector):
    newvector=len(vector)*[0]
    for key in range(len(vector)):
        bb=bin(key)[2:]
        bb=bb[::-1]
        
        
        if len(bb)<cc: #no flip
            newvector[key]=vector[key]
        elif bb[cc-1]=='0': #no flip
            newvector[key]=vector[key]
        else: #flip target bit
            if len(bb)<tt:
                newvector[key+2**(tt-1)]=vector[key]
            elif bb[tt-1]=='0':
                newvector[key+2**(tt-1)]=vector[key]
            else:
                newvector[key-2**(tt-1)]=vector[key]

    return newvector

def parseString(s,v):
    s=s[0:len(s)-1]
    l=s.split(')')
    l=l[::-1]
    op=''
    cc=''
    tt=''
    for key in range(len(l)):
        op=l[key].split('(')[0]
        if op=='C':
            cc=l[key].split('(')[1].split(',')[0]
            tt=l[key].split('(')[1].split(',')[1]
            print cc
            print tt
            v=C(int(cc),int(tt),v)
        elif op=='X':
            cc=l[key].split('(')[1]
            v=X(int(cc),v)
        elif op=='Z':
            cc=l[key].split('(')[1]
            v=Z(int(cc),v)
        elif op=='H':
            cc=l[key].split('(')[1]
            v=H(int(cc),v)
        elif op=='T':
            cc=l[key].split('(')[1]
            v=X(int(cc),v)

    return v


def printDiracNotation(final):
    for key in range(len(final)):
        if final[key]>0.000000001:
            print '|...q2q1>~~~>'+str(final[key])+'|'+'0'*(Nqubits-len(bin(key)[2:]))+bin(key)[2:]+'>'
        
        
        
Nqubits=5

v=[0.0]*(2**Nqubits)
v[0]=1.0


ops='H(1)H(2)H(3)H(4)H(5)'
final=parseString(ops,v)

printDiracNotation(final)


