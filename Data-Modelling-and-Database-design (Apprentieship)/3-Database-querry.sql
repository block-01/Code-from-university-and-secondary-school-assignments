-- Outputs all of the data in the database before the changes are made
SELECT * FROM `UNI_Assignment_DMDD_Testing_DB_1`.`CodeRepo`;
SELECT * FROM `UNI_Assignment_DMDD_Testing_DB_1`.`DateTime`;
SELECT * FROM `UNI_Assignment_DMDD_Testing_DB_1`.`Error`;
SELECT * FROM `UNI_Assignment_DMDD_Testing_DB_1`.`LogPath`;
SELECT * FROM `UNI_Assignment_DMDD_Testing_DB_1`.`Main`;
SELECT * FROM `UNI_Assignment_DMDD_Testing_DB_1`.`OperatingSystem`;
SELECT * FROM `UNI_Assignment_DMDD_Testing_DB_1`.`Users`;

SELECT AVG(`Durration (mins)`) 
FROM `UNI_Assignment_DMDD_Testing_DB_1`.`DateTime`; -- Outputs the average of the duration collumn in the DateTime table

SELECT MIN(`Durration (mins)`) 
FROM `UNI_Assignment_DMDD_Testing_DB_1`.`DateTime`; -- Outputs the smallest number (shortest time) in the duration collumn in the DateTime table

SELECT MAX(`Durration (mins)`) 
FROM `UNI_Assignment_DMDD_Testing_DB_1`.`DateTime`; -- Outputs the largest number (lognest time) in the duration collumn in the DateTime table

SELECT COUNT(*) 
FROM `UNI_Assignment_DMDD_Testing_DB_1`.`Main`; -- Outputs the number of rows in the Main table


-- Inner Join that joins the LogPath and Users tables
SELECT `UNI_Assignment_DMDD_Testing_DB_1`.`LogPath`.`LogID`, `UNI_Assignment_DMDD_Testing_DB_1`.`LogPath`.`Path`, `UNI_Assignment_DMDD_Testing_DB_1`.`LogPath`.`UserID`
FROM `UNI_Assignment_DMDD_Testing_DB_1`.`LogPath`
INNER JOIN `UNI_Assignment_DMDD_Testing_DB_1`.`Users` ON `UNI_Assignment_DMDD_Testing_DB_1`.`LogPath`.`LogID` = `UNI_Assignment_DMDD_Testing_DB_1`.`Users`.`UserID`;

-- Subquerry that outputs the ID and Status for row when Status is "Finished"
SELECT `ID`,`Status` FROM `UNI_Assignment_DMDD_Testing_DB_1`.`Main`
WHERE `Status`="Finished";

-- Manipulates the database by changing all occurances of `2` in the `UserID` collumn to a `1` and then deletes the row with the UserID of 2 from the `Users` Table.

SELECT * FROM `UNI_Assignment_DMDD_Testing_DB_1`.`Main`;
UPDATE `UNI_Assignment_DMDD_Testing_DB_1`.`Main`
SET `UserID`="1" 
WHERE `UserID`="2";
SELECT * FROM `UNI_Assignment_DMDD_Testing_DB_1`.`Main`;

SELECT * FROM `UNI_Assignment_DMDD_Testing_DB_1`.`LogPath`;
UPDATE `UNI_Assignment_DMDD_Testing_DB_1`.`LogPath`
SET `UserID`="1" 
WHERE `UserID`="2";
SELECT * FROM `UNI_Assignment_DMDD_Testing_DB_1`.`LogPath`;

SELECT * FROM `UNI_Assignment_DMDD_Testing_DB_1`.`CodeRepo`;
UPDATE `UNI_Assignment_DMDD_Testing_DB_1`.`CodeRepo`
SET `UserID`="1" 
WHERE `UserID`="2";
SELECT * FROM `UNI_Assignment_DMDD_Testing_DB_1`.`CodeRepo`;

-- Deletes the row from the User table
SELECT * FROM `UNI_Assignment_DMDD_Testing_DB_1`.`Users`;
DELETE FROM `UNI_Assignment_DMDD_Testing_DB_1`.`Users`
WHERE `UserID`="2";
SELECT * FROM `UNI_Assignment_DMDD_Testing_DB_1`.`Users`;

-- Sets up a view for added security so that a public user can only see curtain bit of information such as the ID, Status and what the Error was.

CREATE VIEW `UNI_Assignment_DMDD_Testing_DB_1`.`public`
AS
SELECT `ID`, `Status`, `ErrorID`
From `UNI_Assignment_DMDD_Testing_DB_1`.`Main`;

SELECT * FROM `UNI_Assignment_DMDD_Testing_DB_1`.`public`;
