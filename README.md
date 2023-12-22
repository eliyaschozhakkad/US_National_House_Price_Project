## End to End US National House Price Project

### Steps to run Web App

### Create an environment

```
conda create -p venv python==3.8 -y

conda activate venv/

```

### Install all necessary libraries

```
pip install -r requirements.txt
```

### Run the command to run Flask Web App

```
python app.py
```

### US National House Price Web App is ready!!

```
Open any web browser and type http://127.0.0.1:5000/ OR http://localhost:5000/
```

### Introduction About the Data :

The goal is to find publicly available data for key factors that influence US home prices nationally and build a data science model that explains how these factors impacted home prices over the last 20 years.

Use the **'S&P Case-Schiller'** Home Price Index as a proxy for home prices: [https://fred.stlouisfed.org/series/CSUSHPISA].

**There are 14 independent variables:**

- `Median Sale Price House` : The Median Sale Price of a House is the middle value of all house sale prices in a given area, providing a representative measure of central tendency.

- `Personal Income Per Capita` : Personal Income Per Capita is the average income earned by an individual in a specific geographical area or region, calculated by dividing the total personal income by the population.

- `Property Tax` : Property Tax is a local government levy on the assessed value of real estate properties, typically imposed annually as a source of revenue for funding public services and infrastructure.

- `Nasdaqcom` : NASDAQ is an American stock exchange known for its electronic trading platform, hosting a diverse array of companies, particularly in the technology sector.Here its value is considered.

- `Construction Employment Cost` : Construction Employment Cost refers to the total expenses incurred by an employer in the construction industry to compensate and provide benefits to its workforce, encompassing wages, salaries, and associated employment-related costs.

- `Population` : Population refers to the total number of individuals living in a specific geographical area, such as a country, city, or region, at a given point in time.

- `New House Units Construction` :New House Units Construction refers to the process of building and creating new residential structures or dwellings, typically measured by the number of housing units under construction within a specified area or timeframe.

- `CPI` : The Consumer Price Index (CPI) is a measure that examines the weighted average of prices of a basket of consumer goods and services, such as transportation, food, and medical care, over time, reflecting changes in the cost of living and inflation.

- `Mortage Rate` : Mortgage Rate refers to the interest rate charged by a lender on a mortgage loan, representing the cost of borrowing for the homebuyer. It is expressed as a percentage and plays a crucial role in determining the overall cost of financing a home purchase.

- `Unemployment Rate` : The Unemployment Rate is a measure that expresses the percentage of the labor force that is currently unemployed and actively seeking employment, providing an indicator of the overall health of the job market within a specific region or country.

- `Household Debt Payment` : Household Debt Payment typically refers to the total amount of money that households spend on repaying debts, including mortgages, credit card payments, and other loans. It is a measure of the financial obligations that households must meet regularly to service their existing debt.

- `Recession_Rate_Prob` : Recession Rate refers to a significant decline in economic activity across the economy, typically characterized by a decrease in gross domestic product (GDP), employment, and other economic indicators, lasting for an extended period.

- `Date Quarter` : Quarter of Year - Q1,Q2,Q3,Q4

- `Date Year` : Year from 2000 to 2023

**Target variable:**

- `S&PCase_Schiller_Index `: 'The S&P/Case-Shiller Index is a widely followed benchmark that tracks changes in the value of residential real estate in various metropolitan areas in the United States.'

**Public Dataset Source Link :**

The data were collected publically from Fred Economic data which is publicaly available.

1. Median_Sale_Price_House - https://fred.stlouisfed.org/series/MSPUS.

2. Personal_Income_Per_Capita - https://fred.stlouisfed.org/series/A792RC0Q052SBEA

3. Property_Tax - https://fred.stlouisfed.org/series/S210400

4. Nasdaqcom - https://fred.stlouisfed.org/series/NASDAQCOM

5. Construction_Employment_Cost - https://fred.stlouisfed.org/series/CIU2012300000000I

6. Population - https://fred.stlouisfed.org/series/POPTHM

7. New_House_Units_Construction - https://fred.stlouisfed.org/series/UNDCONTSA

8. Consumer Price Index(CPI) - https://fred.stlouisfed.org/series/CORESTICKM159SFRBATL

9. Mortage_Rate - https://fred.stlouisfed.org/series/MORTGAGE30US

10. Unemployment_Rate - https://fred.stlouisfed.org/series/UNRATE

11. Household_Debt_Payment - https://fred.stlouisfed.org/series/TDSP

12. Recession_Rate_Prob - https://fred.stlouisfed.org/series/RECPROUSM156N

13. S&PCase_Schiller_Index and Date - https://fred.stlouisfed.org/series/CSUSHPISA
