#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 17:04:17 2020

@author: Yani Ferhaoui
"""

def apriori(transactions, nbMinOcurrencies):
    
    # Init L1
    last_set = []
    for elem in transactions:
        for elemb in elem:
            to_add = {elemb}
            if to_add not in last_set and countFrequency(transactions, to_add) >= nbMinOcurrencies:
                last_set.append(to_add)
    all_sets = []
    k = 2
    
    while (len(last_set) != 0):
        all_sets.append(list(last_set))
        next_set = []
        
        for sub_set_one in last_set:
            for sub_set_two in last_set:
                new_sub_set = sub_set_one | sub_set_two
                
                # Here we check size, frequency and not already ib
                if len(new_sub_set) == k and countFrequency(transactions, new_sub_set) >= nbMinOcurrencies and new_sub_set not in next_set: 
                    next_set.append(new_sub_set)
                
        last_set = next_set
        k+=1

    return all_sets

def countFrequency(transactions, last):
    return sum(map(lambda elem : last.issubset(elem), transactions))

def printSets(s):
    for i in range(len(s)):
        print("   L", i+1, " = ", s[i])

if __name__ == '__main__':
    
    #
    # Ce programme fonctionne apriori bien !
    #
    
    print("TEST 1: n=3")
    ls = [
            {1, 2, 5},
            {1, 3, 5}, 
            {1, 2},
            {1, 2, 3, 4, 5},
            {1, 2, 4, 5}, 
            {2, 3, 5}, 
            {1, 5}
        ]
    res = apriori(ls, 3)
    printSets(res)
    
    print("TEST 2: n=2")
    res = apriori(ls, 2)
    printSets(res)
    
    