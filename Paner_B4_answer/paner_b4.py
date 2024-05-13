import pandas as pd

data = pd.read_csv("Exam_Table.csv", skip_blank_lines=True).dropna()

data.transpose().to_csv("./b4_output1.csv", index = False)

print()