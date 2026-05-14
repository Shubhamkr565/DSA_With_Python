l1 = 6
l2 = 5
t = 5

def solution(l1,l2,t):
    cost1 = 0
    cost2 = 0
    if t < l1:
        p1 = l1-t
        
        cost1 = p1*(l1-p1)
        print("Total cost l1: ",cost1)
    if t < l2:
        q1 = l2-t
        cost2 = q1*(l2-q1)
        print("Total cost l2: ",cost2)
    

    total_amount = cost1+cost2
    print("Total Amount : ",total_amount)

solution(l1,l2,t)

    
        
