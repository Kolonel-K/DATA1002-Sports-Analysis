import pandas as pd

contents_df = pd.read_csv(r"C:\Users\berni\Documents\GitHub\DATA1002-Sports-Analysis\AusGov Sports Data\data\csv_files\Contents.csv")
three_df = pd.read_csv(r"C:\Users\berni\Documents\GitHub\DATA1002-Sports-Analysis\AusGov Sports Data\data\csv_files\Table 3.csv")
threeA_df = pd.read_csv(r"C:\Users\berni\Documents\GitHub\DATA1002-Sports-Analysis\AusGov Sports Data\data\csv_files\Table 3a.csv")

contentsColumns = contents_df.columns.tolist()
three_csv = three_df.columns.tolist()
threeA_csv = threeA_df.columns.tolist()

print(contentsColumns)
print(three_csv)
print(threeA_csv)