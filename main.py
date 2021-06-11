import streamlit as st
import logging
import requests
import pytrends
import pandas as pd
import lxml
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
import os
import re
import functools
import time
import collections

st.title("Hello world ! It's Arthur ALLIOUX")

if st.button('Generate joke'):
    req = requests.get(" https://v2.jokeapi.dev/joke/Any")
    reponse = req.json()
    st.text(reponse['category'] + " joke received : ")
    if reponse['type'] == 'single':
        st.write(reponse['joke'])
    if reponse['type'] == 'twopart':
        st.write(reponse['setup'])
        st.write(reponse['delivery'])


