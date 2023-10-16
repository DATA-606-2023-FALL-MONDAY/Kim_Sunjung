## 1. Title and Author: 

- Project Title: **Maryland Residential Housing: Prices, Trends, and Forecast.**
-	Prepared for UMBC Data Science Master Degree Capstone by Dr **Chaojie (Jay) Wang**
-	Author Name: **Sunjung Kim**
-	Link to the author's GitHub profile: **https://github.com/DATA-606-2023-FALL-MONDAY/Kim_Sunjung/edit/main/docs/Proposal.md**
-	Link to the author's LinkedIn progile: **N/A**
-	Link to your PowerPoint presentation file: **N/A**
- Link to your YouTube video: **N/A**
  
## 2. Background

-	**What is it about?**
  - The topic is about the housing market in Maryland, a state in the United States. It involves collecting, analyzing, and interpreting data related to housing prices, trends, and forecasts. This analysis aims to provide insights into the real estate market in Maryland.
 	
- **Why does it matter?**
  - The housing market is a critical component of the economy, and it plays a significant role in the financial well-being of individuals and the state as a whole. Understanding the housing market in Maryland is essential for various reasons:
  - Economic Impact: The housing market has a substantial economic impact, affecting industries such as construction, finance, and real estate. It also influences property taxes and revenue for the state.
  - Quality of Life: Housing affordability and quality impact the residents' quality of life. Access to suitable housing affects educational opportunities, access to jobs, and overall well-being.
  - Investment Opportunities: For investors and homeowners, the housing market presents opportunities for wealth accumulation and financial security.
    
-	**What are your research questions?**
  - To explore the Maryland housing market comprehensively, we can frame various research questions:

    - Price Trends: What are the historical trends in housing prices in Maryland? Are prices increasing, decreasing, or stabilizing over time?
    - Geographic Variations: How do housing prices vary by location within Maryland? Are there specific areas where prices are consistently high or low?
    - Forecasting: Can we use historical data to predict future housing market trends in Maryland? What methods and models are most accurate for forecasting?
## 3. Data

- **Data sources:**
  - Multiple MLS 
- **Data size:**
  - 3.46MB
-	**Data shape (# of rows and # columns)**
  - 21597, 21

-	**Time period:**
  -	 Year Range: 2014-2015 using historial data to predict future housing price. 
- **What does each row represent?** 
  - id', 'date', 'price', 'bedrooms', 'bathrooms', 'sqft_living',
       'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade',
       'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode',
       'lat', 'long', 'sqft_living15', 'sqft_lot15'],
      dtype='object
  
- **Data dictionary**:
     - Column Name       Data Type                          Definition
   - 0              id           int64                   Unique identifier
   - 1            date  datetime64[ns]                        Date of sale
   - 2           price           int64                  Price of the house
   - 3        bedrooms           int64                  Number of bedrooms
   - 4    bathrooms         float64                 Number of bathrooms
   - 5     sqft_living           int64          Living area square footage
   - 6        sqft_lot           int64                  Lot square footage
   - 7          floors         float64                    Number of floors
   - 8      waterfront         float64                   Waterfront status
   - 9            view         float64                         View rating
   - 10      condition           int64                    Condition rating
   - 11          grade           int64                        Grade rating
   - 12     sqft_above           int64         Square footage above ground
   - 13  sqft_basement           int64      Square footage of the basement
   - 14       yr_built           int64                          Year built
   - 15   yr_renovated         float64                      Year renovated
   - 16        zipcode           int64                             Zipcode
   - 17            lat         float64                            Latitude
   - 18           long         float64                           Longitude
   - 19  sqft_living15           int64  Living area square footage in 2015
   - 20     sqft_lot15           int64          Lot square footage in 2015
- **Which variable/column will be your target/label in your ML model?**
  -Tartget Column = Price

- **Which variables/columns may be selected as features/predictors for your ML models?**
  - Feature Columns= bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors', 'waterfront','view','condition', 'grade', 'sqft_above', 'sqft_basement', 'yr_built', 'yr_renovated','zipcode', 'lat', 'long', 'sqft_living15', 'sqft_lot15'
