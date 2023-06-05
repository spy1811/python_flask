create database leave_management;
use leave_management
show tables;
drop database vishakatext
drop table leave
select * from user
truncate table user
select * from branch_master
select * from staff_master
select * from workload
select * from staff

insert into user(uemail)


select * from leaves
truncate table leaves
select * from leaves as lv join staff_master as sm on lv.staff_id = sm.id join leave_master as lm on lv.leave_id = lm.id where lv.approve_level='Admin'
select * from principle
select * from leave_master
select * from leave_track
select * from leaves as lv join staff_master as sm on lv.staff_id = sm.id join leave_master as lm on lv.leave_id = lm.id
select * from leaves as lv join leave_track as lt on lv.staff_id = lt.id join user as us on lv.leave_id = us.id where lv.id=1
desc leave_master
desc leaves
delete from staff_master where id=2
delete from leave_track
alter table admin modify column aphone integer;
select * from leave_master

insert into branch_master values(1,'Computer Science and Technology',1310)
insert into principle (pname,pemail,pphone) values('Rohit','rohitmadas@gmail.com','8421466569')
insert into staff_master(sname,semail,sphone,spost) values('Rohit','rohitmadas@gmail.com','8421466569','Professor')
insert into user(uemail,upassword,user_type,status)values('admin@gmail.com','admin@123','Admin','Active')
update leaves set approve_level='Principle' where id=1
update user set user_type='HOD' where id=5
drop table branch_master
truncate table user
select * from user
select * from admin
select * from principle
select * from branch_master
select * from notice_board
alter table notice_board add notice_content varchar(100)
select * from leave
show tables
 