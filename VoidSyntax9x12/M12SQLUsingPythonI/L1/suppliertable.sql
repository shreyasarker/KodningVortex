CREATE TABLE supplier (
    SNO INT PRIMARY KEY,
    NAME TEXT,
    STATUS INT,
    CITY TEXT
);

INSERT INTO supplier (SNO, NAME, STATUS, CITY) VALUES
(1, 'Smith', 20, 'London'),
(2, 'Jones', 10, 'Paris'),
(3, 'Blake', 30, 'Paris'),
(4, 'Clarke', 20, 'London'),
(5, 'Adams', 30, 'Athens');

SELECT * FROM supplier;