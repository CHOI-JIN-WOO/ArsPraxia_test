# 판다스 Profiling

import pandas as pd
import pandas_profiling

data = pd.read_csv("./csv/spam.csv", encoding="latin1")

print(data[:5])

#pr = data.profile_report()
