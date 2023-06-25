/* Вариант 1 */

SELECT * FROM table1
UNION
SELECT * FROM table2
ORDER BY 2;

/* Вариант 2 */

CREATE TABLE table3 (
    Num INT,
    Name VARCHAR(255),
);

INSERT INTO table3 (Num, Name)
    SELECT * FROM table1
    UNION
    SELECT * FROM table2
    ORDER BY 2;