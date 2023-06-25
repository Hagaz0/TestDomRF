CREATE TABLE active_clients (
    report_month DATE,
    client_id INT
);

INSERT INTO active_clients
VALUES ('01/01/2018', 1847982357),
       ('01/01/2018', 938475),
       ('02/01/2018', 1847982357),
       ('02/01/2018', 184),
       ('03/01/2018', 184),
       ('03/01/2018', 1847982357),
       ('03/01/2018', 184442),
       ('04/01/2018', 12345),
       ('04/01/2018', 184),
       ('05/01/2018', 35732),
       ('06/01/2018', 12357),
       ('07/01/2018', 1847982357);

WITH max_date AS (
    SELECT max(report_month) AS date
    FROM active_clients
), all_checks AS (
       SELECT report_month,
              active_clients.client_id,
              CASE WHEN ((report_month + INTERVAL '1 month')::date, active_clients.client_id) IN
                 (SELECT report_month AS month, client_id from active_clients) THEN 1 ELSE 0 END AS month_1,
              CASE WHEN ((report_month + INTERVAL '2 month')::date, active_clients.client_id) IN
                 (SELECT report_month AS month, client_id from active_clients) THEN 1 ELSE 0 END AS month_2,
              CASE WHEN ((report_month + INTERVAL '3 month')::date, active_clients.client_id) IN
                 (SELECT report_month AS month, client_id from active_clients) THEN 1 ELSE 0 END AS month_3,
              CASE WHEN EXTRACT(MONTH FROM AGE(max_date.date, report_month)) +  12 * EXTRACT(YEAR FROM AGE(max_date.date, report_month)) >= 3
                 THEN 'yes'
                 ELSE 'no'
                 END AS delta
       FROM active_clients, max_date
       ORDER BY 1),
    all_ottok AS (
       SELECT report_month AS month, coalesce(count(client_id), 0) AS ottek
       FROM all_checks
       WHERE delta = 'yes' AND month_1 = 0 AND month_2 = 0 AND month_3 = 0
       GROUP BY report_month
), active_in_month AS (
       SELECT active_clients.report_month as month, coalesce(COUNT(client_id), 0) AS active_users
       FROM active_clients
       GROUP BY active_clients.report_month
       ORDER BY 1)

SELECT active_in_month.month, active_users, coalesce((100 * ottek / active_users), 0) as persent_ottekshih
FROM active_in_month
LEFT JOIN all_ottok ON active_in_month.month = all_ottok.month
