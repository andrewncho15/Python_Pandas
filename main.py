import pandas as pd
import statsmodels.formula.api as smf

turkeydf = pd.read_csv("/Users/andrewcho/Downloads/01_turkey_animal_data.csv")
print(turkeydf.dtypes)

model = smf.ols("ADG ~ C(Diet)", data=turkeydf).fit()

print(model.summary())