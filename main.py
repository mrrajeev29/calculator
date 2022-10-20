print('Hi User... \n you are here to use Mathematics calculator..')
import math
print('click 0 for trigonometry values,1 for quadratic equation , 2 for Linear equation.., \n ,3 for exponential value and 4 for log values \n 5 to calculate a^x ,6 for sum of series.')
n=int(input('Enter Here = '))
if n==0:
    ang=float(input('Enter angle (in rad.) to find its trigo ratio = '))
    s1=math.sin(ang)
    s2=math.cos(ang)
    print('sin(',ang,')',"=",s1)
    print("cos(",ang,")",'=',s2)
elif n==1:
    print('quadratic equation of form ax^2+bx+c=0' + '\n' +'Enter following data .')
    a=float(input('a = '))
    b=float(input('b = '))
    c=float(input('c = '))
    d=(b**2-4*a*c)
    D=(d)**0.5
    x1=(-b+D)/(2*a)
    x2=(-b-D)/(2*a)
    if d==0:
        print('Unique Real root',x1)
    elif d>0:
        print('Two different real roots',x1,x2)
    else:
        print('Two Imaginary roots',x1,x2)
elif n==2:
    print('Enter corresponding values of two linear equation of form ax+by+c=0..')
    a1=float(input('a1 = '))
    b1=float(input('b1 = '))
    c1=float(input('c1 = '))
    a2=float(input('a2 = '))
    b2=float(input('b2 = '))
    c2=float(input('c2 = '))
    k1=a1/a2
    k2=b1/b2
    k3=c1/c2
    if k1==k2==k3:
        print('Both lines are coinciding..')
    elif k1==k2!=k3:
        print('Both lines are parallel to each other \nSo no intersecting point..')
    elif k1!=k2:
        x=(b1*c2-b2*c1)/(a1*b2-a2*b1)
        y=(a1*c2-a2*c1)/(a2*b1-a1*b2)
        print("Their intersecting co-ordinate is",'(',x,',',y,')')
elif n==3:
    x=float(input('Enter x of form e^x = '))
    y=math.exp(x)
    print(y)
elif n==4:
    print('log(x) with base b. \n kindly enter 2.7 for e.')
    b=float(input('Enter base(b) of log = '))
    x=float(input('Enter x = '))
    y=math.log(x,b)
    print(y)
elif n==5:
    print('To get a to the power x (i.e a^x).')
    a=float(input('a = '))
    x=float(input('x = '))
    y=a**x
    print('Answer =',y)
elif n==6:
    print('Enter 0 for sum of n series \n 1 for n^2 \n 2 for n^3 \n 3 for any Arithmetic Progression')
    t=int(input('Enter Here = '))
    if t==0:
        print('For sum of series 1+2+3+4+.....+n'+'\n'+'n must be a positive integer otherwise it will be rounded to nearest integer')
        r=int(input('n = '))
        y=(r*(r+1))/2
        print('sum =',y)
    elif t==1:
        print('For sum of series 1^2 +2^2 +3^2 + ....+ n^2' +"\n" +'n must be positive')
        r=int(input('n = '))
        y=(r*(r+1)*(2*r+1))/6
        print('Sum = ',y)
    elif t==2:
        print('For sum of series 1^3 + 2^3 +3^3 +....+n^3 \n nmust be a positive integer')
        r=int(input('n = '))
        y=(r**2)*(r+1)**2/4
        print('Sum =',y)
    elif t==3:
        print('For any A P enter its First term and Common Difference and number of terms..')
        a=float(input('First Term = '))
        d=float(input('Common Difference = '))
        n=int(input('Number of terms = '))
        t=a+(n-1)*d
        s=0.5*n*(2*a+(n-1)*d)
        print('Nth term of AP is',t,'\n'," Sum of nth term is",s)
    else:
        while t!=0 or t!=1 or t!=2 or t!=3:
            print('Oops,Enter a valid input.')
            print('Enter 0 for sum of n series \n 1 for n^2 \n 2 for n^3 \n 3 for any Arithmetic Progression')
            t=int(input('Enter Here = '))
            if t==0:
                print('For sum of series 1+2+3+4+.....+n'+'\n'+'n must be a positive integer otherwise it will be rounded to nearest integer')
                r=int(input('n = '))
                y=(r*(r+1))/2
                print('sum =',y)
                break
            elif t==1:
                print('For sum of series 1^2 +2^2 +3^2 + ....+ n^2' +"\n" +'n must be positive')
                r=int(input('n = '))
                y=(r*(r+1)*(2*r+1))/6
                print('Sum = ',y)
                break
            elif t==2:
                print('For sum of series 1^3 + 2^3 +3^3 +....+n^3 \n nmust be a positive integer')
                r=int(input('n = '))
                y=(r**2)*(r+1)**2/4
                print('Sum =',y)
                break
            elif t==3:
                print('For any A P enter its First term and Common Difference and number of terms..')
                a=float(input('First Term = '))
                d=float(input('Common Difference = '))
                n=int(input('Number of terms = '))
                t=a+(n-1)*d
                s=0.5*n*(2*a+(n-1)*d)
                print('Nth term of AP is',t,'and its sum is',s)
                break
else:
    while n!=0 or n!=1 or n!=2 or n!=3 or n!=4 or n!=5 or n!=6:
        print('Oops,Enter a valid input..')
        n=int(input('Enter Again = '))
        if n==0:
            ang=float(input('Enter angle (in rad.) to find its trigo ratio = '))
            s1=math.sin(ang)
            s2=math.cos(ang)
            print('sin(',ang,')',"=",s1)
            print("cos(",ang,")",'=',s2)
            break
        elif n==1:
            print('quadratic equation of form ax^2+bx+c=0' + '\n' +'Enter following data .')
            a=float(input('a = '))
            b=float(input('b = '))
            c=float(input('c = '))
            d=(b**2-4*a*c)
            D=(d)**0.5
            x1=(-b+D)/(2*a)
            x2=(-b-D)/(2*a)
            if d==0:
                print('Unique Real root',x1)
            elif d>0:
                print('Two different real roots',x1,x2)
            else:
                print('Two Imaginary roots',x1,x2)
            break
        elif n==2:
            print('Enter corresponding values of two linear equation of form ax+by+c=0..')
            a1=float(input('a1 = '))
            b1=float(input('b1 = '))
            c1=float(input('c1 = '))
            a2=float(input('a2 = '))
            b2=float(input('b2 = '))
            c2=float(input('c2 = '))
            k1=a1/a2
            k2=b1/b2
            k3=c1/c2
            if k1==k2==k3:
                print('Both lines are coinciding..')
            elif k1==k2!=k3:
                print('Both lines are parallel to each other \nSo no intersecting point..')
            elif k1!=k2:
                x=(b1*c2-b2*c1)/(a1*b2-a2*b1)
                y=(a1*c2-a2*c1)/(a2*b1-a1*b2)
                print("Their intersecting co-ordinate is",'(',x,',',y,')')
            break
        elif n==3:
            x=float(input('Enter x of form e^x = '))
            y=math.exp(x)
            print(y)
            break
        elif n==4:
            print('log(x) with base b. \n kindly enter 2.7 for e.')
            b=float(input('Enter base(b) of log = '))
            x=float(input('Enter x = '))
            y=math.log(x,b)
            print(y)
            break
        elif n==5:
            print('To get a to the power x (i.e a^x).')
            a=float(input('a = '))
            x=float(input('x = '))
            y=a**x
            print('Answer =',y)
            break
        elif n==6:
            print('Enter 0 for sum of n series \n 1 for n^2 \n 2 for n^3 \n 3 for any Arithmetic Progression')
            t=int(input('Enter Here = '))
            if t==0:
                print('For sum of series 1+2+3+4+.....+n'+'\n'+'n must be a positive integer otherwise it will be rounded to nearest integer')
                r=int(input('n = '))
                y=(r*(r+1))/2
                print('sum =',y)
            elif t==1:
                print('For sum of series 1^2 +2^2 +3^2 + ....+ n^2' +"\n" +'n must be positive')
                r=int(input('n = '))
                y=(r*(r+1)*(2*r+1))/6
                print('Sum = ',y)
            elif t==2:
                print('For sum of series 1^3 + 2^3 +3^3 +....+n^3 \n nmust be a positive integer')
                r=int(input('n = '))
                y=(r**2)*(r+1)**2/4
                print('Sum =',y)
            elif t==3:
                print('For any A P enter its First term and Common Difference and number of terms..')
                a=float(input('First Term = '))
                d=float(input('Common Difference = '))
                n=int(input('Number of terms = '))
                t=a+(n-1)*d
                s=0.5*n*(2*a+(n-1)*d)
                print('Nth term of AP is',t,'\n'," Sum of nth term is",s)
            else:
                while t!=0 or t!=1 or t!=2 or t!=3:
                    print('Oops,Enter a valid input.')
                    print('Enter 0 for sum of n series \n 1 for n^2 \n 2 for n^3 \n 3 for any Arithmetic Progression')
                    t=int(input('Enter Here = '))
                    if t==0:
                        print('For sum of series 1+2+3+4+.....+n'+'\n'+'n must be a positive integer otherwise it will be rounded to nearest integer')
                        r=int(input('n = '))
                        y=(r*(r+1))/2
                        print('sum =',y)
                        break
                    elif t==1:
                        print('For sum of series 1^2 +2^2 +3^2 + ....+ n^2' +"\n" +'n must be positive')
                        r=int(input('n = '))
                        y=(r*(r+1)*(2*r+1))/6
                        print('Sum = ',y)
                        break
                    elif t==2:
                        print('For sum of series 1^3 + 2^3 +3^3 +....+n^3 \n nmust be a positive integer')
                        r=int(input('n = '))
                        y=(r**2)*(r+1)**2/4
                        print('Sum =',y)
                        break
                    elif t==3:
                        print('For any A P enter its First term and Common Difference and number of terms..')
                        a=float(input('First Term = '))
                        d=float(input('Common Difference = '))
                        n=int(input('Number of terms = '))
                        t=a+(n-1)*d
                        s=0.5*n*(2*a+(n-1)*d)
                        print('Nth term of AP is',t,'and its sum is',s)
                        break
            break
print('Thank You....')


