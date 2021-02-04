from math import gcd

def solution(w,h):    
    div = gcd(w, h)

    return w * h - (w + h - div)
        

solution(8, 12)