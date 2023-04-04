import pandas as pd
import streamlit as st
from database import *


def delete_employee():
    result = view_all_data_Employee()
    df = pd.DataFrame(result, columns=['Employee-name','Employee-id','Employee-phone','BB-id'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_employee = [i[0] for i in view_only_Employee_id()]
    selected_employee = st.selectbox("Task to Delete_Employee", list_of_employee)
    st.warning("Do you want to delete ::{}".format(selected_employee))
    if st.button("Delete Employee"):
        delete_Employee_data(selected_employee)
        st.success("Employee has been deleted successfully")
    new_result = view_all_data_Employee()
    df2 = pd.DataFrame(new_result, columns=['Employee-name','Employee-id','Employee-phone','BB-id'])
    with st.expander("Updated data"):
        st.dataframe(df2)



def delete_BB():
    result = view_all_data_BB()
    df = pd.DataFrame(result, columns=['Blood-bank-id','Blood-bank-address','Blood-bank-phone','BB-manager-id'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_blood_bank = [i[0] for i in view_only_BB_id()]
    selected_blood_bank = st.selectbox("Task to Delete_BB", list_of_blood_bank)
    st.warning("Do you want to delete ::{}".format(selected_blood_bank))
    if st.button("Delete Blood-bank"):
        delete_BB_data(selected_blood_bank)
        st.success("Blood-bank has been deleted successfully")
    new_result = view_all_data_BB()
    df2 = pd.DataFrame(new_result, columns=['Blood-bank-id','Blood-bank-address','Blood-bank-phone','BB-manager-id'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def delete_BD():
    result = view_all_data_BD()
    df = pd.DataFrame(result, columns=['Blood-Donor-ID','BD-name','BD-gender','BD-address','BD-phone','Blood-group','Bld-bank-id','BD-Date-Of-Birth','BD-age'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_blood_donor = [i[0] for i in view_only_BD_id()]
    selected_blood_donor = st.selectbox("Task to Delete_BD", list_of_blood_donor)
    st.warning("Do you want to delete ::{}".format(selected_blood_donor))
    if st.button("Delete Blood-blood-donor"):
        delete_BD_data(selected_blood_donor)
        st.success("Blood-donor has been deleted successfully")
    new_result = view_all_data_BD()
    df2 = pd.DataFrame(new_result, columns=['Blood-Donor-ID','BD-name','BD-gender','BD-address','BD-phone','Blood-group','Bld-bank-id','BD-Date-Of-Birth','BD-age'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_hospital():
    result = view_all_data_hospital()
    df = pd.DataFrame(result, columns=['Hospital-name','Hospital-id','Hospital-address','Hospital-phone'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_hospital = [i[0] for i in view_only_hospital_id()]
    selected_hospital = st.selectbox("Task to Delete_Hospital", list_of_hospital)
    st.warning("Do you want to delete ::{}".format(selected_hospital))
    if st.button("Delete Hospital"):
        delete_hospital_data(selected_hospital)
        st.success("Hospital has been deleted successfully")
    new_result = view_all_data_hospital()
    df2 = pd.DataFrame(new_result, columns=['Hospital-name','Hospital-id','Hospital-address','Hospital-phone'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_orders():
    result = view_all_data_orders()
    df = pd.DataFrame(result, columns=['Required-BG','Blood-Units-Required','Requested-Date','Hos-Id','BloodB_Id'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_orders = [i[0] for i in view_only_orders_id()]
    selected_orders= st.selectbox("Task to Delete_Orders", list_of_orders)
    st.warning("Do you want to delete ::{}".format(selected_orders))
    if st.button("Delete Orders"):
        delete_ORDERS_data(selected_orders)
        st.success("Order has been deleted successfully")
    new_result = view_all_data_orders()
    df2 = pd.DataFrame(new_result, columns=['Required-BG','Blood-Units-Required','Requested-Date','Hos-Id','BloodB_Id'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def delete_donateblood():
    result = view_all_data_donateblood()
    df = pd.DataFrame(result, columns=['BloodD-bg','blood_B_id','blood_D_id','Blood-Units','Donor_Donated_date'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_donaters = [i[0] for i in view_only_donateblood_id()]
    selected_donaters= st.selectbox("Task to Delete_Donaters", list_of_donaters)
    st.warning("Do you want to delete ::{}".format(selected_donaters))
    if st.button("Delete donater"):
        delete_donateblood_data(selected_donaters)
        st.success("donater has been deleted successfully")
    new_result = view_all_data_donateblood()
    df2 = pd.DataFrame(new_result, columns=['BloodD-bg','blood_B_id','blood_D_id','Blood-Units','Donor_Donated_date'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def delete_blood_type():
    result = view_all_data_blood_type()
    df = pd.DataFrame(result, columns=['Blood-type-grp','Availability','BldBnk-Id'])
    with st.expander("Current data"):
        st.dataframe(df)

    list_of_blood = [i[0] for i in view_only_blood_type_id()]
    selected_blood = st.selectbox("Task to Delete", list_of_blood)
    st.warning("Do you want to delete ::{}".format(selected_blood))
    if st.button("Delete Blood-type"):
        delete_blood_type_data(selected_blood)
        st.success("Blood has been deleted successfully")
    new_result = view_all_data_blood_type()
    df2 = pd.DataFrame(new_result, columns=['Blood-type-grp','Availability','BldBnk-Id'])
    with st.expander("Updated data"):
        st.dataframe(df2)