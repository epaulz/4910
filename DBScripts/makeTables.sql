CREATE TABLE ACCOUNT
(
	ID			INT				NOT NULL	AUTO_INCREMENT,
	Username	VARCHAR(30)		NOT NULL,
	Pass		VARCHAR(100)	NOT NULL,
	PRIMARY KEY(ID)
);
CREATE TABLE ADMINS
(
	AID			INT			NOT NULL,
	AdminNum	INT,
	PRIMARY KEY(AID),
	FOREIGN KEY(AID) REFERENCES ACCOUNT(ID)
);
CREATE TABLE SPONSOR
(
	AID			INT			NOT NULL,
	CompName	VARCHAR(30),
	PtVal		INT		NOT NULL,
	AdminID		INT,
	MonthEarn	DECIMAL(9,2),
	MonthPay	DECIMAL(9,2),
	PRIMARY KEY(AID),
	FOREIGN KEY(AID) REFERENCES ACCOUNT(ID),
	FOREIGN KEY(AdminID) REFERENCES ADMINS(AID)
);
CREATE TABLE DRIVER
(
	AID			INT			NOT NULL,
	Fname		VARCHAR(30),
	Lname		VARCHAR(30),
	Points		DECIMAL(10,2),
	Reputation	VARCHAR(30),
	StartDate	DATE,
	SponID		INT,
	PRIMARY KEY(AID),
	FOREIGN KEY(AID) REFERENCES ACCOUNT(ID),
	FOREIGN KEY(SponID) REFERENCES SPONSOR(AID)
);
CREATE TABLE ITEMS
(
	ID			INT			NOT NULL,
	Item_Name	VARCHAR(30),
	Link		VARCHAR(100),
	Cost		Decimal(7,2),
	SponID		INT,
	PRIMARY KEY(ID),
	FOREIGN KEY(SponID) REFERENCES SPONSOR(AID)
);
CREATE TABLE BUYS
(
	DrivID		INT			NOT NULL,
	ItemID		INT			NOT NULL,
	BDate		DATE,
	PRIMARY KEY(DrivID,ItemID),
	FOREIGN KEY(DrivID) REFERENCES DRIVER(AID),
	FOREIGN KEY(ItemID) REFERENCES ITEMS(ID)
);
CREATE TABLE PAYCHECKS
(
	CheckID		INT			NOT NULL,
	Amount		DECIMAL(5,2),
	PDate		DATE,
	SponID		INT,
	AdminID		INT,
	PRIMARY KEY(CheckID),
	FOREIGN KEY(SponID) REFERENCES SPONSOR(AID),
	FOREIGN KEY(AdminID) REFERENCES ADMINS(AID)
);