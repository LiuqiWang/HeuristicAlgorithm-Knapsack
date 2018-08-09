# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 17:48:54 2018

@author: liuqi
"""

def load_knapsack(things,knapsack_cap):
    """ You write your heuristic knapsack algorithm in this function using the argument values that are passed
             items: is a dictionary of the items no yet loaded into the knapsack
             knapsack_cap: the capacity of the knapsack (volume)
    
        Your algorithm must return two values as indicated in the return statement:
             my_team_number_or_name: if this is a team assignment then set this variable equal to an integer representing your team number;
                                     if this is an indivdual assignment then set this variable to a string with you name
            items_to_pack: this is a list containing keys (integers) of the items you want to include in the knapsack
                           The integers refer to keys in the items dictionary. 
   """
# iteration using ratio        
    my_team_number_or_name = "lwang"    # always return this variable as the first item
    
    items_to_pack = []    # use this list for the indices of the items you load into the knapsack
    load = 0.0            # use this variable to keep track of how much volume is already loaded into the backpack
    value = 0.0           # value in knapsack
      
    item_list = [[k,v,float(v[1])/v[0]] for k,v in things.items()]
    j = lambda x:x[2]
    item_list=sorted(item_list,key=j,reverse=True)
    
    item_keys = [item[0] for item in item_list]
   
    for i in range(len(item_keys)):
        if load <= knapsack_cap:
            pack_item = item_keys[i]
            load += things[pack_item][0]
            if load <= knapsack_cap:
                items_to_pack.append(pack_item)
            #load += things[pack_item][0]
                value += things[pack_item][1]
    return my_team_number_or_name, items_to_pack 

