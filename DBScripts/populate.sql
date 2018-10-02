insert into ACCOUNT
values  (1,'driver','Imadriver'),
        (2,'sponsor','Imasponsor'),
        (3,'admin','Imanadmin');

insert into ADMINS
values  (3,1);

insert into SPONSOR
values  (2,'Clemson University',1,3,100.00,1.00);

insert into DRIVER
values  (1,'Aidan','Isner',10,'Good','2018-09-20',2);

insert into ITEMS
values  (1,'Something','www.something.com',28.00,2);

insert into BUYS
values  (1,1,'2018-09-20');

insert into PAYCHECKS
values  (1,1.00,'2018-09-20',2,3);