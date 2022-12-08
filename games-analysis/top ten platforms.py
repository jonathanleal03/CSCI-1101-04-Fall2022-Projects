import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("game-ratings-top-10-platforms.csv")

# group by metrics
df_follow = df.groupby(["platform_name"])["follow_count"].sum().reset_index

df_follow = df_follow.rename(colums = {"follows_count"; "total_follows"})

f_hype= df.groupby(["platform_name"])["hype_count"].sum().reset_index

df_hype = df_hype.rename(colums = {"hype_count"; "total_hypes"})

# analyze data through viziluazation 
BAR_WIDTH = 0.4 

plt.bar(df_follow.index - BAR_WIDTH / 2, df_follow["total_follow"], color = "blue", label = "number of follows", width = BAR_WIDTH)

plt.bar(df_hype + BAR_WIDTH / 2, df hype["total_hypes"]. color  "red", label = "number of hype", width = BAR_WIDTH)

plt.xticks(df_follow.index, df_follow["platform_name"])

plt.legend(loc = "upper left")

plt.show()