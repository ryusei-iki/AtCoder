def main():
    A,B,N=map(int,input().split())
    max=0
    for i in range(1,N+1):
        if(A*i//B-A*(i//B)>max):
            a=i
            max=A*i//B-A*(i//B)
    print(max)
main()
