# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2021-02-19 22:46:31
# @Last Modified by:   prateekagrawaliiit
# @Last Modified time: 2021-02-20 15:14:50


from math import*
from decimal import Decimal
import streamlit as st
import numpy as np 

def nth_root(value, n_root):
 
    root_value = 1/float(n_root)
    return round (Decimal(value) ** Decimal(root_value),3)
 
def minkowski_distance(x,y,p_value):
 
    return nth_root(sum(pow(abs(a-b),p_value) for a,b in zip(x, y)),p_value)
 
# print minkowski_distance([0,3,4,5],[7,6,3,-1],3)
def L_p_infinite(H1,H2):
    x = [abs(a-b) for a,b in zip(H1,H2)]
    return np.max(x)
def L_n_infinite(H1,H2):
    x = [abs(a-b) for a,b in zip(H1,H2)]
    return np.min(x)

def BhattacharyaDistance(H1,H2):
    distance =0
    for i in range(len(H1)):
        distance += np.sqrt(H1[i]*H2[i])
    return -1 * log2(distance)

# FUNCTION TO CALCULATE KL DISTANCE
def KLDistance(H1,H2) :
    distance=0
    for i in range(len(H1)):
        distance+=H1[i]*log2((H1[i]/H2[i]))
    return distance

def quad_form_dist(V,A):
    return np.matmul(V,np.matmul(A,V.T))

def cosine_distance(H1,H2):
    return 1 - (np.dot(H1,H2)/(np.linalg.norm(H1)*(np.linalg.norm(H2))))





st.write("""
        # PATTERN RECOGNITION HELPER UTILS
        """)

st.write("""
        ## Metric Distance and Proximity Measures for Normalized Histograms
        """)
st.write("""
         First Line Input Rep = 1,2,3,4,5 - Histogram \n
         Second Line Input Rep = 6,7,8,9,10 - Histogram 2 \n 
         P-value - 2""")

sequence_input = "1,2,3,4,5\n6,7,8,9,10\n2"

sequence = st.text_area("Inputs H1 and H2", sequence_input, height=100)
sequence = sequence.splitlines()

H1 = [float(x) for x in sequence[0].split(',')]
H2 = [float(x) for x in sequence[1].split(',')]
p_value = int(sequence[2])
minkowski_btn = st.button('Calculate Metric Distances')

if minkowski_btn:
    st.write('The Minkowski Distance is {}'.format(minkowski_distance(H1,H2,p_value)))
    st.write('The Euclidean Distance is {}'.format(minkowski_distance(H1,H2,2)))
    st.write('The Manhattan Distance is {}'.format(minkowski_distance(H1,H2,1)))
    st.write('The L (infinity) Norm Chybyshev Distance is {}'.format(L_p_infinite(H1,H2)))
    st.write('The L (-infinity) Norm is {}'.format(L_n_infinite(H1,H2)))


st.header('Quadratic Form Distance')

query_vector = st.text_input("Query Vector Hq", '1,2,3')
mean_vector = st.text_input("Mean Vector Ht", '1,0,0')

query_vector = [float(x) for x in query_vector.split(',')]
mean_vector =  [float(x) for x in mean_vector.split(',')]
V=[]
for i in range(len(query_vector)):
    V.append(query_vector[i]-mean_vector[i])
V = np.asarray(V)
transform_matrix = st.text_area('Transform Matrix A','1,0.9,0\n0.9,1,0\n0,0,1')
transform_matrix_lines = transform_matrix.splitlines()
A = np.asarray([np.asarray([float(y) for y in x.split(',')]) for x in transform_matrix_lines])

quad_form_dist_btn = st.button('Calculate Quadratic Form Distance')

if quad_form_dist_btn:
    st.write('The Quadratic Form Distance is {}'.format(quad_form_dist(V,A)))

st.write("""
        ## Non-Metric Distance and Proximity Measures for Normalized Histograms
        """)
st.write("""
         First Line Input Rep = 1,2,3,4,5 - Histogram \n
         Second Line Input Rep = 6,7,8,9,10 - Histogram 2 \n """)
sequence_input = "0.24,0.2,0.16,0.12,0.08,0.04,0.12,0.04\n0.22,0.23,0.16,0.13,0.11,0.08,0.05,0.02"

sequence = st.text_area("Inputs H1 and H2", sequence_input, height=100)
sequence = sequence.splitlines()

H1 = [float(x) for x in sequence[0].split(',')]
H2 = [float(x) for x in sequence[1].split(',')]

histo_distance = st.button('Click to Calculate the Distances')

if histo_distance:
    st.write('The KL distance between H1 and H2 is = {}'.format(KLDistance(H1,H2)))
    st.write('The Bhattacharya distance between H1 and H2 is = {}'.format(BhattacharyaDistance(H1,H2)))
    st.write('The Cosine distance between H1 and H2 is = {}'.format(cosine_distance(H1,H2)))