
drop table if exists User;
drop table if exists Language;
drop table if exists Project;
drop table if exists ProjectMember;
drop table if exists TimeLog;


create table User (
	id int not null,
	username varchar(100),
	password varchar(100),
	primary key (id)
);

create table Language (
	id int not null,
	name varchar(100),
	primary key (id)
);

create table Project (
	id int not null,
	name varchar(100),
	createdby int,
	primary key (id),
	foreign key (createdby) references User
);

create table ProjectMember (
	projectID int not null,
	userID int not null,
	primary key (projectID, userID),
	foreign key (projectID) references Project,
	foreign key (userID) references User
);

create table TimeLog (
	userID int not null,
	logID int not null,
	projectID int,
	languageID int,
	timeLogged int not null,
	primary key (userID, logID),
	foreign key (userID) references User,
	foreign key (projectID) references Project,
	foreign key (languageID) references Language
);


insert into User (id, username, password)
values 
	(1, 'user_1', 'password_1'),
	(2, 'user_2', 'password_2'),
	(3, 'user_3', 'password_3');

insert into Language (id, name)
values
	(1, 'C'),
	(2, 'C++'),
	(3, 'C#'),
	(4, 'Java'),
	(5, 'Python'),
	(6, 'Lua'),
	(7, 'Julia'),
	(8, 'Bash'),
	(9, 'Ruby');


insert into Project (id, name, createdby)
values
	(1, "user_1's first project", 1),
	(2, "user_1's second project", 1),
	(3, "user_2's project", 2);

insert into ProjectMember (projectID, userID)
values
	(1, 1),
	(1, 2),
	(1, 3),
	(2, 1),
	(3, 2),
	(3, 3);

insert into TimeLog (userID, logID, projectID, languageID, timeLogged)
values
	-- user_1 working on project 1
	(1, 1, 1, 1, 20),
	(1, 2, 1, 1, 300),
	(1, 3, 1, 5, 70),
	-- user_2 working on project 1
	(2, 1, 1, 1, 10),
	(2, 2, 1, 9, 10),
	-- user_3 working on project 1
	(3, 1, 1, 8, 10),
	(3, 2, 1, 7, 10),

	-- users working on non-projects
	(1, 4, null, 3, 10),
	(1, 5, null, 3, 10),
	(1, 6, null, 3, 10);


