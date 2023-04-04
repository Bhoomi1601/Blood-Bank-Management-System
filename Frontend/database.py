import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="pes1ug20cs633_blood"
)
c = mydb.cursor()


# def create_table():
#     c.execute('CREATE TABLE IF NOT EXISTS BLOOD_BANK(bb_id char(10), bb_address varchar(20), bb_phone varchar(20),m_id char(9));')
def add_data_Employee(e_name,e_id,e_phone,bloodbank_id):
    c.execute('INSERT INTO EMPLOYEE(e_name,e_id,e_phone,bloodbank_id) VALUES (%s,%s,%s,%s)',
              (e_name,e_id,e_phone,bloodbank_id))
    mydb.commit()


def view_all_data_Employee():
    c.execute('SELECT * FROM EMPLOYEE')
    data = c.fetchall()
    return data


def view_only_Employee_id():
    c.execute('SELECT e_id FROM Employee')
    data = c.fetchall()
    return data


def get_Employee(e_id):
    c.execute('SELECT * FROM EMPLOYEE WHERE e_id="{}"'.format(e_id))
    data = c.fetchall()
    return data


def edit_Employee_data(new_e_id,new_e_name,new_e_phone,new_bloodbank_id,e_id):
    c.execute("UPDATE EMPLOYEE SET e_id=%s,e_name=%s,e_phone=%s,bloodbank_id=%s WHERE e_id=%s",
              (new_e_id,new_e_name,new_e_phone,new_bloodbank_id,e_id))
    mydb.commit()
    # data = c.fetchall()
    # return data


def delete_Employee_data(e_id):
    c.execute('DELETE FROM EMPLOYEE WHERE e_id="{}"'.format(e_id))
    mydb.commit()





def add_data_BB(bb_id, bb_address, bb_phone, m_id):
    c.execute('INSERT INTO BLOOD_BANK(bb_id,bb_address,bb_phone,m_id) VALUES (%s,%s,%s,%s)',
              (bb_id, bb_address, bb_phone, m_id))
    mydb.commit()


def view_all_data_BB():
    c.execute('SELECT * FROM BLOOD_BANK')
    data = c.fetchall()
    return data


def view_only_BB_id():
    c.execute('SELECT bb_id FROM BLOOD_BANK')
    data = c.fetchall()
    return data


def get_BB(bb_id):
    c.execute('SELECT * FROM BLOOD_BANK WHERE bb_id="{}"'.format(bb_id))
    data = c.fetchall()
    return data


def edit_BB_data(new_bb_id, new_bb_address, new_bb_phone, new_m_id, bb_id):
    c.execute("UPDATE BLOOD_BANK SET bb_id=%s,bb_address=%s,bb_phone=%s,m_id=%s WHERE bb_id=%s ",
              (new_bb_id, new_bb_address, new_bb_phone, new_m_id, bb_id))
    mydb.commit()
    # data = c.fetchall()
    # return data


def delete_BB_data(bb_id):
    c.execute('DELETE FROM BLOOD_BANK WHERE bb_id="{}"'.format(bb_id))
    mydb.commit()



def add_data_BD(bd_id,bd_name,bd_sex,bd_address, bd_phone,bd_Bgroup,registered_blood_bank_id,Date_of_birth,age):
    c.execute('INSERT INTO BLOOD_DONOR(bd_id,bd_name,bd_sex,bd_address, bd_phone,bd_Bgroup,registered_blood_bank_id,Date_of_birth,age) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)',
              (bd_id,bd_name,bd_sex,bd_address, bd_phone,bd_Bgroup,registered_blood_bank_id,Date_of_birth,age))
    mydb.commit()


def view_all_data_BD():
    c.execute('SELECT * FROM BLOOD_DONOR')
    data = c.fetchall()
    return data


def view_only_BD_id():
    c.execute('SELECT bd_id FROM BLOOD_DONOR')
    data = c.fetchall()
    return data


def get_BD(bd_id):
    c.execute('SELECT * FROM BLOOD_DONOR WHERE bd_id="{}"'.format(bd_id))
    data = c.fetchall()
    return data


def edit_BD_data(new_bd_id,new_bd_name,new_bd_sex,new_bd_address, new_bd_phone,new_bd_Bgroup,new_registered_blood_bank_id,new_Date_of_birth,new_age,bd_id):
    c.execute("UPDATE BLOOD_DONOR SET bd_id=%s,bd_name=%s,bd_sex=%s,bd_address=%s,bd_phone=%s,bd_Bgroup=%s,registered_blood_bank_id=%s,Date_of_birth=%s,age=%s WHERE bd_id=%s",
              (new_bd_id,new_bd_name,new_bd_sex,new_bd_address, new_bd_phone,new_bd_Bgroup,new_registered_blood_bank_id,new_Date_of_birth,new_age,bd_id))
    mydb.commit()
    # data = c.fetchall()
    # return data


def delete_BD_data(bd_id):
    c.execute('DELETE FROM BLOOD_DONOR WHERE bd_id="{}"'.format(bd_id))
    mydb.commit()




def add_data_hospital(h_name,h_id,h_address,h_phone):
    c.execute('INSERT INTO HOSPITAL(h_name,h_id,h_address,h_phone) VALUES (%s,%s,%s,%s)',
              (h_name,h_id,h_address,h_phone))
    mydb.commit()


def view_all_data_hospital():
    c.execute('SELECT * FROM HOSPITAL')
    data = c.fetchall()
    return data


def view_only_hospital_id():
    c.execute('SELECT h_id FROM HOSPITAL')
    data = c.fetchall()
    return data


def get_hospital(h_id):
    c.execute('SELECT * FROM HOSPITAL WHERE h_id="{}"'.format(h_id))
    data = c.fetchall()
    return data


def edit_hospital_data(new_h_id,new_h_name,new_h_address,new_h_phone,h_id):
    c.execute("UPDATE HOSPITAL SET h_id=%s,h_name=%s,h_address=%s,h_phone=%s WHERE h_id=%s",
              (new_h_id,new_h_name,new_h_address,new_h_phone,h_id))
    mydb.commit()
    # data = c.fetchall()
    # return data


def delete_hospital_data(h_id):
    c.execute('DELETE FROM HOSPITAL WHERE h_id="{}"'.format(h_id))
    mydb.commit()



def add_data_orders(required_bg,blood_units_required,requested_date,hospital_id,blood_bank_id):
    c.execute('INSERT INTO ORDERS(required_bg,blood_units_required,requested_date,hospital_id,blood_bank_id) VALUES (%s,%s,%s,%s,%s)',
              (required_bg,blood_units_required,requested_date,hospital_id,blood_bank_id))
    mydb.commit()


def view_all_data_orders():
    c.execute('SELECT * FROM ORDERS')
    data = c.fetchall()
    return data


def view_only_orders_id():
    c.execute('SELECT hospital_id FROM ORDERS')
    data = c.fetchall()
    return data


def get_ORDERS(hospital_id):
    c.execute('SELECT * FROM ORDERS WHERE hospital_id="{}"'.format(hospital_id))
    data = c.fetchall()
    return data


def edit_ORDERS_data(new_required_bg,new_blood_units_required,new_requested_date,new_hospital_id,new_blood_bank_id,hospital_id):
    c.execute("UPDATE ORDERS SET required_bg=%s,blood_units_required=%s,requested_date=%s,hospital_id=%s,blood_bank_id=%s WHERE hospital_id=%s",
              (new_required_bg,new_blood_units_required,new_requested_date,new_hospital_id,new_blood_bank_id,hospital_id))
    mydb.commit()
    # data = c.fetchall()
    # return data


def delete_ORDERS_data(hospital_id):
    c.execute('DELETE FROM ORDERS WHERE hospital_id="{}"'.format(hospital_id))
    mydb.commit()





def add_data_donateblood(blood_group,bloodB_id,bloodD_id,units,Donated_date):
    c.execute('INSERT INTO DONATE_BLOOD(blood_group,bloodB_id,bloodD_id,units,Donated_date) VALUES (%s,%s,%s,%s,%s)',
              (blood_group,bloodB_id,bloodD_id,units,Donated_date))
    mydb.commit()


def view_all_data_donateblood():
    c.execute('SELECT * FROM DONATE_BLOOD')
    data = c.fetchall()
    return data


def view_only_donateblood_id():
    c.execute('SELECT bloodD_id FROM DONATE_BLOOD')
    data = c.fetchall()
    return data


def get_donateblood(bloodD_id):
    c.execute('SELECT * FROM DONATE_BLOOD WHERE bloodD_id="{}"'.format(bloodD_id))
    data = c.fetchall()
    return data


def edit_donateblood_data(new_blood_group,new_bloodB_id,new_bloodD_id,new_units,new_Donated_date,bloodD_id):
    c.execute("UPDATE DONATE_BLOOD SET blood_group=%s,bloodB_id=%s,bloodD_id=%s,units=%s,Donated_date=%s WHERE bloodD_id=%s",
              (new_blood_group,new_bloodB_id,new_bloodD_id,new_units,new_Donated_date,bloodD_id))
    mydb.commit()
    # data = c.fetchall()
    # return data


def delete_donateblood_data(bloodD_id):
    c.execute('DELETE FROM DONATE_BLOOD WHERE bloodD_id="{}"'.format(bloodD_id))
    mydb.commit()












def add_data_blood_type(bloodtype_grp,availabile,bldbank_id):
    c.execute('INSERT INTO BLOOD_TYPE(bloodtype_grp,availabile,bldbank_id) VALUES (%s,%s,%s)',
              (bloodtype_grp,availabile,bldbank_id))
    mydb.commit()


def view_all_data_blood_type():
    c.execute('SELECT * FROM BLOOD_TYPE')
    data = c.fetchall()
    return data


def view_only_blood_type_id():
    c.execute('SELECT bloodtype_grp FROM BLOOD_TYPE')
    data = c.fetchall()
    return data


def get_blood_type(bloodtype_grp):
    c.execute('SELECT * FROM BLOOD_TYPE WHERE bloodtype_grp="{}"'.format(bloodtype_grp))
    data = c.fetchall()
    return data


def edit_blood_type_data(new_bloodtype_grp,new_availabile,new_bldbank_id,bloodtype_grp):
    c.execute("UPDATE BLOOD_TYPE SET bloodtype_grp=%s,availabile=%s,bldbank_id=%s WHERE bloodtype_grp=%s",
              (new_bloodtype_grp,new_availabile,new_bldbank_id,bloodtype_grp))
    mydb.commit()
    # data = c.fetchall()
    # return data


def delete_blood_type_data(bloodtype_grp):
    c.execute('DELETE FROM BLOOD_TYPE WHERE bloodtype_grp="{}"'.format(bloodtype_grp))
    mydb.commit()



def query_exec(query):
    c.execute(query)
    data=c.fetchall()
    return  data



