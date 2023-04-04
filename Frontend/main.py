import streamlit as st
import mysql.connector
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
# )

# c = mydb.cursor()
# c.execute("CREATE DATABASE pes1ug20cs633_lab10")

from create import *
from database import *
from delete import *
from read import *
from update import *
from query import  *



def main():
    st.title("pes1ug20cs633 BLOOD-BANK")
    menu_main = ["Employee", "Blood-bank", "Blood-donor", "Hospital","Orders","Donate-Blood","Blood-type"]
    choice_main = st.sidebar.selectbox("Menu_Tables", menu_main)

    if choice_main=="Employee":
        menu = ["Add", "View", "Edit", "Remove","Query"]
        choice = st.sidebar.selectbox("Menu", menu)
        if choice == "Add":
            st.subheader("Enter Employee details:")
            create_Employee()

        elif choice == "View":
            st.subheader("View created Employee")
            read_Employee()

        elif choice == "Edit":
            st.subheader("Update created Employee")
            update_employee()

        elif choice == "Remove":
            st.subheader("Delete created Employee")
            delete_employee()
        elif choice=="Query":
            st.subheader("Enter Query")
            query()
        else:
            st.subheader("About Employee")



    elif choice_main=="Blood-bank":
        menu = ["Add", "View", "Edit", "Remove","Query"]
        choice = st.sidebar.selectbox("Menu", menu)
        if choice == "Add":
            st.subheader("Enter Blood-bank details:")
            create_BB()

        elif choice == "View":
            st.subheader("View created Blood-bank")
            read_BB()

        elif choice == "Edit":
            st.subheader("Update created Blood-bank")
            update_BB()

        elif choice == "Remove":
            st.subheader("Delete created Blood-bank")
            delete_BB()
        elif choice=="Query":
            st.subheader("Enter Query")
            query()

        else:
            st.subheader("About Blood-bank")




    elif choice_main=="Blood-donor":
        menu = ["Add", "View", "Edit", "Remove","Query"]
        choice = st.sidebar.selectbox("Menu", menu)
        if choice == "Add":
            st.subheader("Enter Blood-donor details:")
            create_BD()
        elif choice == "View":
            st.subheader("View created Blood-donor")
            read_BD()

        elif choice == "Edit":
            st.subheader("Update created Blood-donor")
            update_BD()

        elif choice == "Remove":
            st.subheader("Delete created Blood-donor")
            delete_BD()
        elif choice=="Query":
            st.subheader("Enter Query")
            query()
        else:
            st.subheader("About Blood-donor")


    elif choice_main=="Hospital":
        menu = ["Add", "View", "Edit", "Remove","Query"]
        choice = st.sidebar.selectbox("Menu", menu)
        if choice == "Add":
            st.subheader("Enter Hospital details:")
            create_hospital()
        elif choice == "View":
            st.subheader("View created Hospital")
            read_hospital()

        elif choice == "Edit":
            st.subheader("Update created Hospital")
            update_hospital()

        elif choice == "Remove":
            st.subheader("Delete created Hospital")
            delete_hospital()
        elif choice=="Query":
            st.subheader("Enter Query")
            query()
        else:
            st.subheader("About Hospital")

    elif choice_main=="Orders":
        menu = ["Add", "View", "Edit", "Remove","Query"]
        choice = st.sidebar.selectbox("Menu", menu)
        if choice == "Add":
            st.subheader("Enter Order details:")
            create_orders()
        elif choice == "View":
            st.subheader("View created Order")
            read_orders()

        elif choice == "Edit":
            st.subheader("Update created Order")
            update_orders()

        elif choice == "Remove":
            st.subheader("Delete created Order")
            delete_orders()
        elif choice=="Query":
            st.subheader("Enter Query")
            query()
        else:
            st.subheader("About Order")

    elif choice_main=="Donate-Blood":
        menu = ["Add", "View", "Edit", "Remove","Query"]
        choice = st.sidebar.selectbox("Menu", menu)
        if choice == "Add":
            st.subheader("Enter donater details:")
            create_donateblood()
        elif choice == "View":
            st.subheader("View created donater")
            read_donateblood()

        elif choice == "Edit":
            st.subheader("Update created donater")
            update_donateblood()

        elif choice == "Remove":
            st.subheader("Delete created donater")
            delete_donateblood()
        elif choice=="Query":
            st.subheader("Enter Query")
            query()
        else:
            st.subheader("About donater")



    elif choice_main=="Blood-type":
        menu = ["Add", "View", "Edit", "Remove"]
        choice = st.sidebar.selectbox("Menu", menu)
        if choice == "Add":
            st.subheader("Enter Blood-type details:")
            create_blood_type()


        elif choice == "View":
            st.subheader("View created Blood-type")
            read_blood_type()

        elif choice == "Edit":
            st.subheader("Update created Blood-type")
            update_blood_type()

        elif choice == "Remove":
            st.subheader("Delete created Blood-type")
            delete_blood_type()
        else:
            st.subheader("About Blood-type")

    else:
        st.subheader("Blood-bank")




if __name__ == '__main__':
    main()
