# Global Stock Market Analysis 

## Project Overview & Concept
The **Global Stock Market Analysis** project is an end-to-end data analytics solution designed to ingest, clean, model, and visualize daily historical trading data of 10 major global stock indices (representing over 13,000 trading records). 

By tracking liquidity, market sentiment, historical trends, and volatility across different countries, the project provides a unified multi-tool analytics experience utilizing **Microsoft Excel**, **Microsoft Power BI**, and **Tableau**.

---

### Graduation Project | Digital Egypt Pioneers Initiative (DEPI) - Data Analysis Track

**Dataset Source:** [Kaggle - Daily Global Stock Market Indicators](https://www.kaggle.com/datasets/aliiihussain/daily-global-stock-market-indicators)

---

## Project Objectives
The primary strategic and technical objectives of this project are:
* **Centralize Global Market Data:** Consolidate disparate daily trading metrics from 10 major global indices into a single, structured analytical pipeline.
* **Assess Market Volatility:** Track and quantify daily price fluctuations to help investors identify stable versus high-risk trading environments.
* **Analyze Liquidity Distribution:** Evaluate trading volumes across different countries to pinpoint where global financial capital and liquidity are concentrated.
* **Decipher Market Sentiment:** Create automated classifications (Bullish/Bearish) to monitor daily market direction trends over time.
* **Demonstrate Multi-Tool Proficiency:** Showcase comprehensive data analytical capabilities by delivering cohesive, specialized dashboards using Microsoft Excel, Power BI, and Tableau.


---

##  Project Contributors

We are pleased to introduce the team members collaborating on this project:

| Full Name | GitHub Account |
| :---: | :---: |
| **Hazem Shady Nasr** | [@HazemShady](https://github.com/HazemShady) |
| **Merna Elia Abdelmaboud** | [@mernaelia](https://github.com/mernaelia) |
| **Mostafa Mohamed Elbohoty** | [@MostafaElbohoty97](https://github.com/MostafaElbohoty97) |
| **Mohamed Sobhi Ibrahim** | [@mohamedabofoul](https://github.com/mohamedabofoul) |
| **Injy Makarem Abd elmenaem** | [@injymakarem](https://github.com/injymakarem) |
| **Ayatullah Ahmed Sallam** | [@AyatullahSallam](https://github.com/AyatullahSallam) |


---

## Data Dictionary & Schema
The dataset consists of **13,050+ rows** of historical daily stock market records. Below is the technical schema of the attributes analyzed:

| Column Name | Data Type | Description |
| :--- | :--- | :--- |
| `Date` | Date | The specific trading day (YYYY-MM-DD format). |
| `Index_Name` / `Stock Index` | Text | Name of the global stock index (e.g., S&P 500, FTSE 100, Nikkei 225). |
| `Country` | Text | The country where the stock index exchange is located. |
| `Open` | Decimal | The opening price of the index on that trading day. |
| `High` | Decimal | The highest price recorded during the trading session. |
| `Low` | Decimal | The lowest price recorded during the trading session. |
| `Close` | Decimal | The closing price of the index (used as the primary benchmark). |
| `Volume` | Integer | The total number of shares/units traded (representing market liquidity). |
| `Daily Return` | Decimal | Calculated percentage of gain/loss compared to the previous session. |
| `Volatility` | Decimal | Calculated index price fluctuation metric. |
| `Market Sentiment` | Text | Classification of the day's trend (`Bullish` if Close > Open, `Bearish` if Close < Open). |

---

# Project Implementation & Tooling

## Phase 1: Power BI

This project features an interactive Power BI dashboard designed to analyze global stock market trends by studying financial index data across multiple countries. It assists investors and data analysts in tracking market movements, comparing performance across countries, and analyzing trading volumes, returns, and price trends over time.

The dashboard is built with fully interactive elements, allowing users to seamlessly filter data by country, year, month, or index name to extract key insights and drive data-backed investment decisions.

---

#### Key Performance Indicators (KPIs) & DAX Measures

The dashboard utilizes specialized DAX measures to calculate critical financial metrics dynamically:

##### 1. Total Markets
* **Formula:** `Total Markets = DISTINCTCOUNT(Sheet1[Index_Name])`
* **Description:** Calculates the total number of unique stock markets or indices present in the dataset.
* **Value:** Helps track the scale of the dataset and the number of active markets under analysis.

##### 2. Average Close Price
* **Formula:** `Average Close = AVERAGE(Sheet1[Close])`
* **Description:** Calculates the average closing price across selected records.
* **Value:** Measures the overall average baseline performance of indices during the selected period.

##### 3. Max Close
* **Formula:** `Max Close = MAX(Sheet1[Close])`
* **Description:** Calculates the highest closing price recorded.
* **Value:** Pinpoints the peak value achieved by the stock index within the filtered timeframe.

##### 4. Min Close
* **Formula:** `Min Close = MIN(Sheet1[Close])`
* **Description:** Calculates the lowest closing price recorded.
* **Value:** Identifies the minimum baseline value recorded for the index.

##### 5. Average Return
* **Formula:** `Average Return = AVERAGE(Sheet1[Daily_Return])`
* **Description:** Calculates the average daily return.
* **Value:** Evaluates the overall average profitability or loss rate of the selected indices.

##### 6. Total Volume
* **Formula:** *Standard Sum aggregation on the Volume column*
* **Description:** Calculates the total cumulative trading volume.
* **Value:** Measures overall market activity, transaction density, and trading liquidity.

---

#### Dashboard Interactive Filters (Slicers)

* **Slicer (Index Name):** Filters all visuals to focus on a specific stock index's performance.
* **Slicer (Month):** Enables month-by-month historical analysis.
* **Slicer (Year):** Filters the dataset to display annual performance.
* **Slicer (Country):** Filters the dashboard to display metrics for a specific country.

---

#### Visualizations & Analytical Insights

##### 1. Market Trend Analysis
* **Close Price Over Time (Area Chart):**
  * **Description:** Visualizes the fluctuations of the average closing price across years.
  * **Value:** Tracks long-term market trends to quickly determine if the market is overall growing, declining, or consolidating.

##### 2. Country & Index Comparisons
* **Top Countries by Average Close (Clustered Column Chart):**
  * **Description:** Compares the average closing prices across different countries.
  * **Value:** Instantly identifies the leading global markets by closing price and simplifies international index comparison.

##### 3. Market Sentiment Distribution
* **Bullish vs. Bearish (Donut Chart):**
  * **Description:** Displays the percentage distribution of the market status (rising vs. falling).
  * **Value:** Provides a high-level snapshot of global market sentiment, showing the exact ratio of bullish versus bearish days.

##### 4. Geographic Analysis
* **Average Close by Country (Azure Map):**
  * **Description:** Plots countries on a global map, where bubble sizes correspond to their average closing price.
  * **Value:** Offers a geographical overview of market performances, visually emphasizing stronger economic zones.

##### 5. Liquidity & Trading Strength
* **Total Volume by Country (Treemap):**
  * **Description:** Represents the total trading volume for each country using sized tiles.
  * **Value:** Easily distinguishes which countries hold the largest shares of market liquidity and trading activity.

##### 6. Return Evaluation
* **Average Daily Return (%) by Country (Clustered Column Chart):**
  * **Description:** Compares the average daily return percentages across countries.
  * **Value:** Rates the performance of each country based on returns, highlighting the most profitable and the weakest markets.

##### 7. Granular Data Reference
* **Performance Summary (Table):**
  * **Description:** Displays a comprehensive tabular view of each country alongside its key metrics: *Total Volume*, *Average Return*, *Average Close*, and *Average Volatility*.
  * **Value:** Serves as a reference table that supports visual insights with precise, numeric details.

---

### Power BI Dashboard Showcase:
<p align="center">
  <img width="1198" height="670" alt="1000202908" src="https://github.com/user-attachments/assets/a10419ea-d291-41e2-84de-9b3a7d4a407d" />
  <img width="1151" height="656" alt="1000202907" src="https://github.com/user-attachments/assets/59cb84f7-07b5-4146-b0a3-71d544a32596" />
<img width="1147" height="671" alt="1000202906" src="https://github.com/user-attachments/assets/9b44f478-05ea-4fe4-92cc-d2bb9317a4e9" />


</p>

---

## Phase 2: Excel

<p align="center">
 <img width="863" height="472" alt="1000202909" src="https://github.com/user-attachments/assets/2ea128ee-4d98-4998-9492-ac3b60257ead" />


This project features an interactive, dynamic Excel Dashboard designed to analyze global stock market trends, financial performance, and volatility. The dashboard is built on a dynamic architecture where all visualizations update instantly based on user interaction.

### Dashboard Overview

The dashboard serves as a unified interface that consolidates vital financial and market information into a single screen. It provides stakeholders with an interactive environment to explore data dynamically. 

By interacting with the dashboard, users can:
* Select and filter by a specific Country.
* Select and filter by a specific Stock Index.
* Select and filter by a specific Sector.
* Adjust and change the Timeframe.
* Observe all visual elements and charts updating instantly in real-time.

#### Key Performance Indicators (KPIs) and Visualizations

The dashboard is structured into specific dynamic sheets, each tracking critical performance metrics and financial indicators:

##### 1. Interactive Filters (Slicers)
These components allow the user to isolate and display specific subsets of data instead of viewing the entire dataset at once:
* **Country:** Filters the metrics to display data for a specific country (such as USA, UK, or Germany), enabling a direct performance comparison between countries.
* **Stock Index (Index Name):** Filters the metrics to display data for a specific index (such as NASDAQ, S&P 500, FTSE, or DAX), allowing focused tracking of a single index's performance.

##### 2. Market Performance Metrics

* **Close Price Over Time (Line Chart):**
  * **Horizontal Axis (X-Axis):** Date.
  * **Vertical Axis (Y-Axis):** Close Price.
  * **Purpose:** Identifies the overall trend of the market.
  * **Function:** Determines whether the stock index is in a rising (bullish), falling (bearish), or stable state.

* **Index Performance Ranking (Bar Chart):**
  * **Purpose:** Compares different indices (such as NASDAQ, S&P 500, or FTSE).
  * **Function:** Identifies which stock index achieved the highest value.

* **Volume Over Time (Area Chart):**
  * **Purpose:** Displays the trading volume over a period of time.
  * **Function:** It represents the performance trend similarly to a line chart, but with the area underneath the line shaded to visually emphasize the strength of growth or decline.

* **Countries by Trading Volume (Bar Chart):**
  * **Purpose:** Compares a specific value (such as Average Volume) for each stock index.
  * **Function:** Instantly highlights and identifies the best-performing index.

### 3. Financial Insights Metrics

<p align="center">
 <img width="758" height="452" alt="1000202910" src="https://github.com/user-attachments/assets/99f73c72-7f3e-48ed-b84f-dd808f5e1015" />


This section is dedicated entirely to evaluating the corporate and financial performance of indices and companies:

* **Revenue Comparison:**
  * **Purpose:** Compares total revenues generated among different companies.
  * **Function:** Pinpoints which company achieved the highest revenue.

* **Profit Comparison:**
  * **Purpose:** Displays and compares profitability metrics.
  * **Function:** Identifies the most profitable companies.

* **Index Performance Ranking (Financial Index Performance):**
  * **Purpose:** Sorts and ranks all available indices from the best-performing to the worst-performing.
  * **Function:** Helps to instantly identify the top-performing index.

* **Trend and Volatility Analysis (Max Close vs. Min Close / Average Volatility) (Line Chart):**
  * **Purpose:** Displays the historical change of specific financial metrics over time, such as Profit, Revenue, or Market Value.
  * **Function:** Analyzes financial trends and price fluctuations.

#### Technical Architecture

##### Pivot Tables
The dashboard relies entirely on Pivot Tables to process the backend data:
* **Function:** They summarize thousands of raw data rows into structured, simplified tables.
* **Metrics Aggregated:** Calculates Average, Sum, Count, Maximum (Max Value), and Minimum (Min Value).

##### Pivot Charts
* All visual charts on the dashboard are Pivot Charts directly linked to their respective Pivot Tables.
* Any change made to the filters (Slicers) or the underlying dataset automatically updates the Pivot Tables and refreshes all charts instantly.

</p>

---
## Phase 3: Tableau

### Dashboard 1: Global Market Overview
<p align="center">
 <img width="1361" height="846" alt="1000202903" src="https://github.com/user-attachments/assets/acff6945-240f-4caf-8f90-1be449c75387" />

### Tabs on this Dashboard

- Market Performance by Country
- Market Performance by Index
- Avg Daily Change
- Avg Daily Change%
- Markets Up
- Markets Down
- Total Volume

### Key Insights

#### Market Performance by Country

- Pakistan (KSE 100) has the strongest average daily performance overall.
- Japan (Nikkei 225) has the weakest overall (-0.21%).

#### Market Performance by Index

- Ranking from best to worst: NASDAQ (+0.34%), KSE 100 (+0.30%), S&P 500 (+0.17%), DAX (+0.15%), Hang Seng (+0.10%), SSE Composite (+0.08%), CAC 40 (+0.07%), Dow Jones (-0.02%), FTSE 100 (-0.07%), Nikkei 225 (-0.21%).
- The three US indices (NASDAQ, S&P 500, Dow Jones) land in very different places on the ranking, showing that indices from the same country can move very differently.

#### Avg Daily Change

- The monthly average moves up and down around the reference line without one clear long-term direction, consistent with data that behaves close to random day-to-day noise.

#### Avg Daily Change%

- Since most of the seven included indices posted a small positive average in this window, the overall card would read positive (green).

#### Markets Up

- Across the full dataset, up-days make up about 49% of all records.

#### Markets Down

- Down-days make up about 51% of all records across the full dataset.

#### Total Volume

- Total volume across all countries (full dataset) is roughly 266 billion units; the USA alone accounts for about 100 billion of that because it has three indices.

---

### Dashboard 2: Performance Analysis
<p align="center">
 <img width="1362" height="846" alt="1000202905" src="https://github.com/user-attachments/assets/844b8d90-d401-4526-842d-6d0e12aa0e43" />
 
**Purpose:** A deeper look at price movement (candlestick chart for the S&P 500), risk versus return across all indices, and the top/bottom performers, for the period 28 Apr 2020 – 8 Feb 2022.

### Tabs on this Dashboard

- CANDLESTICK
- RISKS vs RETURNS
- TOP GAINER KPI
- TOP LOSER KPI
- Highest Volatility

### Key Insights

#### CANDLESTICK

- The S&P 500's close price in this dataset ranges from about 866 to 40,323, which is far outside its real historical range — a sign the price data here is simulated rather than a real feed.
- The chart correctly demonstrates the candlestick technique (colour for direction, wick for daily range) regardless of the underlying data's realism.

#### RISKS vs RETURNS

- KSE 100 has the best combination in this window: the highest return (+0.22%) with comparatively low volatility (4.99).
- Dow Jones has the worst combination: the lowest return (-0.19%) even though its volatility is also the lowest (4.72).
- SSE Composite has the highest volatility of the group (5.74) with only a middling return.

#### TOP GAINER KPI

- KSE 100 is the Top Gainer in this window.

#### TOP LOSER KPI

- Nikkei 225 is the Top Loser in this window.

#### Highest Volatility

- The highest single volatility reading in this window is 94.46 — far above the typical 5.0–5.5 range seen in the index averages, showing a rare extreme spike exists somewhere in the data.

---

### Dashboard 3: Trading Activity & Risk
<p align="center">  
<img width="1367" height="847" alt="1000202904" src="https://github.com/user-attachments/assets/3c378503-5217-4791-a457-d6351401358b" />

**Purpose:** Focuses on trading volume — which country and index trade the most, how volume trends over time, and whether volume relates to performance. This dashboard only includes the months of May and October across all five years.

### Tabs on this Dashboard

- Volume by Country
- Volume Trend Over Time
- Avg Volume Per Index
- Most Active Country
- Most Active Index
- VOLUME vs DAILY CHANGE %

### Key Insights

#### Volume by Country

- USA has by far the largest bubble (16.5 billion) — but this is mostly because the USA has three indices, not one, summed together.
- Excluding that structural effect, the other seven countries are fairly close together, from about 5.1 to 5.8 billion.

#### Avg Volume Per Index

- Gives a fair per-index benchmark that isn't skewed by the USA having three indices, unlike the country-level total.

#### Most Active Country

- USA is the Most Active Country (16.5 billion) — again mainly because it has three indices combined into one total.

#### Most Active Index

- DAX is the Most Active single index (about 5.84 billion), narrowly ahead of Dow Jones (5.74 billion) and SSE Composite (5.64 billion) — a different answer than the country-level card because no single US index individually beats DAX.

#### VOLUME vs DAILY CHANGE %

- Higher trading volume does not necessarily correspond to better market performance.

---
##  Phase 4: Python 

In this phase, we leveraged Python to build an interactive, web-based dashboard to provide deep insights into global stock market trends, trading volumes, and volatility. The application was built to ensure high performance and an intuitive user experience using a custom dark theme.

###  Technologies & Libraries Used
*   **[Streamlit](https://streamlit.io/):** Used to build the interactive web application interface and manage dynamic user filters.
*   **[Pandas](https://pandas.pydata.org/):** Utilized for loading the dataset, performing aggregations, and manipulating time-series data efficiently.
*   **[Plotly](https://plotly.com/python/):** Powered the dynamic and interactive visualizations (Choropleth Maps, Treemaps, Candlestick charts, and Bubble charts).

###  Dashboard Features & Architecture
<p align="center">
<img width="1600" height="818" alt="1" src="https://github.com/user-attachments/assets/14e1641e-c316-4503-8051-ad69ea6f165b" />
<img width="1600" height="602" alt="2" src="https://github.com/user-attachments/assets/8884f8a6-38a3-4468-bee1-14b4d5d4bb45" />
<img width="1600" height="669" alt="3" src="https://github.com/user-attachments/assets/3e87a6cd-5a57-4d2a-8541-4c34760ebbc8" />
<img width="1600" height="474" alt="4" src="https://github.com/user-attachments/assets/9b8a7b5c-aac1-4208-b4a1-c55be26bca15" />


The Streamlit application is designed with sidebar filters (Country and Year) and is divided into three main analytical tabs:

1.  **Overview Tab:**
    *   **KPI Metrics:** Highlights Total Volume, Avg Daily Change, and identifies the Top Gainer and Top Loser indices.
    *   **Global Map (Choropleth):** Visualizes the average market close prices globally.
    *   **Volume Trend:** An Area Chart tracking overall trading volume trends over time.

2.  **Performance Tab:**
    *   **Volume Treemap:** Showcases the hierarchical distribution of trading volumes by country and index.
    *   **OHLC Candlestick Chart:** Provides detailed price movements (Open, High, Low, Close) for any selected index.
    *   **Return Comparison:** A Bar Chart comparing average daily returns across different nations.

3.  **Risk & Volume Tab:**
    *   **Risk vs. Return:** A Bubble Scatter Plot analyzing market volatility against daily returns, with bubble sizes reflecting trading volume.
    *   **Volume vs. Performance:** A Scatter Plot examining how total trading volume correlates with overall market performance.

###  How to Run the App Locally
To run the Streamlit dashboard on your local machine, follow these steps:

1. Navigate to the Python project directory:
   ```bash
   cd path/to/python_dashboard_folder



---
## Key Insights & Performance Summary

### Best and Worst Performers

- Across the full 5-year dataset, KSE 100 (+0.13%/day) and Hang Seng (+0.08%/day) are the strongest average performers; Nikkei 225 (-0.21%/day) and Dow Jones (-0.16%/day) are the weakest.
- In the shorter Performance Analysis window (Apr 2020–Feb 2022), KSE 100 is again the Top Gainer and Nikkei 225 is the Top Loser.

### Volume and Country Comparisons

- The USA appears as the top country by volume, but only because three US indices (Dow Jones, NASDAQ, S&P 500) are summed together.
- DAX (Germany) is the single most active individual index by volume in the May/October sample, ahead of Dow Jones and SSE Composite.
- Trading volume does not appear to predict performance; some high-volume indices underperformed while some lower-volume indices, like the S&P 500, outperformed.

### Risk vs Return

- KSE 100 offers the best combination of high return and comparatively low risk in the Performance Analysis window.
- Dow Jones has the lowest volatility but also the lowest return, making it the weakest risk-adjusted performer in that window.
- The highest single total volatility spike recorded anywhere in the dataset is 94.46 — much higher than the typical 5.0–5.5 average, showing rare extreme-risk days do occur even though average risk looks similar across indices.
- The Risk vs. Return analysis demonstrates that higher volatility does not always produce greater returns.
</p>

