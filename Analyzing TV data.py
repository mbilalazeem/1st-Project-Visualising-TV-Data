#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing pandas
import pandas as pd

# Loading the CSV data into DataFrames
super_bowls = pd.read_csv("super_bowls.csv")
tv =  pd.read_csv("tv.csv")
halftime_musicians =  pd.read_csv("halftime_musicians.csv")

# Displaying the first five rows of each DataFrame
display(super_bowls.head(5))
display(tv.head(5))
display(halftime_musicians.head(5))


# In[2]:


#Checking TV Dataset
tv.info()

print('\n')

# Checking Halftime musicians Dataset
halftime_musicians.info()


# In[3]:


#Visualising Data
# Importing matplotlib and set plotting style
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
plt.style.use('seaborn')

# Ploting a histogram of combined points
plt.hist(super_bowls["combined_pts"])
plt.xlabel('Combined Points')
plt.ylabel('Number of Super Bowls')
plt.show()

# Displaying the Super Bowls with the highest and lowest combined scores
display(super_bowls[super_bowls['combined_pts'] > 70])
display(super_bowls[super_bowls["combined_pts"] < 25])


# In[4]:


# Ploting a histogram of point differences
plt.hist(super_bowls.difference_pts)
plt.xlabel('Point Difference')
plt.ylabel('Number of Super Bowls')
plt.show()
# Displaying the closest game(s) and biggest blowouts
display(super_bowls.difference_pts == 1)
display(super_bowls.difference_pts >= 36)


# In[8]:


# Join game and TV data, filtering out SB I because it was split over two networks
games_tv = pd.merge(tv[tv['super_bowl'] > 1], super_bowls, on='super_bowl')

# Import seaborn
import seaborn as sns

# Create a scatter plot with a linear regression model fit
sns.regplot(x="difference_pts", y="share_household", data=games_tv)


# In[16]:


# Create a figure with 3x1 subplot and activate the top subplot
plt.subplot(3, 1, 1)
plt.plot(tv["super_bowl"], tv["avg_us_viewers"], color='#648FFF')
plt.title('Average Number of US Viewers')

# Activate the middle subplot
plt.subplot(3, 1, 2)
plt.plot(tv["super_bowl"], tv["rating_household"], color='#DC267F')
plt.title('Household Rating')

# Activate the bottom subplot
plt.subplot(3, 1, 3)
plt.plot(tv["super_bowl"], tv["ad_cost"], color='#FFB000')
plt.title('Ad Cost')
plt.xlabel('SUPER BOWL')

# Improve the spacing between subplots
plt.tight_layout()


# In[10]:


# Display all halftime musicians for Super Bowls up to and including Super Bowl XXVII
halftime_musicians[halftime_musicians.super_bowl<=27]


# In[11]:


# Count halftime show appearances for each musician and sort them from most to least
halftime_appearances = halftime_musicians.groupby('musician').count()['super_bowl'].reset_index()
halftime_appearances = halftime_appearances.sort_values('super_bowl', ascending=False)

# Display musicians with more than one halftime show appearance
halftime_appearances[halftime_appearances['super_bowl'] > 1]


# In[12]:


# Filter out most marching bands
no_bands = halftime_musicians[~halftime_musicians.musician.str.contains('Marching')]
no_bands = no_bands[~no_bands.musician.str.contains('Spirit')]

# Plot a histogram of number of songs per performance
most_songs = int(max(no_bands['num_songs'].values))
plt.hist(no_bands.num_songs.dropna(), bins=most_songs)
plt.xlabel('Number of Songs Per Halftime Show Performance')
plt.ylabel('Number of Musicians')
plt.show()

# Sort the non-band musicians by number of songs per appearance...
no_bands = no_bands.sort_values('num_songs', ascending=False)
# ...and display the top 15
display(no_bands.head(15))


# In[18]:


# 2018-2019 conference champions
patriots = 'New England Patriots'
rams = 'Los Angeles Rams'

# Who will win Super Bowl LIII?
super_bowl_LIII_winner = ...
print('The winner of Super Bowl LIII will be the', super_bowl_LIII_winner)


# In[ ]:




