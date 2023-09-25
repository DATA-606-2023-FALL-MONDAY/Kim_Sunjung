## 1. Title and Author: 

- Project Title: **Popular Baby Name in United States**
-	Prepared for UMBC Data Science Master Degree Capstone by Dr **Chaojie (Jay) Wang**
-	Author Name: **Sunjung Kim**
-	Link to the author's GitHub profile: **https://github.com/DATA-606-2023-FALL-MONDAY/Kim_Sunjung/edit/main/docs/Proposal.md**
-	Link to the author's LinkedIn progile: **N/A**
-	Link to your PowerPoint presentation file: **N/A**
- Link to your YouTube video: **N/A**
  
## 2. Background

-	**What is it about?**
  - In 1998, the Social Security Administration released Actuarial Note #139, authored by actuary Michael W. Shackleford, providing an analysis of the distribution of given names among Social Security number holders. The Actuarial Note #139 has become a valuable resource for studying name distribution within the United States. All data utilized by the Social Security website is sourced from a 100% sample of records pertaining to SSN applications.
 	
- **Why does it matter?**
  - The chosen topic of this report revolves around the popularity of baby names in the United States, as indicated by data obtained from the Social Security Office. This topic delves into the trends and patterns in baby naming practices within the United States.  
  - Becoming a parent is very exciting. However, naming a newborn baby could be somewhat difficult, and this is significant for several reasons: 
    - Societal Understanding: Researching name distribution trends offers insights into     cultural and societal changes over time, reflecting cultural and generational shifts. 
    - Demographic Research: The name data is valuable for demographic research, aiding policymakers in tracking population dynamics and migration patterns. 
    -  Public Policy: Government and local organizations can utilize this name data to inform policies related to social services, education, and marketing strategies based on the demographics associated with names.

-	**What are your research questions?**
  -	What are the most popular baby names in the United States over the past decade, and how have these names evolved?
  -	What are the least popular baby names in the United States over the past decade, and how have these names evolved?
  -	How do cultural and celebrity influences impact baby naming trends?
  - What are the top 5 popular baby names in the past five years? (For boy/girl)
  - What were the trendiest boy and girl names in 2022? (For the most updated information)

## 3. Data

- **Data sources:**
  - Social Security Administration https://www.ssa.gov/oact/babynames/limits.html
- **Data size:**
  - National data: (7Mb)
  - State-Specific Data: (22Mb)
  -	Territory-specific data: (280kb)
-	**Data shape (# of rows and # columns)**
  -	National data: 6255047 rows and 3 columns
  -	State-Specific Data: 12815981 rows and 5 columns
  -	Territory-specific data: 53765 rows and 5 columns
-	**Time period:**
  -	 Year Range: 1998 to 2022
- **What does each row represent?** 
  - Each row represents baby names.
  
- **Data dictionary**:
  - **National Data:**
    - name (object): This column represents the names of babies.
    - gender (object): This column represents the gender of the baby (male or female).
    - count (int64): This column represents the count of babies with a particular name and gender combination.

  -	**State-Specific Data:**
    -	state (object): This column represents the state in the United States where the data is specific to.
    -	gender (object): This column represents the gender of the baby (male or female).
    -	year (int64): This column represents the year of the data.
    -	name (object): This column represents the names of babies.
    -	count (int64): This column represents the count of babies with a particular name, gender, state, and year combination.

  - **Territory-Specific Data:**
    - pr_status (object): This column represents the territorial status (e.g., "PR" for Puerto Rico).
    -	gender (object): This column represents the gender of the baby (male or female).
    -	year (int64): This column represents the year of the data.
    -	name (object): This column represents the names of babies.
    -	count (int64): This column represents the count of babies with a particular name, gender, territorial status, and year combination.

- **Which variable/column will be your target/label in your ML model?**
  - The target variable for predicting baby names is `Count` colum.

- **Which variables/columns may be selected as features/predictors for your ML models?**
  -	`name`: using name column for popularity or characteristics.
  -	`gender`: Using gender column to find out naming trends by gender.
  -	`state` (in state-specific data): analyzing naming trends by state.
  -	`year`: Analyzing trends over time.
  -	`pr_status` (in territory-specific data): Using pr_status to analyze naming trends in different territories.

