CREATE TABLE Books(
    Book_ID BIGINT UNSIGNED NOT NULL,
    Title VARCHAR(255) NOT NULL,
    Release_Date INT,
    Location VARCHAR(255),
    PRIMARY KEY(Book_ID));
  

CREATE TABLE Authors(
    Author_ID BIGINT UNSIGNED NOT NULL,
    Name VARCHAR(255) NOT NULL,
    Notes LONGTEXT,
    PRIMARY KEY(Author_ID));  
   
   
CREATE TABLE Prices(
    Book_ID BIGINT UNSIGNED NOT NULL,
    Price DECIMAL(10,2) ZEROFILL NOT NULL,
    PRIMARY KEY(Book_ID, Price),
    CONSTRAINT fk_book_id
        FOREIGN KEY (Book_ID) REFERENCES Books (Book_ID)
        ON DELETE CASCADE
        ON UPDATE RESTRICT);
       

CREATE TABLE Publishers(
    Book_ID BIGINT UNSIGNED NOT NULL,
    Publisher VARCHAR(255),
    PRIMARY KEY(Book_ID),
    CONSTRAINT fk_book_id_2
        FOREIGN KEY(Book_ID)
        REFERENCES Books(Book_ID)
        ON DELETE CASCADE
        ON UPDATE RESTRICT);
        
       
CREATE TABLE Publications(
    Author_ID BIGINT UNSIGNED NOT NULL,
    Book_ID BIGINT UNSIGNED NOT NULL,
    PRIMARY KEY(Author_ID, Book_ID),
    CONSTRAINT fk_author_id
        FOREIGN KEY(Author_ID)
        REFERENCES Authors(Author_ID)
        ON DELETE CASCADE
        ON UPDATE RESTRICT,
    CONSTRAINT fk_book_id3
        FOREIGN KEY(Book_ID)
        REFERENCES Books(Book_ID)
        ON DELETE CASCADE
        ON UPDATE RESTRICT);
           

CREATE TABLE Quality(
    Book_ID BIGINT UNSIGNED NOT NULL,
    Binding VARCHAR(255),
    Grade VARCHAR(255),
    PRIMARY KEY(Book_ID),
    CONSTRAINT fk_book_id4
        FOREIGN KEY(Book_ID)
        REFERENCES Books(Book_ID)
        ON DELETE CASCADE
        ON UPDATE RESTRICT);
       
       
CREATE TABLE Languages(
    Book_ID BIGINT UNSIGNED NOT NULL,
    Language VARCHAR(255),
    PRIMARY KEY(Book_ID),
    CONSTRAINT fk_book_id5
        FOREIGN KEY(Book_ID)
        REFERENCES Books(Book_ID)
        ON DELETE CASCADE
        ON UPDATE RESTRICT);
       
/*
DROP TABLE Prices;
DROP TABLE Languages;
DROP TABLE Quality;
DROP TABLE Publications;
DROP TABLE Publishers;
DROP TABLE Authors;
DROP TABLE Books;


SELECT * FROM Prices;
SELECT * FROM Languages;
SELECT * FROM Quality;
SELECT * FROM Publishers;
SELECT * FROM Authors;
SELECT * FROM Books;



SELECT a.Name, COUNT(Book_ID) AS Number_of_Books
FROM Publications p, Authors a
WHERE p.Author_ID = a.Author_ID
GROUP BY a.Name
ORDER BY a.Name


SELECT a.Name, b.Title
FROM Authors a, Books b, Publications p
WHERE p.Book_ID = b.Book_ID
    AND p.Author_ID = a.Author_ID
ORDER BY a.Name


SELECT COUNT(*)
FROM Books


SELECT Publisher, COUNT(Book_ID) AS Number_of_Books
FROM Publishers
WHERE Publisher IS NOT NULL
GROUP BY Publisher
ORDER BY Publisher

SELECT b.Book_ID
FROM Books b, Languages L, Prices pr, Publishers p, Quality q
WHERE L.Book_ID = b.Book_ID
    AND pr.Book_ID = b.Book_ID
    AND p.Book_ID = b.Book_ID
    AND q.Book_ID = b.Book_ID
    AND (b.Release_Date IS NULL
    OR b.Location IS NULL
    OR L.Language IS NULL
    OR pr.Price = 0.00
    OR p.Publisher IS NULL
    OR q.Binding IS NULL
    OR q.Grade IS NULL)




