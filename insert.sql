INSERT into EMPLOYEE VALUES('john','100','9845671234','B01'),('james','101','9842221234','B01'),
('Ram','102','9845871224','B01'),('Roopa','103','6665671234','B01'),
('Shree','104','7845671234','B01'),('Sana','105','9845671234','B01'),
('Reena','200','9845551234','B02'),('Sheela','201','9888671234','B02'),
('Hima','202','9191677774','B02'),('Tom','203','8181677774','B02'),
('Lewis','204','9845672724','B02'),('Lara','205','9845667674','B02'),
('Droupadi','300','9977671234','B03'),('Rahul','301','9845674444','B03'),
('Anshu','302','9846666234','B03'),('Ans','303','9846661134','B03'),
('Rack','304','7161661134','B03'),('Jack','305','8886661134','B03'),
('David','306','7746661134','B03');



INSERT into BLOOD_BANK VALUES('B01','Girinagar','9345671230','101'),
('B02','Jayanagar','9345675656','202'),('B03','RT Nagar','9131315230','300');


INSERT into BLOOD_TYPE VALUES('A+ve','yes','B01'),
('B+ve','yes','B01'),
('AB+ve','no','B01'),
('A-ve','no','B01'),
('B-ve','no','B01'),
('AB-ve','yes','B01'),
('O+ve','yes','B01'),
('O-ve','yes','B01'),
('A+ve','no','B02'),
('B+ve','yes','B02'),
('AB+ve','yes','B02'),
('A-ve','no','B02'),
('AB-ve','yes','B02'),
('O+ve','yes','B02'),
('O-ve','no','B02'),
('A+ve','no','B03'),
('B+ve','yes','B03'),
('AB+ve','no','B03'),
('A-ve','yes','B03'),
('AB-ve','yes','B03'),
('O+ve','no','B03'),
('O-ve','yes','B03');


INSERT into BLOOD_DONOR VALUES('BD1','Robert','M','Jayanagar','9886712333','A+ve','B01','1989-04-14',NULL),
('BD2','David','M','JP Nagar','9886713333','AB+ve','B03','1989-03-12',NULL),
('BD3','John','M','Grinagar','9886712332','B+ve','B02','1980-04-14',NULL),
('BD4','Ajit Ullal','M','High Street','9896712333','B-ve','B01','2004-01-01',NULL),
('BD5','Suma S','F','Jp Nagar','9886712344','A-ve','B03','1970-02-14',NULL),
('BD6','Samanta','F','Girinagar','9886712367','B+ve','B02','1960-05-31',NULL),
('BD7','Ansh','F','JC Road','9990712333','O+ve','B03','1999-02-27',NULL),
('BD8','Roopa','F','M G Road','8886712333','O-ve','B01','1996-12-10',NULL),
('BD9','Virat','M','Pink Street','9886712322','AB-ve','B02','2002-01-01',NULL),
('BD10','Subbu','M','Jayanagar','9877712333','A+ve','B01','1990-09-20',NULL),
('BD11','Udupa','F','Anna Sali','9886712424','B+ve','B02','2000-11-07',NULL),
('BD12','Rish','M','KSR Road','6666712333','O+ve','B01','1991-05-15',NULL),
('BD13','Arun','M','Clone Colony','6565712333','AB+ve','B02','2002-12-10',NULL),
('BD14','Margaret','F','Mirza Road','9886111333','B+ve','B03','1979-08-15',NULL),
('BD15','Irani','F','T Nagar','9886712111','O+ve','B02','1997-01-31',NULL);


INSERT into DONATE_BLOOD VALUES('AB+ve','B03','BD2','10','2019-01-10'),
('B+ve','B02','BD3','15','2022-10-01'),
('AB-ve','B02','BD9','5','2022-10-01'),
('A+ve','B01','BD10','10','2019-01-10'),
('O+ve','B01','BD12','20','2022-12-22'),
('AB-ve','B02','BD9','10','2021-11-30'),
('O+ve','B02','BD15','10','2020-04-16'),
('A-ve','B03','BD5','15','2022-12-20'),
('O+ve','B03','BD7','12','2021-07-30'),
('AB-ve','B03','BD9','13','2021-11-16'),
('AB+ve','B03','BD2','15','2022-01-20'),
('O+ve','B01','BD12','10','2020-10-02'),
('B+ve','B01','BD3','10','2019-01-20');


INSERT into HOSPITAL VALUES('Mayoclinic','H01','Jayanagar','9222333558'),
('Alexa','H02','JP Nagara','9333555777'),
('Siri','H03','Girinagar','93335557722'),
('ValueView','H04','Street Road','9311555777'),
('MothersPalace','H05','M G Road','9111555777'),
('UnityClinics','H06','RR Nagar','9333555444');


INSERT into ORDERS VALUES('A+ve','10','H01','B02'),
('A+ve','10','H01','B03'),
('AB+ve','5','H02','B01'),
('B+ve','10','H03','B02'),
('O+ve','10','H05','B03');



