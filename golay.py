import numpy as np
from exceptions import LongitudCodigoIncorrecto, LongitudFuenteIncorrecto,\
    CodigoNoBinario
from random import shuffle


G= np.array([[1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1],
                     [0,1,0,0,0,0,0,0,0,0,0,0,1,1,1,0,1,1,1,0,0,0,1,0],
                     [0,0,1,0,0,0,0,0,0,0,0,0,1,1,0,1,1,1,0,0,0,1,0,1],
                     [0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,1,1,0,0,0,1,0,1,1],
                     [0,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,0,0,0,1,0,1,1,0],
                     [0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0,0,0,1,0,1,1,0,1],
                     [0,0,0,0,0,0,1,0,0,0,0,0,1,1,0,0,0,1,0,1,1,0,1,1],
                     [0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,1,0,1,1,0,1,1,1],
                     [0,0,0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,1,1,0,1,1,1,0],
                     [0,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,1,1,0,1,1,1,0,0],
                     [0,0,0,0,0,0,0,0,0,0,1,0,1,1,0,1,1,0,1,1,1,0,0,0],
                     [0,0,0,0,0,0,0,0,0,0,0,1,1,0,1,1,0,1,1,1,0,0,0,1]
                     ])
        
G_TR= np.transpose(G)
A=G[ : , 12: ]
        
        
        
        
def descodifica(r):
        r="".join(r.split())
        try:
            if not all(d in '01' for d in r):
                raise CodigoNoBinario
            
            elif len(r) != 24 :
                raise LongitudCodigoIncorrecto
                
            zero12=np.array([0,0,0,0,0,0,0,0,0,0,0,0])
            ai_index=None
            c=None
            msg="la palabra codigo transmitida es: "
            r_arr= np.array(list(r),dtype=int)
            r1=r_arr[0:12]
            r2=r_arr[12:24] 
            s1=np.add(r1,np.dot(r2,A)%2)%2
            
            if np.count_nonzero(s1 == 1) <= 3 :
                e=np.concatenate((s1,zero12))
                c=np.add(e,r_arr)%2
                msg+=np.array_str(c)
               
            elif (ai_index := sumaFilasA(s1)):
                zero12[ai_index[1]]=1
                e=np.concatenate((np.add(s1,ai_index[0]),zero12))
                c=np.add(e,r_arr)%2
                msg+=np.array_str(c)
                
            else:
                s2=np.dot(s1,A)%2
                if np.count_nonzero(s2 == 1) <= 3 :
                    e=np.concatenate((zero12,s2))
                    c=np.add(e,r_arr)%2
                    msg+=np.array_str(c)
                
                elif (ai_index := sumaFilasA(s2)):
                    zero12[ai_index[1]]=1
                    e=np.concatenate((zero12,np.add(s2,ai_index[0])))
                    c=np.add(e,r_arr)%2
                    msg+=np.array_str(c)
                
                else:
                    msg="Se han producido mas de tres errores, retransmision necesaria"
                    
            print(msg)
            c=''.join(map(str,c)) if c is not None else None
            return c
        
        except LongitudCodigoIncorrecto:
            print("La palabra codigo no tiene longitud 24")
            raise
            
        except CodigoNoBinario:
            print("Los simbolos de la palabra codigo no pertenecen a Z2")
            raise
        
def sumaFilasA(s):
        s_plus_ai=None
        for row in A:
            row_arr=np.asarray(row)
            s_plus_ai=np.add(np.asarray(s),row_arr)
            if np.count_nonzero(s_plus_ai == 1) <= 2:
                index=np.where(np.all(row_arr==A,axis=1))    
                return row_arr,index
        
        
            else:
                pass
                
        
        

def recuperaPalabraFuente(c):
        c="".join(c.split())
        try:
            if not all(d in '01' for d in c) :
                raise CodigoNoBinario
            elif len(c) != 24:
                raise LongitudCodigoIncorrecto  
            c_arr= np.array(list(c),dtype=int)
            f=c_arr[0:12]
            print("la palabra fuente transmitida es: "+np.array_str(f))
            return ''.join(map(str,f))
        
        except CodigoNoBinario:
            print("Los simbolos de la palabra codigo no pertenecen a Z2")
            
        except LongitudCodigoIncorrecto:
            print("La palabra codigo no tiene longitud 24")
        
        
def paridad(c):
        c="".join(c.split())
        c_arr= np.array(list(c),dtype=int)    
        zero=np.dot(c_arr,G_TR)%2
        print(zero)
        
    
def codifica(f):
        f="".join(f.split())
        try:
            if not all(d in '01' for d in f) :
                raise CodigoNoBinario
            elif len(f) != 12:
                raise LongitudFuenteIncorrecto
            f_arr= np.array(list(f),dtype=int)   
            c=np.dot(f_arr,G)%2
            print("La palabra fuente codificada es: "+np.array_str(c))
            return ''.join(map(str,c))    
        
        except CodigoNoBinario:
            print("Los elementos de la palabra codigo no pertenecen a Z2")
            raise
            
        except LongitudFuenteIncorrecto:
            print("La palabra fuente no tiene longitud 12")
            raise
            
def introduceRuido(c):
    mask1=np.array([1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    mask2=np.array([1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    mask3=np.array([1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    mask4=np.array([1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    mask5=np.array([1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    
    lista = [mask1,mask2,mask3,mask4,mask5]
    c=np.array(list(c),dtype=int)
    for i in range(len(lista)):
        shuffle(lista[i])
        lista[i]=''.join(map(str,np.add(lista[i],c)%2)) 
    return lista    
