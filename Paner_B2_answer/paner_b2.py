import pandas as pd

data = pd.read_csv("Exam_Table.csv", skip_blank_lines=True).dropna()

sn = data["Stage"].unique()

averages = data.groupby["Stage"]["Cry1Ac,ppmDW"].mean()

output = pd.DataFrame["Stage": sn, "Mean Concentration": averages]

output.to_csv("./b2_output1.csv", index=False)

print()