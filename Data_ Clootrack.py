#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


df = pd.read_csv('test_data.csv')


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


df.isnull().sum()


# In[6]:


df['Location'].value_counts()


# In[7]:


df_cleaned = df.dropna(subset=['Location'])


# In[8]:


df_cleaned.isnull().sum()


# In[9]:


df2 = df_cleaned.dropna(subset=['Review'])


# In[10]:


df2.isnull().sum()


# In[12]:


# Filter rows containing positive feedback (you can customize the keywords)
positive_keywords = ["impressed", "great", "excellent", "friendly", "good"]
positive_reviews = df2[df2['Review'].str.contains('|'.join(positive_keywords), case=False, na=False)]

# Count the frequency of each positive keyword
keyword_counts = {}
for keyword in positive_keywords:
    keyword_counts[keyword] = positive_reviews['Review'].str.count(keyword).sum()

# Find the most common positive feedback keyword
most_common_positive_feedback = max(keyword_counts, key=keyword_counts.get)

print(f"The most common positive feedback keyword is: {most_common_positive_feedback}")


# In[13]:


# Filter rows containing negative feedback (customize the keywords)
negative_keywords = ["old", "small rooms", "poor service", "dirty", "unresponsive"]
negative_reviews = df2[df2['Review'].str.contains('|'.join(negative_keywords), case=False, na=False)]

# Count the frequency of each negative keyword
keyword_counts = {}
for keyword in negative_keywords:
    keyword_counts[keyword] = negative_reviews['Review'].str.count(keyword).sum()

# Find the most common negative feedback keyword
most_common_negative_feedback = max(keyword_counts, key=keyword_counts.get)

print(f"The most common negative feedback keyword is: {most_common_negative_feedback}")


# In[14]:


df2['date'] = pd.to_datetime(df2['date'])

# Group the data by the date and count the number of reviews for each date
review_count_by_date = df2.groupby('date').size()

# Create a time series chart
plt.figure(figsize=(12, 6))
plt.plot(review_count_by_date.index, review_count_by_date.values, marker='o', linestyle='-')
plt.title('Review Frequency Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Reviews')
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

# Show the chart
plt.show()


# In[15]:


location_ratings = df2.groupby('Location')['Review'].apply(lambda x: (x.str.count("impressed|great|excellent|friendly|good") - x.str.count("old|small rooms|poor service|dirty|unresponsive")).mean())

# Sort the locations by average rating in descending order
location_ratings = location_ratings.sort_values(ascending=False)

# Print the location-based ratings
print(location_ratings)


# In[16]:


# Display the top 10 locations with the highest ratings
location_ratings = location_ratings[:10]

# Create a bar chart with rotated x-axis labels
plt.figure(figsize=(12, 6))
ax = sns.barplot(x=location_ratings.index, y=location_ratings.values, palette="Reds_d")
plt.title('Top 10 Location-Based Ratings')
plt.xlabel('Location')
plt.ylabel('Average Rating')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')  # Rotate and adjust alignment
plt.tight_layout()

# Show the chart
plt.show()


# In[17]:


# Sort the locations by average rating in ascending order to get the lowest ratings
location_ratings = location_ratings.sort_values()

# Display the top 10 locations with the lowest ratings
top_10_lowest_ratings = location_ratings.head(10)

# Create a bar chart for the top 10 lowest-rated locations
plt.figure(figsize=(12, 6))
ax = sns.barplot(x=top_10_lowest_ratings.index, y=top_10_lowest_ratings.values, palette="Blues_d")
plt.title('Top 10 Locations with Lowest Ratings')
plt.xlabel('Location')
plt.ylabel('Average Rating')
ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')  # Rotate and adjust alignment
plt.tight_layout()

# Show the chart
plt.show()


# In[ ]:




