import streamlit as st
from database import *


def create_Employee():
    col1, col2 = st.columns(2)
    with col1:
        e_name = st.text_input("Employee-name:")
        e_id = st.text_input("Employee-id:")
    with col2:
        e_phone = st.text_input("Employee-phone:")
        bloodbank_id = st.text_input("BB-id:")
        if st.button("Add Employee"):
            add_data_Employee(e_name,e_id,e_phone,bloodbank_id)
            st.success("Successfully added employee: {}".format(e_name))


def create_BB():
    col1, col2 = st.columns(2)
    with col1:
        bb_id = st.text_input("Bld-bank-id")
        bb_address = st.text_input("Blood-bank-address:")
    with col2:
        bb_phone = st.text_input("Blood-bank-phone:")
        m_id = st.text_input("BB-manager-id:")
    if st.button("Add Blood-bank"):
        add_data_BB(bb_id, bb_address, bb_phone, m_id)
        st.success("Successfully added: {}".format(bb_phone))


def create_BD():
    col1, col2 = st.columns(2)
    with col1:
        bd_id = st.text_input("Blood-Donor-ID")
        bd_name=st.text_input("BD-name")
        bd_sex = st.selectbox("BD-gender",["M","F"])
        bd_address=st.text_input("BD-address")
        bd_phone=st.text_input("BD-phone")
    with col2:
        bd_Bgroup = st.selectbox("Blood-Group", ["A+ve", "B+ve", "A-ve", "B-ve", "AB+ve", "AB-ve", "O+ve", "O-ve"])
        registered_blood_bank_id = st.text_input("BBId")
        Date_of_birth = st.date_input("BD-Date-Of-Birth:")
        age = st.text_input("BD-age")
    if st.button("Add Blood-Donor"):
        add_data_BD(bd_id,bd_name,bd_sex,bd_address, bd_phone,bd_Bgroup,registered_blood_bank_id,Date_of_birth,age)
        st.success("Successfully added: {}".format(bd_phone))


def create_hospital():
    col1, col2 = st.columns(2)
    with col1:
        h_name = st.text_input("Hospital-name:")
        h_id = st.text_input("Hospital-id:")
    with col2:
        h_address = st.text_input("Hospital-address:")
        h_phone = st.text_input("Hospital-phone:")
        if st.button("Add Hospital"):
            add_data_hospital(h_name,h_id,h_address,h_phone)
            st.success("Successfully added hospital: {}".format(h_phone))


def create_orders():
    col1, col2 = st.columns(2)
    with col1:
        required_bg = st.text_input("Required-BG:")
        blood_units_required = st.text_input("Blood-Units-Required:")
        requested_date=st.date_input("Requested-Date:")
    with col2:
        hospital_id = st.text_input("Hos-Id:")
        blood_bank_id = st.text_input("BloodB_Id:")
        if st.button("Add Orders"):
            add_data_orders(required_bg,blood_units_required,requested_date,hospital_id,blood_bank_id)
            st.success("Successfully added orders: {}".format(hospital_id))


def create_donateblood():
    col1, col2 = st.columns(2)
    with col1:
        blood_group = st.selectbox("BloodD-bg:", ["A+ve", "B+ve", "A-ve", "B-ve", "AB+ve", "AB-ve", "O+ve", "O-ve"])
        bloodB_id = st.text_input("blood_B_id:")
        bloodD_id=st.text_input("blood_D_id:")
    with col2:
        units = st.text_input("Blood-Units:")
        Donated_date= st.date_input("Donor_Donated_date:")
        if st.button("Add donaters"):
            add_data_donateblood(blood_group,bloodB_id,bloodD_id,units,Donated_date)
            st.success("Successfully added donors: {}".format(bloodD_id))


def create_blood_type():
    col1, col2 = st.columns(2)
    with col1:
        bloodtype_grp = st.selectbox("Blood-type-grp", ["A+ve", "B+ve", "A-ve", "B-ve", "AB+ve", "AB-ve", "O+ve", "O-ve"])
    with col2:
        availabile = st.selectbox("Availability", ['yes', 'no'])
    bldbank_id= st.text_input("BldBnk-Id")
    if st.button("Add Blood-type"):
        add_data_blood_type(bloodtype_grp,availabile,bldbank_id)
        st.success("Successfully added: {}".format(bldbank_id))


