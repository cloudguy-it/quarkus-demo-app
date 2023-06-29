#importing pandas package
import pandas as pd

# reading JSON file
df = pd.read_json('report.json')

# displaying sample output
df.sample(5)