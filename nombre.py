def suma(x,y):
    return x+y
def resta(x,y):
    print("La resta entre {0} y {1} es:".format(x,y))
    return x-y
def producto(x,y):
    return x*y
def mcd(x,y):
    if x<y:
        x,y=y,x
    else:
        residuo = y
        while residuo!=0:
            residuo=x%y
            x,y=y,residuo
    return x
def fracciones (x,y):
    num = int(x/mcd(x,y))
    den = int(y/mcd(x,y))
    return str(num)+'/'+str(den)
def simplificar(x,y):
    num = int(x/mcd(x,y))
    den = int(y/mcd(x,y))
    if den == 1:
        str(num)
    if den == 0:
        print("ERROR: No existe")
    return str(num)+'/'+str(den)
def suma_fracciones(n1,d1,n2,d2):
    num = ((n1*d2)+(n2*d1))
    den = (d1*d2)
    sf = ((n1*d2)+(n2*d1))/(d1*d2)
    if d1*d2 == 0:
        print("ERROR")
    else:
        print ("La suma entre {}/{} y {}/{} es:".format(n1,d1,n2,d2))
    return str(num)+'/'+str(den)
def resta_fracciones (n1,d1,n2,d2):
    num = ((n1*d2)-(n2*d1))
    den = (d1*d2)
    rf = ((n1*d2)-(n2*d1))/(d1*d2)
    if d1*d2 == 0:
        print("ERROR")
    else:
        print ("La resta entre {}/{} y {}/{} es:".format(n1,d1,n2,d2))
    return str(num)+'/'+str(den)
def multi_fracciones (n1,d1,n2,d2):
    num = (n1*n2)
    den = (d1*d2)
    mf = (n1*n2)/(d1*d2)
    if d1*d2 == 0:
        print("ERROR")
    else: 
        print ("La multiplicación entre {}/{} y {}/{} es:".format(n1,d1,n2,d2))
    return str(num)+'/'+str(den)
def divi_fracciones (n1,d1,n2,d2):
    num = (n1*d2)
    den = (d1*n2)
    df = (n1*d2)/(d1*n2)
    if d1*n2 == 0:
        print ("ERROR")
    else: 
        print ("La división entre {}/{} y {}/{} es:".format(n1,d1,n2,d2))
    return str(num)+'/'+str(den)

 
          