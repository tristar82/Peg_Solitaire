<img src="https://cdn.freelogovectors.net/wp-content/uploads/2020/01/university-of-exeter-logo.png" alt="Univeristy of Exeter Logo" width="100"/>

# HPDM139 Assignment 1 - Peg Solitaire
*Elliott Coyne*

*MSc Health Data Science 2021/2 Cohort*

## Content
- [Project Description](#project-description)
- [Hypotheses / Questions](#hypotheses-questions)
- [Dataset](#dataset)
- [Cleaning](#cleaning)
- [Analysis](#analysis)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [Conclusion](#conclusion)
- [Future Work](#future-work)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

## Assignment Description
The purpose of this task is to emulate the work of a business consultant who has been engaged by a venture capital group who are considering whether or not to purcahse the UK based online retailer 'Alpine Online'. Part of this due dilligence exercise is to identify opportunities for improvement within the business. Strategies to be explored include the implementation of a recommender system to increase sales for both regular and business customers (based on their purchasing habits), clustering/ categorizing of customers to increase personalisation of communications with them, as well as an analysis of customer returns and the potential impact on cash flow and employee workload.

## Questions
Given the retailer is only able to provide transactional data (and not details of all customers or a current inventory master file), much time will be taken to analyse and clean the data in order to derive meaningful insights. Once the data is cleaned and the necessary assumptions made, the following questions will need to answered:
* How much can be learned about a business simply by analysing it's transaction data?
* What is the potentail increase in revenue that could be enjoyed if a recommender system were to be implemented?
* What is the rate of returned products? Does this identify stock that should be discontinued? What are the possible implications for employee workflow, when considering the processing of returned items.
* What features should be considered when clustering customers.

## Dataset
* This project is a simulation of a Business Analysis Consultation for a ficticious online retailer. The raw dataset used was sourced from UCI Machine Learning Repository. The link to the raw dataset can be found in the links sections below. The data was provided in an Excel (XLSX) file, with 11 monhts of transactional data within a 22.6mb file (size).
* From the raw dataset, it was necessary to reverse engineer an inventory master file (based on listed transactions) to provide an Average Weighted Price (AWP) and average purchase quantity. Each of these metrics were calculated each for business (B2B) and retail (B2C) customers.
* In order to add a continuous numerical value related to each customers' location the GeoPy library was installed. The numerical value derived was the distance from the centre of the customers country to the UK. Therefore customers found in the UK would return a value of 0.

## Cleaning
Siginificant time and effort when into cleaning the dataset, as it became apparent there were a number of issues captured within the raw file. There were many issues - such as same day returns (which are assumed to be processing errors by administration staff). The transaction log also contain stock write offs (negative quantity with no CustomerID associated). These need to be exluded as they are not relevant to this investigation.

## Analysis
* The analysis phase of this project looked at many factors including but not limited to: 1. Annual Revenue 2. Number of Customers by Country 3. Number of erroneous transactions (same day returns) 4. Suitable Number of Customer Clusters.
* Issues with the data included different prices charged, customers with multiple countries assigned to them (which is problematic for clustering), customers with a net negative quantity of items purchased over time period investigated.
* The the clustering exercise it was necessary to derive the following features for each customer: 1. Total Revenye 2. Average Transaction Value 3. Minimum Transaction Value, 4. Maximum Transaction, 5. Number of Transactions 6. Total number of items purchased and 7. Distance of customer from UK.

## Model Training and Evaluation
* Recommender Systems are on the use of customer clustering and the investigation of distances between customers. There are multiple metrics that can be used to calculate the aforementioned distances (i.e. 'cityblock', 'correlation', 'cosine', 'dice', 'euclidean', 'hamming' and 'jaccard'). During the build of the recommender system different metrics will be used and their output assessed to determine which would be the most suitable to implement. The range in revenue uplift values (per metric type) ranged from 365,870 to 488,219

## Conclusion
* Working with transactional data alone proved to be a challenge, however the additional cleaning and exploratory data analysis resulted in a more intiment knowledge of the retailer.
* In order to assess the strength/ validity of the recommendations, a furtheer analysis will need to be carried out following their implemention.

## Future Work
The assumption would be that the retailer would adopt the recommendations made within this project. Therefore it would be prudent to collect further transaction data in order to assess the success or failure of the recommentations. In addition to the quantitative data collected from transaction lots, it would also be useful to collect qualitative data from employess both pre and post implementation of the recommendations. Additionally, further work can be done to investigate the effectiveness of the clustering and possibly apply AWP and average purchase quantity per cluster type to the prediction of revenue.

## Workflow
* Following the selection of the topic probelm and questions, suitable data was sourced. This data was then downloaded and loaded into dataframes, cleaned and analysed. The cleaning process was carried out simultaneously to Exploratory Data Analysis (EDA); cleaning and removing outliers whilst reviewing the data appeared to be the most efficient use of time.
* Once the data was cleaned then an inventory pricing file was created retrospectively (assigning a respective average price and quantity purcahsed by customer type - B2B or B2C)
* The cleaned trasnaction file was then used to create a recommender system that used the above file to estiamte the revenue improvement.
* Clustering was undertaken (K-means and PCA) using the metrics described above (Which were normalised).

## Organization
In order to organise the project, a kanban board from Trello was used. The link to the Trello board can be found below.

The respository root folder has one main working directory, 'your-project' which is divded into three sub-folders. This Readme file resides in the root directory. Below is an explanation of each sub folder and their respective contents:
* Charts(Tableau) - The downloaded Tableau Public files are stored locally for review and comment.
* Code - The Jupyter Notebook files used to obtain, clean and analyse the data.
* Data - Both the raw XLSX file (downloaded) and CSV files (generated during investigation) used for this project.
* Images - Images downloaded and used for presentation.

## Links
Please find all relevant links for this project below:
*[Repository](https://github.com/tristar82/Project-Week-8-Final-Project)
*[Slides](https://docs.google.com/presentation/d/1GSYmX9WHKzriCXHyuFMpeT_GYxb0U7cIRgJcrQmdu30/edit?usp=sharing)
*[Trello](https://trello.com/b/3icjIHgb/final-project-ironhack-bcn)
**Data Source**
*[UCI****] Dataset downloaded from (https://archive.ics.uci.edu/ml/datasets/Online+Retail+II)
**Libraries Required to Run Code**
*[Plotly](https://plot.ly/python/v3/ipython-notebooks/cufflinks/)
*[GeoPy](https://geopy.readthedocs.io/en/stable/)

