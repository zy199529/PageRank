#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Lenovo
# @Date:   2019-07-11 21:29:49
# @Last Modified by:   Lenovo
# @Last Modified time: 2019-07-11 22:22:25
import numpy as np

if __name__=='__main__':
    f = open('./data.txt','r')
    edges = [line.strip('\n').split(' ') for line in f]
    print(edges)

    nodes = []
    for edge in edges:
        if edge[0] not in nodes:
            nodes.append(edge[0])
        if edge[1] not in nodes:
            nodes.append(edge[1])
    print(nodes)
    N = len(nodes)
    i = 0
    node_to_num = {}
 # 节点映射成阿拉伯数字
    for node in nodes:
    	node_to_num[node] = i
    	i=i+1
    for edge in edges:
    	edge[0] = node_to_num[edge[0]]
    	edge[1] = node_to_num[edge[1]]
    print(edges)
    # 生成初步的S矩阵
    S = np.zeros([N,N])
    for edge in edges:
    	S[edge[1],edge[0]] = 1
    print(S)
    # 计算比例：即一个网页对其他网页的PageRank值
    for j in range(N):
    	sum_of_col = sum(S[:,j])
    	for i in range(N):
    		S[i,j]/=sum_of_col
    print(S)
    alpha = 0.85
    A = alpha*S + (1-alpha)/N*np.ones([N,N])
    print(A)
    p_n = np.ones(N)/N
    p_n1 = np.zeros(N)
    e = 100000
    k = 0
    while e > 0.00000001:
        p_n1 = np.dot(A,p_n)
        e = p_n1 - p_n
        e = max(map(abs,e))
        p_n = p_n1
        k=k+1
        print('%s:'%str(k), p_n1)
    print(p_n)