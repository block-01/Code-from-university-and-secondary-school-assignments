-- Owner
INSERT INTO `UNI_Assignment_DMDD_Testing_DB_1`.`Users` (`UserID`,`Name`,`DateCreated`) 
VALUES
(1,'new-name','31/03/24'),
(2,'old-name','28/04/24'),
(3,'Dave','01/05/24'),
(4,'Mily','15/05/24'),
(5,'Bob','02/05/24'),
(6,'Emma','28/06/24');
D

-- Time and date
INSERT INTO `UNI_Assignment_DMDD_Testing_DB_1`.`DateTime` (`TimeDateID`,`Date (dd/mm/yy)`,`Durration (mins)`)
VALUES
(1,'31/03/24',101),
(2,'01/05/24',12),
(3,'20/05/24',1),
(4,'28/04/24',15),
(5,'10/05/24',89),
(6,'28/05/24',64),
(7,'16/05/24',32),
(8,'15/05/24',16),
(9,'02/05/24',8),
(10,'24/05/24',4),
(11,'01/06/24',2),
(12,'30/06/24',1);

-- Logpath
INSERT INTO `UNI_Assignment_DMDD_Testing_DB_1`.`LogPath` (`LogID`,`Path`,`TimeDateID`,`UserID`) 
VALUES 
(1,'/home/logs/1010.log','1',1),
(2,'/home/logs/1111.log','2',3),
(3,'/home/logs/1212.log','3',1),
(4,'/home/logs/1313.log','4',2),
(5,'/home/logs/1414.log','5',1),
(6,'/home/logs/1515.log','6',3),
(7,'/home/logs/1616.log','7',4),
(8,'/home/logs/1717.log','8',1),
(9,'/home/logs/1818.log','9',5),
(10,'/home/logs/1919.log','10',6),
(11,'/home/logs/2020.log','11',5),
(12,'/home/logs/2121.log','12',3);

-- Extra details
INSERT INTO `UNI_Assignment_DMDD_Testing_DB_1`.`Error` (`ErrorID`,`Name`,`Details`)
VALUES 
(1,'OS Error', 'A Error with the operating System'),
(2,'Package Error', 'A Error within a dependency'),
(3,'Syntax Error', 'A Error'),
(4,'Build Error','A Error in the Build');


-- Code Repository
INSERT INTO `UNI_Assignment_DMDD_Testing_DB_1`.`CodeRepo` (`RepoID`,`Name`,`UserID`,`URL`) 
VALUES 
(1,'Greg-pack',1,'https://github.com/block-01/Gregtech-Quseting-Pack-1.12.2'),
(2,'Game',1,'https://github.com/block-01/Game'),
(3,'GitLab-assignment',2,'https://block-gitlab.srvp.ro/block_01/Code-from-university-and-secondary-school-assignments'),
(4,'random',3,'https://random/url/wont/work.com'),
(5,'Assignment',1,'https://github.com/block-01/Code-from-university-and-secondary-school-assignments');

-- Operating System
INSERT INTO `UNI_Assignment_DMDD_Testing_DB_1`.`OperatingSystem` (`OSID`,`Name`,`Version`,`URL`) 
VALUES 
(1,'Arch-linux','2024.06.01','https://archlinux.org/download/'),
(2,'Ubuntu LTS','22.04','https://releases.ubuntu.com/jammy/ubuntu-22.04.4-live-server-amd64.iso'),
(3,'Windows 11','23H2','https://go.microsoft.com/fwlink/?linkid=2171764'),
(4,'Windows 10','22H2','https://www.microsoft.com/en-gb/software-download/windows10ISO');

-- Main
INSERT INTO `UNI_Assignment_DMDD_Testing_DB_1`.`Main` (`ID`,`LogID`,`UserID`,`RepoID`,`TimeDateID`,`OSID`,`Status`,`ErrorID`) 
VALUES 
(1,1,1,5,'1',1,'Finished',NULL),
(2,2,3,3,'2',3,'Not Started',NULL),
(3,3,1,5,'3',2,'Failed',2),
(4,4,2,3,'4',2,'Finished',NULL),
(5,5,1,5,'5',1,'Failed',2),
(6,6,3,2,'6',4,'Finished',NULL),
(7,7,4,1,'7',2,'Finished',4),
(8,8,1,5,'8',1,'Not Started',NULL),
(9,9,5,4,'9',4,'Finished',NULL),
(10,10,6,3,'10',2,'Failed',3),
(11,11,5,2,'11',3,'Failed',1),
(12,12,3,2,'12',1,'Finished',NULL);

-- Outputs all of the data in the database
SELECT * FROM `UNI_Assignment_DMDD_Testing_DB_1`.`CodeRepo`;
SELECT * FROM `UNI_Assignment_DMDD_Testing_DB_1`.`DateTime`;
SELECT * FROM `UNI_Assignment_DMDD_Testing_DB_1`.`Error`;
SELECT * FROM `UNI_Assignment_DMDD_Testing_DB_1`.`LogPath`;
SELECT * FROM `UNI_Assignment_DMDD_Testing_DB_1`.`Main`;
SELECT * FROM `UNI_Assignment_DMDD_Testing_DB_1`.`OperatingSystem`;
SELECT * FROM `UNI_Assignment_DMDD_Testing_DB_1`.`Users`;
