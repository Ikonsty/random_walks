import pandas as pd
import seaborn

l_30_30 = pd.read_csv('lattice-step-size-30-30-no.csv')
# l_50_50 = pd.read_csv('lattice-step-size-50-50-no.csv')

# di_30_30 = pd.read_csv('diffusion-step-size-30-30-no.csv')
# di_50_50 = pd.read_csv('diffusion-step-size-50-50-no.csv')

# de_30_30 = pd.read_csv('deterministic-step-size-30-30-no.csv')
# de_50_50 = pd.read_csv('deterministic-step-size-50-50-no.csv')

# l_30_30.columns = ["id", "run number", "step-size", "num", "rw-type", "step", "mean distance-to-zero", "ideal distance", "mean xcor", "mean ycor", "percentage", "time-all-covered", "time-border-reached", "angles"]
# df_by_id = l_30_30.columns.groupby("step-size")#["time-all-covered"] #.count().reset_index()
# print(df_by_id)
seaborn.scatterplot(x="Step-size", y="mean", data=l_30_30)