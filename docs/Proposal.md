## 1. Title and Author: 

- Project Title: **Korean Drama Recommendation System**
-	Prepared for UMBC Data Science Master Degree Capstone by Dr **Chaojie (Jay) Wang**
-	Author Name: **Sunjung Kim**
-	Link to the author's GitHub profile: **https://github.com/DATA-606-2023-FALL-MONDAY/Kim_Sunjung/edit/main/docs/Proposal.md**
-	Link to the author's LinkedIn progile: **N/A**
-	Link to your PowerPoint presentation file: **N/A**
- Link to your YouTube video: **N/A**
  
## 2. Background

-	**What is it about?**
  - My Capstone is about Korean Drama recomendation System. Korean dramas have gaied immense popularity over a few decades. Whicha vast libary korean dramars available, viewers can find some challenge to select the best Korean dramas. This recomendation system can alleviate this issue by providing content based suggestions to invidual user. 
- **Why does it matter?**
  - User Satisfaction: this recomendation system can offer users to discover Korean Dramas that resonate with their interest, leading to higher satisfaction.
  - Content Discover: Most of foreginers are having hard time to discover Korean Dramas content lists. This recomendation can helps users navigate through the overwhleming amount of content.
  - Marketing and Revenue: For streaming platforms, en effective recomendatin system can increases revenue.
    
-	**What are your research questions?**
  - You can explore several research questions, such as:

  * What are the most popular genres in South Korean dramas, and how have they evolved over time?

  *Is there a correlation between the average rating and the number of ratings received for a series?

  *Are there certain directors or production companies associated with higher-rated dramas?

  *How has the popularity of South Korean dramas changed over the years?

  *What are the most common keywords associated with successful K-dramas?

  *How do viewership trends differ between domestic and international audiences?

These research questions can serve as a starting point for analyzing the Korean Drama Dataset, but there are many more possibilities depending on your specific research goals and interests. The dataset provides a rich source of information for exploring various aspects of the South Korean TV drama industry and its impact both locally and globally
## 3. Data

- **Data sources:**
  - TMDB website
- **Data size:**
  - 0.25MB
-	**Data shape (# of rows and # columns)**
  - 1920,22

-	**Time period:**
  -	 Year Range: 1983-2022
- **What does each row represent?** 
  - tmdb_id, name, original_name, airing_date, cast_ids, genres_ids, number_of_seasons, number_of_episodes, episode_run_time, synopsis, popularity        
    ,average_rating,networks_ids           
  
- **Data dictionary**:
| Column Name | Data Type | 
| series_id_id   | int64 |
| original_name   | object   | 
| keywords  | int64 | 
| director_ids | object|
| cast_id  | int64 | |
| genres_ids | object| 
|synopsis | object|
| Popularity| int64|
|Aver_rating | int64|
|Networks_ids | int64|
|episode_run_time | int64|

- **Which variable/column will be your target/label in your ML model?**
  -Tartget Column = popularity

- **Which variables/columns may be selected as features/predictors for your ML models?**
  - Feature_columns = 'epdisode_run_time, 'average_rating', and 'original_name'
    
## 4.Exploratory Data Analysis (EDA)

