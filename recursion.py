def towerofhanoi (n,from_rod,aux_rod,to_rod):

    if n == 0:
        return
    
    towerofhanoi(n-1,from_rod,aux_rod,to_rod)

    print(f"Moive disc {n} from {from_rod} to {to_rod}")

    towerofhanoi(n-1,aux_rod,to_rod,from_rod)

def fabbonachiseries(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fabbonachiseries(n-2) + fabbonachiseries(n-1)

n = 3
print(fabbonachiseries(n))