from numpy import in1d


def decideLarger(int1,int2):
    if (int1 < int2):
        return int2
    elif (int1 > int2):
        return int1
    else:
        return 'equal'
        
print(decideLarger(1,1))