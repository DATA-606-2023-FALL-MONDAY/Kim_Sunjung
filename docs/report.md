## 1. Title and Author: 

- Project Title: **Korean Drama Recommendation System**
-	Prepared for UMBC Data Science Master Degree Capstone by Dr **Chaojie (Jay) Wang**
-	Author Name: **Sunjung Kim**
-	Link to the author's GitHub profile: **https://github.com/DATA-606-2023-FALL-MONDAY/Kim_Sunjung/edit/main/docs/Proposal.md**
-	Link to the author's LinkedIn profile: **N/A**
-	Link to your PowerPoint presentation file: **https://github.com/DATA-606-2023-FALL-MONDAY/Kim_Sunjung/blob/main/docs/Final%20.pptx**
- Link to your YouTube video: **N/A**
  
## 2. Background

-	**What is it about?**
  - Korean TV dramas, or K-dramas, have gained popularity in Asia since the 1990s and, over the past decade, have made significant inroads into European and American entertainment markets, attracting a substantial Western audience.
  - Recommender systems are widely used in online streaming and shopping, helping predict consumer preferences for products, movies, or shows. Companies like Netflix and Amazon use these systems to direct users to content that matches their interests.
  - To cater to the increasing global interest in K-dramas, this recommender system specifically suggests Korean dramas, based on users' previous viewing habits and drama synopses, ensuring personalized and relevant K-drama recommendations.

- **Why does it matter?**
  - User Satisfaction: this recomendation system can offer users to discover Korean Dramas that resonate with their interest, leading to higher satisfaction.
  - Content Discovery: The system aids international viewers in navigating the extensive K-drama library, overcoming language and familiarity barriers. It simplifies finding appealing content, enhancing the viewing experience by exposing users to K-dramas tailored to their tastes.
  - Marketing and Revenue: For streaming platforms it increases viewer engagement and leads to longer viewing sessions and potentially higher advertising or subscription revenue. Additionally, it informs marketing strategies and content decisions, contributing to customer acquisition and retention.
    
-	**What are your research questions?**
  - You can explore several research questions, such as:

  *What are the most popular genres in South Korean dramas, and how have they evolved over time?

  *What are the most well-known Network compnay in South Korea?

  *Can I get a recommendation list base on the content?

  *What are the most common keywords associated with successful K-dramas?
  
## 3. Data

- **Data sources:**
  - Kaggle
- **Data size:**
  94.8 KB
-	**Data shape (# of rows and # columns)**
  - 1515,8

-	**Time period:**
  -	 Year Range: 1983-2023
- **What does each row represent?** 
  - tmdb_id, name, original_name, airing_date, cast_ids, genres_ids, number_of_seasons, number_of_episodes, episode_run_time, synopsis, popularity        
    ,average_rating,networks_ids           
  
- **Data dictionary**:
<p align="center">
  <img src="https://github.com/DATA-606-2023-FALL-MONDAY/Kim_Sunjung/blob/main/data/Data.png">
</p>

- **Which variable/column will be your target/label in your ML model?**
  -Target Column = tmbd_id

- **Which variables/columns may be selected as features/predictors for your ML models?**
  - Feature_columns = 'name', 'cast', 'genres', 'synopsis'
    
## 4.Exploratory Data Analysis (EDA)

<p align="center">
  <img src="https://github.com/DATA-606-2023-FALL-MONDAY/Kim_Sunjung/blob/main/data/genre.png">
</p>
This is a distribution of K-drama genres.

<p align="center">
  <img src="https://github.com/DATA-606-2023-FALL-MONDAY/Kim_Sunjung/blob/main/data/network%20.png">
</p>
This displaying top 15 K-drama networks.

<p align="center">
  <img src="https://github.com/DATA-606-2023-FALL-MONDAY/Kim_Sunjung/blob/main/data/Year.png">
</p>
This displaying total number of K-dramas released per year. 

<p align="center">
  <img src="https://github.com/DATA-606-2023-FALL-MONDAY/Kim_Sunjung/blob/main/data/Top50%20words.png">
</p>
This displaying top 50 most common words in the synopsis. 

## 5. Model and Development

- Content-Based Recommendation System: 
  - Data Collection: Gather data on K-dramas, including genres, user ratings, and synopses.
  Feature Extraction: Transform this data into numerical vectors. For example, text data from synopses can be converted using TF-IDF (Term Frequency-Inverse Document Frequency).
  - Similarity Calculation: Compute the cosine similarity between the feature vectors of different K-dramas. This metric quantifies how similar they are based on user preferences and content features.
  - Implementation: Receiving user input, such as preferred dramas or genres, the system generates a feature vector for these preferences. It then calculates the cosine similarity with the vectors of available K-dramas in the database. Dramas with the highest similarity scores are recommended to the user.
- Attributes Recommendation System:
  - Top Actors: Featuring the prominent actors in K-dramas.
  - Synopsis: Providing a brief overview of the K-drama plot.
  - Genres: Identifying the genres associated with each K-drama.
 
  - Data Transformation: The concatenated column attribute_based containing these metadata elements in text form will be converted into numerical vectors using CountVectorizer.
  - Count Matrix: The transformation results in a count_matrix_attribute which is a numerical representation of the metadata.
  - Cosine Similarity Calculation:The system will calculate the Cosine Similarity of the count_matrix_attribute. This metric will determine the similarity between K-dramas based on the key metadata elements, allowing for more targeted recommendations.
  - Implementation: the system utilizes the user's preferences to find K-dramas with similar metadata profiles in the count_matrix_attribute. The system then recommends K-dramas with the highest Cosine Similarity scores.

- Web Application using Streamlit:
<p align="center">
  <img src="https://github.com/DATA-606-2023-FALL-MONDAY/Kim_Sunjung/blob/main/data/Image%20for%20Web%20Application.png">
</p>
Showing K-drama recommendations based on the two systems.

- **Chellanges**
  - Data Quality and Availability: Address challenges related to sourcing and maintaining a high-quality, diverse dataset of Korean dramas, including issues with incomplete or biased data.
  -  Algorithm Complexity: Discuss the complexities in developing and tuning recommendation algorithms, especially in catering to diverse user preferences.

- **Conclusion:**
  - Implementing Cosine Similarity in a K-drama recommendation system can significantly enhance user satisfaction by providing personalized and relevant content suggestions. This approach is not only efficient in handling diverse data but also scales well with expanding K-drama libraries, making it an ideal choice for streaming platforms looking to improve their recommendation algorithms.
