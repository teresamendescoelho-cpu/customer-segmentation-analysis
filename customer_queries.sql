SELECT *
FROM customers;

SELECT *
FROM customers
WHERE SpendingScore > 75;

SELECT AVG(AnnualIncome)
FROM customers;

SELECT Gender,
       AVG(SpendingScore)
FROM customers
GROUP BY Gender;
