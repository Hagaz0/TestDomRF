CREATE TABLE pays (
    email VARCHAR(255),
    date DATE,
    sub_id INT,
    sum INT
);

INSERT INTO pays
VALUES ('g8879@...', '02/01/2021', 1234, 10),
       ('g8879@...', '02/02/2021', 1234, 20),
       ('g8879@...', '02/03/2021', 1234, 30),
       ('g8879@...', '02/04/2021', 1234, 20),
       ('g8879@...', '02/05/2021', 55, 50),
       ('g8879@...', '02/06/2021', 55, 45),
       ('56hh@...', '02/01/2021', 1234, 10),
       ('56hh@...', '02/02/2021', 1324, 20),
       ('56hh@...', '02/03/2021', 1234, 30),
       ('56hh@...', '02/04/2021', 1234, 40),
       ('56hh@...', '02/05/2021', 55, 50),
       ('56hh@...', '02/06/2021', 55, 60),
       ('56hh@...', '02/07/2021', 55, 60);

SELECT email, date, sub_id, sum
FROM (
  SELECT email, date, sub_id, sum, ROW_NUMBER() OVER (PARTITION BY email ORDER BY date) AS row_num
  FROM pays
) subquery
WHERE row_num = 2;

