import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
 
#CSVファイルを読み込む
menu = pd.read_csv('menu.csv')
menu_per_person = pd.read_csv('menu_per_person2.csv')
# print(menu)
df_list = pd.merge(menu,menu_per_person)
df_list['amount'] = df_list['per_person'] * df_list['number']
print(df_list)

# df_food_list = df_list.groupby(('food', 'amount'), as_index=False).sum()
df_food_list = df_list[['food', 'amount', 'unit']].groupby('food', as_index=False).sum()

print(df_food_list)