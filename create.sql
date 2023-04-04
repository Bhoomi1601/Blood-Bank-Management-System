create TABLE EMPLOYEE(e_name varchar(15) NOT NULL,e_id char(9) NOT NULL,
e_phone char(15),bloodbank_id char(10) NOT NULL,PRIMARY KEY(e_id));

CREATE TABLE BLOOD_BANK(bb_id char(10) NOT NULL,bb_address varchar(20),bb_phone varchar(20),
m_id char(9) NOT NULL,PRIMARY KEY(bb_id),FOREIGN KEY(m_id) REFERENCES EMPLOYEE(e_id));

CREATE TABLE BLOOD_TYPE(bloodgroup varchar(10) DEFAULT NULL,availabile varchar(10),bldbank_id char(10) NOT NULL,
PRIMARY KEY(bloodgroup,bldbank_id),FOREIGN KEY(bldbank_id) REFERENCES BLOOD_BANK(bb_id));

CREATE TABLE BLOOD_DONOR(bd_id char(10) NOT NULL,bd_name varchar(15) NOT NULL,
bd_sex varchar(15) NOT NULL,bd_address varchar(20),bd_phone varchar(20),
bd_Bgroup varchar(10) NOT NULL,bbank_id char(15),Date_of_birth date,age char(10) DEFAULT NULL,PRIMARY KEY(bd_id),
FOREIGN KEY(bbank_id) REFERENCES BLOOD_BANK(bb_id));


CREATE TABLE DONATE_BLOOD(blood_group varchar(10) NOT NULL,bloodB_id char(10) NOT NULL,
bloodD_id char(10) NOT NULL,units int,Donated_date date,
FOREIGN KEY(bloodB_id) REFERENCES BLOOD_BANK(bb_id),FOREIGN KEY(bloodD_id) REFERENCES BLOOD_DONOR(bd_id));

CREATE TABLE HOSPITAL(h_name varchar(15) NOT NULL,h_id char(9) NOT NULL,
h_address varchar(20),h_phone  varchar(20),PRIMARY KEY(h_id));


CREATE TABLE ORDERS(required_bg varchar(10),blood_units_required int,hospital_id char(9) NOT NULL,
bloodbank_id char(10) NOT NULL,FOREIGN KEY(hospital_id) REFERENCES HOSPITAL(h_id),
FOREIGN KEY(bloodbank_id) REFERENCES BLOOD_BANK(bb_id));

