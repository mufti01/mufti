
#Metode Bisection 
def f(x):
    return 4*x*cos(x)+4*cos(x)-(x**2)*sin(x)+4*x*sin(x)-4*sin(x)
    
def bisection(f,a,b,tol):
    if f(a)*f(b)>0:
        print "tidak dapat dilakukan bisection"
        return None
    else:
        print "------ITERASI-----"
        c=a+float(b-a)/2
        if f(c)*f(a)>0:
            return bisection(f,c,b,tol)
        elif f(c)*f(b)>0:
            return bisection(f,a,c,tol)
        elif f(c)<tol:
            print "-----END-----"
            return c    

#Metode Fixed Point           
def g(x):
    return 4*x*cos(x)+4*cos(x)-(x**2)*sin(x)+ 4*x*sin(x)-4*sin(x)

def fp(g,po,tol):
    print "-----ITERASI-----"
    print "po: %.6f"%po
    p=g(po)
    print "p: %.6f"%p
    if abs(p-po)<=tol:
        print "-----END-----"
        return p
    else:
        po=p
        return fp(g,po,tol)

#Metode Newton    
def f(x):
    return 4*x*cos(x)+4*cos(x)-(x**2)*sin(x)+4*x*sin(x)-4*sin(x)

def df(x):
    return 4*cos(x)-4*x*sin(x)-4*sin(x)-2*x*sin(x)-(x**2)*cos(x)+4*sin(x)+4*x*cos(x)-4*cos(x)

def newton(f,df,po,tol):
    print "-----ITERASI-----"
    print "po: %.5f"%po
    p=po-float((f(po)/df(po)))
    print "p: %.5f"%p
    if abs (p-po)<=tol:
        print "-----END-----"
        return p
    else:
        po=p
        return newton(f,df,po,tol) 
        
#Metode Secant
def h(x):
    return 4*x*cos(x)+4*cos(x)-(x**2)*sin(x)+4*x*sin(x)-4*sin(x)
    
def secant(po,p1,h,tol):
    print "-----ITERASI-----"
    print "po: %.6f"%po
    print "p1: %.6f"%p1
    p2 = p1 - float((h(p1)*(p1-po))/(h(p1)-h(po)))
    print "p: %.6f"%p2
    if abs(p2-p1)<=tol:
        print "-----END-----"
        return p2
    else:
        po=p1
        p1=p2
        return secant(po,p1,h,tol)

print 'METODE NUMERIK'
print '1 = Bisection'
print '2 = Fixed Point'
print '3 = Newton'
print '4 = Secant'
Metode=input('Pilih salah satu nomer di atas untuk menentukan akar dari f(x) menggunakan metode yang telah dipilih : ')

if Metode==1:
    print 'Metode Bisection dengan nilai a=1, b=2, dan toleransi=10^-5'
    print bisection(f,1,2,10**-5)
elif Metode==2:
    print 'Metode Fixed Point dengan p0=1.5 dan toleransi=10^-5'
    print fp(g,1.5,10**-5)
elif Metode==3:
    print 'Metode Newton dengan p0=1.5 dan toleransi=10^-5'
    print newton(f,df,1.5,10**-5) 
elif Metode==4:
    print 'Metode Secant dengan p0=1.5, p1=1.6, dan toleransi=10^-5'
    print secant(1.5,1.6,h,10**-5)
elif Metode>4:
    print 'Nomer yang anda masukan tidak tersedia di pilihan, silahkan coba lagi'
