import pandas as pd

data = pd.read_csv("Exam_Table.csv", skip_blank_lines=True).dropna()

data["CPEID"] = data["Entry"] + "-" + data["Replication"].astype(int).astype(str) + "-" + data["Stage"]

data.to_csv("./b3_output1.csv", index = False)

print()