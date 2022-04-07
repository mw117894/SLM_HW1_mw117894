import SLM_HW4
import matplotlib.pyplot as plt
import statistics as stat
from statsmodels.nonparametric.smoothers_lowess import lowess as  sm_lowess
puzzles = SLM_HW4.puzzles

plays_lo = stat.median(puzzles.NbPlays)
rating_lo = 1500
rating_high = stat.quantiles(data=puzzles.Rating,n=100)[98]

puzzles_filtered = puzzles[(puzzles.NbPlays > plays_lo) & (puzzles.Rating > rating_lo) & (puzzles.Rating < rating_high)]
good = puzzles_filtered[["Rating","Popularity"]]

rating_mapping = {}

for (i, rating) in enumerate(good.Rating):
    if rating in rating_mapping.keys():
        rating_mapping[rating].append(i)
    else:
        rating_mapping[rating] = [i]

ratings = good.Rating.unique()
mean_popularities = []

for rating in ratings:
    indices = rating_mapping[rating]
    popularities = good.iloc[indices, good.columns.get_loc("Popularity")]
    mean_popularities.append(stat.mean(popularities))

sm_y, sm_x = sm_lowess(ratings, mean_popularities,frac=0.25,it=5,return_sorted=True).T

plt.scatter(x=ratings, y=mean_popularities)
plt.plot(sm_x,sm_y,color="red")
plt.xlabel = "rating"
plt.ylabel = "popularity"
plt.tight_layout()
plt.show()

