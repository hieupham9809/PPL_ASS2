
def subsum(lst):
    if not lst:
        return []
    else:
        return subsum(lst[:-1]) + [sum(lst)] 

lst = [1,2,3,4,5]
print(subsum(lst))

def subsum2(lst):
    
    return reduce(lambda x,y: x + [x[-1] + y],lst,[0])[1:]
    
print(subsum2(lst))