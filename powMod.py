#POWMOD 
def pow(self, x, n, d):
        if(x!=0):
            r=1
            while n>0:
                if n&1==1:
                    r=r*x%d
                n /=2
                x=x*x % d
            return r   
        else:
            return 0