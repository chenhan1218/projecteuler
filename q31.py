#!/usr/bin/python
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    coins = [1,2,5,10,20,50,100,200]
    n=200
    ways=[[1] for i in range(len(coins))]
    for i in range(1,n+1):
        for idx, coin in enumerate(coins):
            ways[idx].append(0)
            if idx>0:
                ways[idx][i] += ways[idx-1][i]
            if i-coin >=0:
                ways[idx][i] += ways[idx][i-coin]
    print ways[len(coins)-1][n]
