import pandas as pd
import streamlit as st
from database import *

def query():
    query=st.text_area('ENTER QUERY')
    if query:
        result=query_exec(query)
        df=pd.DataFrame(result)
    if st.button("SUBMIT QUERY"):
            st.dataframe(df)