-- AGGREGATE FUNCTION

-- SUM
-- Display the total units of blood donated by donor with bdid=BD10 to blood bank with bbid=BD01  
select bloodD_id,SUM(units) as Total_units_donated,bloodB_id
from DONATE_BLOOD where DONATE_BLOOD.bloodD_id='BD10' AND DONATE_BLOOD.bloodB_id='B01';
-- COUNT
-- Retrive the number of donors registered to each of the blood bank.
select COUNT(bd_id),bbank_id from BLOOD_DONOR GROUP BY bbank_id;
-- Retrive the number of donors who donated blood to each of the blood bank.
select COUNT(bloodD_id),bloodB_id, donated_date from DONATE_BLOOD GROUP BY donated_date;




-- CORRELATED QUERIES

-- -- Update age attribute in blood donor
-- UPDATE blood_donor SET Age=DATE_FORMAT(FROM_DAYS(DATEDIFF(now(),Date_of_birth)),'%Y')+0;
-- CORRELATED EXISTS AND NOT EXISTS
-- Display the emplyoee id,name and blood bank id that he manages blood bank B02    .
select e_id,e_name,bloodbank_id from employee as e where EXISTS(
    select m_id,bb_id from BLOOD_BANK as b where b.m_id=e.e_id and b.bb_id='B02'
);
-- Display the emplyoee id,name and blood bank id of employees  working for bloodbank 'B03' and they are not having manager status.
select e_id,e_name,bloodbank_id from employee as e where e.bloodbank_id='B03' and  NOT EXISTS(
    select m_id,bb_id from BLOOD_BANK as b where b.m_id=e.e_id and b.bb_id='B03'
);

-- REGULAR JOIN

-- NATURAL JOIN
-- --Retrive details if required blood by hospital is available in blood bank which it requested
select * from orders NATURAL JOIN BLOOD_TYPE where availabile='yes' and required_bg=bloodgroup and bloodbank_id=bldbank_id;


-- INNER JOIN

-- Retrive details of all donor who donated bloodgroup O+ve
select bd_name,bd_address,bd_id,bd_Bgroup,bloodB_id,Donated_date from BLOOD_DONOR JOIN DONATE_BLOOD 
ON BLOOD_DONOR.bd_id=DONATE_BLOOD.bloodD_id and DONATE_BLOOD.blood_group='O+ve';
-- Retrive the id of hospital who requested for bloodbank to give blood.
select hospital_id ,bb_id from ORDERS JOIN BLOOD_BANK ON BLOOD_BANK.bb_id=ORDERS.bloodbank_id;
-- EQUI JOIN
--Retrive details of the blood donor who donated on particular date()
select bd_name,bd_address,bd_id from BLOOD_DONOR JOIN DONATE_BLOOD 
ON BLOOD_DONOR.bd_id=DONATE_BLOOD.bloodD_id where DONATE_BLOOD.Donated_date='2022-01-20';



-- NESTED QUERIES

-- Retrive details of hospital who had not requested the blood bank for blood group
select h_id,h_name,h_phone from hospital 
where h_id NOT IN(select h_id from 
hospital JOIN orders ON hospital.h_id=orders.hospital_id);
-- Retrive details of all donor who had not donated blood
select bd_id,bd_name,bd_phone,bd_Bgroup from BLOOD_DONOR where bd_id NOT IN
(select bd_id from BLOOD_DONOR JOIN DONATE_BLOOD on
BLOOD_DONOR.bd_id=DONATE_BLOOD.bloodD_id);


-- SET OPERATION

-- Retrive the manager  of all the blood bank
select m_id,bb_id from BLOOD_BANK INTERSECT select e_id,bloodbank_id from employee;
-- Retrive the all the blood bank and hospital along with its address
select bb_id,bb_address from BLOOD_BANK UNION select h_id,h_address from hospital;



-- VIEWS
-- create view of blood donor as eligible donor  whose age is in between 18 and 60 
create VIEW eligible_donor as select bd_id,bd_name,bd_Bgroup,age from blood_donor where blood_donor.age>'18' and blood_donor.age<'60';
-- Retrive details of blooddonor whose age is 33
select bd_id,bd_name,bd_Bgroup,age from eligible_donor where age='33';


DELIMITER $$
CREATE procedure update_age ()
BEGIN
DECLARE cur date;
select sysdate() into cur;
update blood_donor
SET age=year(cur)-year(Date_of_birth);
END ; $$
DELIMITER ;
call update_age();


DELIMITER $$
CREATE FUNCTION check1_donor(ageup int)
BEGIN
DECLARE message VARCHAR(255);
select age from blood_donor where age=ageup;
if age>60 then 
   SET message="Cannot donate blood";
   SIGNAL SQLSTATE '45000'
        SET  MESSAGE_TEXT=message;
  END IF;

END; $$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER check_age
BEFORE UPDATE
ON blood_donor FOR EACH ROW
BEGIN   
-- DECLARE error_msg VARCHAR(255);
-- SET error_msg = 
call check1_donor(blood_donor.age); 
-- SIGNAL SQLSTATE '45000'
-- SET MESSAGE_TEXT = error_msg;
END; $$
DELIMITER ;

DELIMITER $$
CREATE TRIGGER check_age
BEFORE INSERT
ON blood_donor FOR EACH ROW
BEGIN   
call check1_donor(blood_donor.age); 
END IF;
END; $$



delimiter $$
CREATE TRIGGER  Check_age  
BEFORE INSERT ON blood_donor 
FOR EACH ROW
BEGIN
IF blood_donor.age < 18 THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = 'ERROR: 
         AGE MUST BE ATLEAST 18 YEARS!';
END IF;
END; $$
delimiter ; 


DELIMITER $$
CREATE TRIGGER register_donor
BEFORE INSERT
ON blood_donor FOR EACH ROW
BEGIN
DECLARE error_msg VARCHAR(255);
SET error_msg = ('Cannot insert');
IF  (select age from blood_donor where bd_id = new.bd_id )<18 THEN
SIGNAL SQLSTATE '45000'
SET MESSAGE_TEXT = error_msg;
END IF;
END $$
DELIMITER ;


DELIMITER $$

CREATE TRIGGER before_accounts_update
BEFORE UPDATE
ON accounts FOR EACH ROW
BEGIN
    CALL withdraw(
        OLD.accountId, 
        OLD.amount - NEW.amount
    );
END$$

DELIMITER ;