create table data (
	name varchar(255),
    pwd varchar(255),
    id int unique AUTO_INCREMENT,
    groupId int,
    vacStart date,
    vacEnd date,
    cityStart date,
    cityEnd date,
    university varchar(255));
    
create table grps (
	grpName varchar(255),
    groupId int unique AUTO_INCREMENT,
    leaderId int,
    city varchar(255));
    
select * from data;

insert into data(name) values("Dev");

drop table data;
drop table grps;