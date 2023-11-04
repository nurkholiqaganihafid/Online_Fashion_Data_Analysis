<div id="top"></div>

# 📌Online_Fashion_Data_Analysis
- __*Online Fashion Analysis*__ is a data analysis project that uses sales data from a fashion company called Dicoding Collection (DiCo). DiCo is an online company that produces and sells various fashion items. DiCo realizes the importance of data in developing a business, so they store all sales history, product information, and customer data in a database.
- The goal of this project was to evaluate the company's sales performance, understand the most and least sold fashion products, and gain a deeper understanding of customer demographics. By understanding customers better, DiCo can create more efficient campaign strategies.
- This database consists of four tables, including **customers**, **orders**, **products**, and **sales**. [Legend](https://github.com/nurkholiqaganihafid/Online_Fashion_Data_Analysis/blob/main/dataset/Legend.txt)
- This project uses a data analysis cycle, namely:
  - Question (Business Questions)
  - Data Wrangling
  - Exploratory Data Analysis (EDA)
  - Data Visualization
  - Draw Conclusion
  - Project Result Link: [Click here](https://github.com/nurkholiqaganihafid/Online_Fashion_Data_Analysis/blob/main/Online_Fashion_Data_Analysis.ipynb)

# 📌Outline
- [Business Questions](#business-questions) 
- [Results](#dartresults)
  - [Streamlit Dashboard](#streamlit-dashboard)
  - [My Analysis Results](#my-analysis-results)
    - [Merging all Data](#merging-all-data)
    - [Data Visualization](#data-visualization)
      - [1st Question](#1st-question)
      - [2nd Question](#2nd-question)
      - [3rd Question](#3rd-question)
      - [RFM Analysis (4th - 6th Questions)](#rfm-analysis)
- [Conclusions and Recommendations](#conclusions-and-recommendations)

# 🎯Business Questions
[👆](#outline)
Business questions that will be answered through this data analysis include:
1. How has the company's sales and revenue performance been in the last few months?
2. What products sell the most and least?
3. What are the customer demographics of the company?
4. When was the last time a customer made a transaction?
5. How often has a customer made purchases in the last few months?
6. How much money did customers spend in the last few months?

# :dart:Results
## 📊Streamlit Dashboard
[👆](#outline)
Link Streamlit Dashboard: [Dicoding Collection Dashboard](https://nurkholiq-online-fashion-data-analysis.streamlit.app/)

<p align="center">
  <img alt="Dicoding Collection Dashboard" title="Dicoding Collection Dashboard" src="https://github.com/nurkholiqaganihafid/Online_Fashion_Data_Analysis/assets/89395541/b2953718-3ac9-4f39-af8b-63f2df9ee8e4" width="750">
</p>

## 📈My Analysis Results
### Merging all Data
[👆](#outline) Total Data from the Merge Results
<p align="center">
  <img alt="Data Frame" title="Data Frame" src="https://github.com/nurkholiqaganihafid/Online_Fashion_Data_Analysis/assets/89395541/391487aa-1cc9-4fea-b621-cd3170f920c1" width="400">
</p>

### Data Visualization
#### 1st Question
[👆](#outline)
How has the company's sales and revenue performance been in the last few months?

- Sales Performance in Recent Months
<p align="center">
  <img alt="Number of Orders per Month (2021)" title="Number of Orders per Month (2021)" src="https://github.com/nurkholiqaganihafid/Online_Fashion_Data_Analysis/assets/89395541/d00a4f03-93e5-4960-9ab4-c6f8b9a61dd4" width="750">
</p>

- Company Revenue in Recent Months
<p align="center">
  <img alt="Total Revenue per Month (2021)" title="Total Revenue per Month (2021)" src="https://github.com/nurkholiqaganihafid/Online_Fashion_Data_Analysis/assets/89395541/4942e487-4fd4-4ab7-b0da-1333a2691fe2" width="750">
</p>

#### 2nd Question
[👆](#outline)
What products sell the most and least?
- Best and Worst Performing Product by Number of Sales
<p align="center">
  <img alt="Best and Worst Performing Product by Number of Sales" title="Best and Worst Performing Product by Number of Sales" src="https://github.com/nurkholiqaganihafid/Online_Fashion_Data_Analysis/assets/89395541/29d85840-d9cb-4995-a212-c33a2798782c" width="750">
</p>

#### 3rd Question
[👆](#outline)
What are the customer demographics of the company?

- By gender
<p align="center">
  <img alt="Number of Customer by Gender" title="Number of Customer by Gender" src="https://github.com/nurkholiqaganihafid/Online_Fashion_Data_Analysis/assets/89395541/0f6fc017-b540-4d27-800a-4412881a460a" width="750">
</p>

- By age
<p align="center">
  <img alt="Number of Customer by Age" title="Number of Customer by Age" src="https://github.com/nurkholiqaganihafid/Online_Fashion_Data_Analysis/assets/89395541/1c40164a-bd85-4959-b57a-7aaedd82c0d8" width="750">
</p>

- By state
<p align="center">
  <img alt="Number of Customer by States" title="Number of Customer by States" src="https://github.com/nurkholiqaganihafid/Online_Fashion_Data_Analysis/assets/89395541/80a3ead7-8f25-4fbe-8b75-5e10cf3f21fc" width="750">
</p>

#### RFM Analysis
[👆](#outline)
To answer the last three analysis questions, an analysis technique, namely RFM analysis, can be used.
- Recency: a parameter used to see the last time a customer made a transaction.
- Frequency: This parameter is used to identify how often a customer makes transactions.
- Monetary: This last parameter is used to identify how much revenue comes from that customer.

<p align="center">
  <img alt="Best Customer Based on RFM Parameters (customer_id)" title="Best Customer Based on RFM Parameters (customer_id)" src="https://github.com/nurkholiqaganihafid/Online_Fashion_Data_Analysis/assets/89395541/48617f92-7044-4eeb-9586-a27c86deb55b" width="750">
</p>

# 📚Conclusions and Recommendations
- Conclusions
  - Based on the company's sales and revenue results in the last few months, it can be seen that March had the highest number of orders, with 117 orders. However, there was a significant decrease in the number of orders in February, April, May and October. This also has an impact on company revenue. To overcome this decline, further analysis needs to be carried out regarding factors such as the existence of competitors and marketing campaigns.

  - In terms of product sales, Denim products were the most sold with 527 units, while Mandarin Collar products were the least sold with 236 units.

  - Customer demographics show that most customers do not disclose information about their gender. However, the majority of customers are in the adult age group, with 416 customers. Most customers come from the state of South Australia.

  - Lastly, customers made transactions at least a day ago, some even made transactions on the same day. A customer usually makes five or six purchases in the last few months. The customer who spent the most money was AUD 7632.

- Recommendations
  - Based on these results, companies can focus more on increasing sales in months with decreasing orders. Apart from that, companies can also expand their marketing strategies and identify new opportunities to attract more customers. It is also important to maintain and increase existing customer satisfaction by providing good service and quality products.

<p align="right"><a href="#top">Back to top</a></p>
