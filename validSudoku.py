    def isValidSudoku(self, A):
        import collections
        row=0
        for i in range(9): 
            l=[]
            for j in range(9):
                if(i<9 and j<9):
                    if(A[i][j]!='.'):
                        l.append(A[i][j])
            if([x for x in l if l.count(x) > 1]):
                row=1
        if(row==1):
            return 0
        col=0
        B=list(map(list, zip(*A)))
        for i in range(9):
            l=[]
            for j in range(9):
                if(i<9 and j<9):
                    if(B[i][j]!='.'):
                        l.append(B[i][j])
            if([x for x in l if l.count(x) > 1]):
                col=1
        if(col==1):
            return 0
        d=0
        b=[]
        for i in range(9):
            j1=(i/3)*3
            j2=j1+3
            l=[]
            for j in range(int(j1),int(j2)):
                k1=(i%3)*3
                k2=k1+3
                for k in range(k1,k2):
                        if (A[j][k] != '.'):
                            l.append(A[j][k])
            if([x for x in l if l.count(x)>1]):
                d=1
            if(d==1):
                b.append(1)
            else:
                b.append(0)
        for i in range(9):
            if(b[i]==1):
                return 0
        return 1
