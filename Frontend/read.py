import pandas as pd
import streamlit as st
import plotly.express as px
from database import *


def read_Employee():
    result = view_all_data_Employee()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Employee-name', 'Employee-id', 'Employee-phone', 'BB-id'])
    with st.expander("View all employee"):
        st.dataframe(df)
    with st.expander("employee details"):
        employee_df = df['BB-id'].value_counts().to_frame()
        employee_df = employee_df.reset_index()
        st.dataframe(employee_df)
        p1 = px.pie(employee_df, names='index', values='BB-id')
        st.plotly_chart(p1)


def read_BB():
    result = view_all_data_BB()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Blood-bank-id', 'Blood-bank-address', 'Blood-bank-phone', 'BB-manager-id'])
    with st.expander("View all Blood-bank"):
        st.dataframe(df)
    with st.expander("Blood-bank details"):
        blood_df = df['Blood-bank-address'].value_counts().to_frame()
        blood_df = blood_df.reset_index()
        st.dataframe(blood_df)
        p1 = px.pie(blood_df, names='index', values='Blood-bank-address')
        st.plotly_chart(p1)


def read_BD():
    result = view_all_data_BD()
    # st.write(result)
    df = pd.DataFrame(result,
                      columns=['Blood-Donor-ID', 'BD-name', 'BD-gender', 'BD-address', 'BD-phone', 'Blood-group',
                               'Bld-bank-id', 'BD-Date-Of-Birth', 'BD-age'])
    with st.expander("View all Blood-donor"):
        st.dataframe(df)
    with st.expander("Blood-donor details"):
        blood_donor_df = df['BD-gender'].value_counts().to_frame()
        blood_donor_df = blood_donor_df.reset_index()
        st.dataframe(blood_donor_df)
        p1 = px.pie(blood_donor_df, names='index', values='BD-gender')
        st.plotly_chart(p1)


def read_hospital():
    result = view_all_data_hospital()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Hospital-name', 'Hospital-id', 'Hospital-address', 'Hospital-phone'])
    with st.expander("View all hospital"):
        st.dataframe(df)
    with st.expander("hospital details"):
        hospital_df = df['Hospital-address'].value_counts().to_frame()
        hospital_df = hospital_df.reset_index()
        st.dataframe(hospital_df)
        p1 = px.pie(hospital_df, names='index', values='Hospital-address')
        st.plotly_chart(p1)


def read_orders():
    result = view_all_data_orders()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Required-BG', 'Blood-Units-Required','Requested-Date', 'Hos-Id', 'BloodB_Id'])
    with st.expander("View all Orders"):
        st.dataframe(df)
    with st.expander("Order details"):
        orders_df = df['Required-BG'].value_counts().to_frame()
        orders_df = orders_df.reset_index()
        st.dataframe(orders_df)
        p1 = px.pie(orders_df, names='index', values='Required-BG')
        st.plotly_chart(p1)

def read_donateblood():
    result = view_all_data_donateblood()
    # st.write(result)
    df = pd.DataFrame(result, columns=['BloodD-bg','blood_B_id','blood_D_id','Blood-Units','Donor_Donated_date'])
    with st.expander("View all donaters"):
        st.dataframe(df)
    with st.expander("donater details"):
        donate_df = df['blood_B_id'].value_counts().to_frame()
        donate_df = donate_df.reset_index()
        st.dataframe(donate_df)
        p1 = px.pie(donate_df, names='index', values='blood_B_id')
        st.plotly_chart(p1)



def read_blood_type():
    result = view_all_data_blood_type()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Blood-type-grp','Availability','BldBnk-Id'])
    with st.expander("View all Blood-type"):
        st.dataframe(df)
    with st.expander("Blood details"):
        blood_df = df['BldBnk-Id'].value_counts().to_frame()
        blood_df = blood_df.reset_index()
        st.dataframe(blood_df)
        p1 = px.pie(blood_df, names='index', values='BldBnk-Id')
        st.plotly_chart(p1)


