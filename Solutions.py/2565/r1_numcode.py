[length, transformed], previous = [int(_) for _ in input().split()], []
for pos in range(length):
    info = int(input())
    previous = [0 if length-info==1 else 1, info] if pos==0 else ([(1 if(_:=abs(info-previous[1])>previous[1])else 0), previous[1]+(1 if _ else -1)] if transformed==2 else [(1 if info>previous[1] else 0), info])
    print(previous[0])
# Passed