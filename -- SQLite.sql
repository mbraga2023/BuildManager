-- SQLite
CREATE TABLE usuarios (
id INTEGER PRIMARY KEY,
nome TEXT NOT NULL,
sobrenome TEXT NOT NULL,
email TEXT NOT NULL UNIQUE,
phone TEXT NOT NULL UNIQUE,
unit TEXT NOT NULL,
adm BOOL NOT NULL,
senha TEXT NOT NULL);
   
INSERT INTO residentes (nome, sobrenome, email, phone, unit, password) 
VALUES ('admin', 'admin', 'michel.diener@gmail.com', '786-685-0255','101','admin');
