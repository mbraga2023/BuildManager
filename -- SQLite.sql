-- SQLite
CREATE TABLE residentes (
id INTEGER PRIMARY KEY,
nome TEXT NOT NULL,
sobrenome TEXT NOT NULL,
email TEXT NOT NULL UNIQUE,
phone TEXT NOT NULL UNIQUE,
unit TEXT NOT NULL);

   
INSERT INTO residentes (nome, sobrenome, email, phone, unit) 
VALUES ('Michel', 'Braga', 'michel.diener@gmail.com', '786-685-0255','101');

ALTER TABLE users MODIFY COLUMN username_email TEXT AFTER sobrenome;
