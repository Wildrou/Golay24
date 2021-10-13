from golay import descodifica,recuperaPalabraFuente,codifica,introduceRuido
from exceptions import LongitudCodigoIncorrecto,CodigoNoBinario,LongitudFuenteIncorrecto
import numpy as np
try:
    
    f=input("Introduce una palabra fuente: ")
    r=codifica(f)
    r_lista=introduceRuido(r)
    print()
    for i in range(len(r_lista)):
        print("Estacion "+str(i+1)+" recibe:"+r_lista[i])
        c=descodifica(r_lista[i])
        if c is not None:
        
            recuperaPalabraFuente(c)
        print()

    
except LongitudFuenteIncorrecto:
    pass       

except CodigoNoBinario:
    pass
    
    
except LongitudCodigoIncorrecto:
    pass
    
            
            

           

 