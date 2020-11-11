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
    Price DECIMAL(10,2) UNSIGNED,
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
       
    
DROP TABLE Prices;
DROP TABLE Languages;
DROP TABLE Quality;
DROP TABLE Publications;
DROP TABLE Publishers;
DROP TABLE Authors;
DROP TABLE Books;

SHOW PROCESSLIST;

SELECT * FROM Prices;
SELECT * FROM Languages;
SELECT * FROM Quality;
SELECT * FROM Publishers;
SELECT * FROM Authors;
SELECT * FROM Books;
