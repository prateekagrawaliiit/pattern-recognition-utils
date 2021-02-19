# -*- coding: utf-8 -*-
# @Author: prateek
# @Date:   2021-02-19 22:46:31
# @Last Modified by:   prateek
# @Last Modified time: 2021-02-19 22:57:57

import streamlit as st
import numpy as np 
from math import log2

st.write("""
        # PATTERN RECOGNITION HELPER UTILS
        """)

st.header('For calculating the KL distance and Bhattacharya distance between two histograms')
st.write("""
        ### First Line Input Rep = 1,2,3,4,5 - Histogram 1 
        ### Second Line Input Rep = 6,7,8,9,10 - Histogram 2 """)

sequence_input = "0.24,0.2,0.16,0.12,0.08,0.04,0.12,0.04\n0.22,0.23,0.16,0.13,0.11,0.08,0.05,0.02"

sequence = st.text_area("Inputs H1 and H2", sequence_input, height=250)
sequence = sequence.splitlines()

H1 = [float(x) for x in sequence[0].split(',')]
H2 = [float(x) for x in sequence[1].split(',')]

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

histo_distance = st.button('Click to Calculate the Distances')

if histo_distance:
    st.write('The KL distance between H1 and H2 is = {}'.format(KLDistance(H1,H2)))
    st.write('The Bhattacharya distance between H1 and H2 is = {}'.format(BhattacharyaDistance(H1,H2)))