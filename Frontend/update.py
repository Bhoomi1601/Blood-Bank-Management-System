import datetime

import pandas as pd
import streamlit as st
from database import *


def update_employee():
    result = view_all_data_Employee()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Employee-name','Employee-id','Employee-phone','BB-id'])
    with st.expander("Current Employee"):
        st.dataframe(df)
    list_of_employee = [i[0] for i in view_only_Employee_id()]
    selected_employee = st.selectbox("Employee to Edit", list_of_employee)
    selected_result = get_Employee(selected_employee)
    # st.write(selected_result)
    if selected_result:
        e_name = selected_result[0][0]
        e_id = selected_result[0][1]
        e_phone = selected_result[0][2]
        bloodbank_id = selected_result[0][3]


        # Layout of Create

        col1, col2 = st.columns(2)

        with col1:
            new_e_name = st.text_input("Employee-name:",e_name)
            new_e_id = st.text_input("Employee-id:",e_id)
        with col2:
            new_e_phone = st.text_input("Employee-phone:",e_phone)
            new_bloodbank_id = st.text_input("BB-id:",bloodbank_id)

        if st.button("Update Employee"):
            edit_Employee_data(new_e_id,new_e_name,new_e_phone,new_bloodbank_id,e_id)
            st.success("Successfully updated:: {} to ::{}".format(e_phone, new_e_phone))

    result2 = view_all_data_Employee()
    df2 = pd.DataFrame(result2, columns=['Employee-name','Employee-id','Employee-phone','BB-id'])
    with st.expander("Updated data"):
        st.dataframe(df2)






def update_BB():
    result = view_all_data_BB()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Blood-bank-id','Blood-bank-address','Blood-bank-phone','BB-manager-id'])
    with st.expander("Current BLOOD-BANK"):
        st.dataframe(df)
    list_of_blood_bank = [i[0] for i in view_only_BB_id()]
    selected_blood_bank = st.selectbox("Blood-bank to Edit", list_of_blood_bank)
    selected_result = get_BB(selected_blood_bank)
    # st.write(selected_result)
    if selected_result:
        bb_id = selected_result[0][0]
        bb_address = selected_result[0][1]
        bb_phone = selected_result[0][2]
        m_id = selected_result[0][3]


        # Layout of Create

        col1, col2 = st.columns(2)
        with col1:
            new_bb_id = st.text_input('Blood-bank-id',bb_id)
            new_bb_address = st.text_input("Blood-bank-address:",bb_address)
        with col2:
            new_bb_phone = st.text_input("Blood-bank-phone:",bb_phone)
            new_m_id = st.text_input("BB-manager-id:", m_id)
        if st.button("Update Blood-bank"):
            edit_BB_data(new_bb_id, new_bb_address, new_bb_phone, new_m_id, bb_id)
            st.success("Successfully updated:: {} to ::{}".format(bb_phone, new_bb_phone))

    result2 = view_all_data_BB()
    df2 = pd.DataFrame(result2, columns=['Blood-bank-id','Blood-bank-address','Blood-bank-phone','BB-manager-id'])
    with st.expander("Updated data"):
        st.dataframe(df2)



def update_BD():
    result = view_all_data_BD()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Blood-Donor-ID','BD-name','BD-gender','BD-address','BD-phone','Blood-group','Bld-bank-id','BD-Date-Of-Birth','BD-age'])
    with st.expander("Current DONOR"):
        st.dataframe(df)
    list_of_donor = [i[0] for i in view_only_BD_id()]
    selected_donor = st.selectbox("Blood-donor to Edit", list_of_donor)
    selected_result = get_BD(selected_donor)
    # st.write(selected_result)
    if selected_result:
        bd_id = selected_result[0][0]
        bd_name = selected_result[0][1]
        bd_sex = selected_result[0][2]
        bd_address=result[0][3]
        bd_phone = selected_result[0][4]
        bd_Bgroup = selected_result[0][5]
        registered_blood_bank_id = selected_result[0][6]
        Date_of_birth = result[0][7]
        age=result[0][8]


        # Layout of Create

        col1, col2 = st.columns(2)

        with col1:
            new_bd_id = st.text_input("Blood-Donor-ID",bd_id)
            new_bd_name = st.text_input("BD-name",bd_name)
            new_bd_sex = st.selectbox(bd_sex, ["M", "F"])
            new_bd_address = st.text_input("BD-address",bd_address)
            new_bd_phone = st.text_input("BD-phone",bd_phone)
        with col2:
            new_bd_Bgroup = st.selectbox(bd_Bgroup, ["A+ve", "B+ve", "A-ve", "B-ve", "AB+ve", "AB-ve", "O+ve", "O-ve"])
            new_registered_blood_bank_id = st.text_input('Bld-bank-id',registered_blood_bank_id)
            new_Date_of_birth = st.date_input("BD-Date-Of-Birth:",Date_of_birth)
            new_age = st.text_input("BD-age",age)

        if st.button("Update DONOR"):
            edit_BD_data(new_bd_id,new_bd_name,new_bd_sex,new_bd_address, new_bd_phone,new_bd_Bgroup,new_registered_blood_bank_id,new_Date_of_birth,new_age,bd_id)
            st.success("Successfully updated:: {} to ::{}".format(bd_phone, new_bd_phone))

    result2 = view_all_data_BD()
    df2 = pd.DataFrame(result2, columns=['Blood-Donor-ID','BD-name','BD-gender','BD-address','BD-phone','Blood-group','Bld-bank-id','BD-Date-Of-Birth','BD-age'])
    with st.expander("Updated data"):
        st.dataframe(df2)



def update_hospital():
    result = view_all_data_hospital()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Hospital-name','Hospital-id','Hospital-address','Hospital-phone'])
    with st.expander("Current Hospital"):
        st.dataframe(df)
    list_of_hospital = [i[0] for i in view_only_hospital_id()]
    selected_hospital = st.selectbox("Hospital to Edit", list_of_hospital)
    selected_result = get_hospital(selected_hospital)
    # st.write(selected_result)
    if selected_result:
        h_name = selected_result[0][0]
        h_id = selected_result[0][1]
        h_address=selected_result[0][2]
        h_phone = selected_result[0][3]


        # Layout of Create

        col1, col2 = st.columns(2)

        with col1:
            new_h_name = st.text_input("Hospital-name:",h_name)
            new_h_id = st.text_input("Hospital-id:",h_id)
        with col2:
            new_h_address = st.text_input("Hospital-address:", h_address)
            new_h_phone = st.text_input("Hospital-phone:",h_phone)

        if st.button("Update Hospital"):
            edit_hospital_data(new_h_id,new_h_name,new_h_address,new_h_phone,h_id)
            st.success("Successfully updated:: {} to ::{}".format(h_phone, new_h_phone))

    result2 = view_all_data_hospital()
    df2 = pd.DataFrame(result2, columns=['Hospital-name','Hospital-id','Hospital-address','Hospital-phone'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def update_orders():
    result = view_all_data_orders()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Required-BG','Blood-Units-Required','Requested-Date','Hos-Id','BloodB_Id'])
    with st.expander("Current Orders"):
        st.dataframe(df)
    list_of_orders = [i[0] for i in view_only_orders_id()]
    selected_orders = st.selectbox("Orders to Edit", list_of_orders)
    selected_result = get_ORDERS(selected_orders)
    # st.write(selected_result)

    if selected_result:
        required_bg = selected_result[0][0]
        blood_units_required= selected_result[0][1]
        requested_date=selected_result[0][2]
        hospital_id=selected_result[0][3]
        blood_bank_id = selected_result[0][4]


        # Layout of Create

        col1, col2 = st.columns(2)

        with col1:
            new_required_bg = st.text_input("Required-BG:",required_bg)
            new_blood_units_required = st.text_input("Blood-Units-Required:",blood_units_required)
            new_requested_date=st.date_input("Requested-Date:",requested_date)
        with col2:
            new_hospital_id = st.text_input("Hos-Id:", hospital_id)
            new_blood_bank_id = st.text_input("BloodB_Id:",blood_bank_id)

        if st.button("Update Orders"):
            edit_ORDERS_data(new_required_bg,new_blood_units_required,new_requested_date,new_hospital_id,new_blood_bank_id,hospital_id)
            st.success("Successfully updated:: {} to ::{}".format(blood_units_required, new_blood_units_required))

    result2 = view_all_data_orders()
    df2 = pd.DataFrame(result2, columns=['Required-BG','Blood-Units-Required','Requested-Date','Hos-Id','BloodB_Id'])
    with st.expander("Updated data"):
        st.dataframe(df2)

def update_donateblood():
    result = view_all_data_donateblood()
    # st.write(result)
    df = pd.DataFrame(result, columns=['BloodD-bg','blood_B_id','blood_D_id','Blood-Units','Donor_Donated_date'])
    with st.expander("Current Donaters"):
        st.dataframe(df)
    list_of_donaters = [i[0] for i in view_only_donateblood_id()]
    selected_donaters = st.selectbox("Donaters to Edit", list_of_donaters)
    selected_result = get_donateblood(selected_donaters)
    # st.write(selected_result)

    if selected_result:

        blood_group = selected_result[0][0]
        bloodB_id= selected_result[0][1]
        bloodD_id=selected_result[0][2]
        units=selected_result[0][3]
        Donated_date = selected_result[0][4]


        # Layout of Create

        col1, col2 = st.columns(2)

        with col1:
            new_blood_group = st.text_input("BloodD-bg:",blood_group)
            new_bloodB_id = st.text_input("blood_B_id:",bloodB_id)
            new_bloodD_id=st.text_input("blood_D_id:",bloodD_id)
        with col2:
            new_units= st.text_input("Blood-Units:", units)
            new_Donated_date= st.date_input("Donor_Donated_date:",Donated_date)

        if st.button("Update donaters"):
            edit_donateblood_data(new_blood_group,new_bloodB_id,new_bloodD_id,new_units,new_Donated_date,bloodD_id)
            st.success("Successfully updated:: {} to ::{}".format(units, new_units))

    result2 = view_all_data_donateblood()
    df2 = pd.DataFrame(result2, columns=['BloodD-bg','blood_B_id','blood_D_id','Blood-Units','Donor_Donated_date'])
    with st.expander("Updated data"):
        st.dataframe(df2)


def update_blood_type():
    result = view_all_data_blood_type()
    # st.write(result)
    df = pd.DataFrame(result, columns=['Blood-type-grp','Availability','BldBnk-Id'])
    with st.expander("Current Blood-details"):
        st.dataframe(df)
    list_of_blood = [i[0] for i in view_only_blood_type_id()]
    selected_blood = st.selectbox("blood to Edit", list_of_blood)
    selected_result = get_blood_type(selected_blood)
    # st.write(selected_result)
    if selected_result:
        bloodtype_grp = selected_result[0][0]
        availabile = selected_result[0][1]
        bldbank_id = selected_result[0][2]


        # Layout of Create

        col1, col2 = st.columns(2)

        with col1:
            new_bloodtype_grp = st.text_input('Blood-type-grp',bloodtype_grp)
            new_availabile = st.selectbox(availabile,['yes', 'no'])
        with col2:
            new_bldbank_id = st.text_input('BldBnk-Id',bldbank_id)

        if st.button("Update blood-details"):
            edit_blood_type_data(new_bloodtype_grp,new_availabile,new_bldbank_id,bldbank_id)
            st.success("Successfully updated:: {} to ::{}".format(bldbank_id,new_bldbank_id))

    result2 = view_all_data_blood_type()
    df2 = pd.DataFrame(result2, columns=['Blood-type-grp','Availability','BldBnk-Id'])
    with st.expander("Updated data"):
        st.dataframe(df2)