
def is_rearranged(list_1, list_2):
    #print(len(list_1))
    #print(len(list_2))
    missmatch = []
    list_2_mod = list_2.copy()
    for i in list_1:
        try:
            list_2_mod.remove(i)
        except:
            missmatch.append(i)
    
    if len(list_1) != len(list_2):
        print("different lists (different lengths)")    
    else:
        if len(list_2_mod) == 0:

            print("lists are matching")
        else:
            print(f"There are missmatching values: {missmatch}")


