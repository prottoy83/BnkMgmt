-- CREATE TABLE users(id INT PRIMARY_KEY, 
--                     name TEXT NOT NULL, 
--                     address TEXT NOT NULL, 
--                     contact TEXT NOT NULL, 
--                     username TEXT NOT NULL UNIQUE, 
--                     pass TEXT NOT NULL);

INSERT INTO users(id,name,address,contact,username,pass)
VALUES (2,'Rifat Hossain', 'Dhaka', '01884748394', 'rifath077', 'weakpass');


SELECT * FROM users