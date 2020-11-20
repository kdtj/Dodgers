#import libraries and set up options
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#load data from csv
events = pd.read_csv('gameevents.csv')
rosters = pd.read_csv('gamerosters.csv')
teams = pd.read_csv('teams.csv')

# Merge all three csv files
allpasses = pd.merge(events, teams, on='teamId', how='left')
allpasses = pd.merge(allpasses, rosters, on='playerId', how='left')

# Drop all failed outcomes
allpasses.drop((allpasses[ allpasses['outcome'] == 'failed'].index) , inplace = True)

# Only keep strings pass and reception from name column
pass_reception = ['pass','reception']
allpasses = allpasses[allpasses['name'].isin(pass_reception)]

# Split dataframe in two with pass and reception in separate datasframes
passing = ['pass']
Passes = allpasses[allpasses['name'].isin(passing)]

receipts = ['reception']
Receptions = allpasses[allpasses['name'].isin(receipts)]

# Merge both dataframes above based on the time of the pass. Right dataframe (Receptions) is merged to the nearest value equal or above the left dataframe.
Passes_in_order = pd.merge_asof(Passes, Receptions, direction='forward', on='gameTime')

# Keep rows Applicable to Washington Only and Isolate for Forwards
Washington = Passes_in_order[Passes_in_order['teamName_x'] == 'Capitals']
WashForwards = Washington[(Washington['playerPosition_x'] != 'D') & (Washington['playerPosition_x'] != 'G')]

# Set X and Y coordinates for Scatterplot
x = WashForwards.xAdjCoord_x.values
y = WashForwards.yAdjCoord_x.values
x2 = WashForwards.xAdjCoord_y.values
y2 = WashForwards.yAdjCoord_y.values

# Plot Scatterplot with team color
plt.scatter(x,y,color="#E21936",alpha=1)
plt.plot([x,x2],[y,y2],alpha=0.3,color="black")
plt.title('Washington Forwards Completed Passes')
plt.show()

# Keep rows Applicable to Pittsburgh Only and Isolate for Forwards
Pittsburgh = Passes_in_order[Passes_in_order['teamName_x'] != 'Capitals']
PittForwards = Pittsburgh[(Pittsburgh['playerPosition_x'] != 'D') & (Pittsburgh['playerPosition_x'] != 'G')]

# Set X and Y coordinates for Scatterplot
x = PittForwards.xAdjCoord_x.values
y = PittForwards.yAdjCoord_x.values
x2 = PittForwards.xAdjCoord_y.values
y2 = PittForwards.yAdjCoord_y.values

# Plot Scatterplot with team color
plt.scatter(x,y,color="#C5B358",alpha=1)
plt.plot([x,x2],[y,y2],alpha=0.3,color="black")
plt.title('Pittsburgh Forwards Completed Passes')
plt.show()

# Keep rows Applicable to Washington Defensemen only
Washington = Passes_in_order[Passes_in_order['teamName_x'] == 'Capitals']
WashDefense = Washington[Washington['playerPosition_x'] == 'D']

# Set X and Y coordinates for Scatterplot
xx = WashDefense.xAdjCoord_x.values
yx = WashDefense.yAdjCoord_x.values
x2x = WashDefense.xAdjCoord_y.values
y2x = WashDefense.yAdjCoord_y.values

# Plot Scatterplot with team color
plt.scatter(xx,yx,color="#E21936",alpha=1)
plt.plot([xx,x2x],[yx,y2x],alpha=0.3,color="black")
plt.title('Washington Defensemen Completed Passes')
plt.show()

# Keep rows Applicable to Pittsburgh Defensemen only
Pittsburgh = Passes_in_order[Passes_in_order['teamName_x'] != 'Capitals']
PittDefense = Pittsburgh[Pittsburgh['playerPosition_x'] == 'D']

# Set X and Y coordinates for Scatterplot
xx = PittDefense.xAdjCoord_x.values
yx = PittDefense.yAdjCoord_x.values
x2x = PittDefense.xAdjCoord_y.values
y2x = PittDefense.yAdjCoord_y.values

# Plot Scatterplot with team color
plt.scatter(xx,yx,color="#C5B358",alpha=1)
plt.plot([xx,x2x],[yx,y2x],alpha=0.3,color="black")
plt.title('Pittsburgh Defensemen Completed Passes')
plt.show()
