import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib
 
#CSVファイルを読み込む
menu = pd.read_csv('menu.csv')
menu_per_person = pd.read_csv('menu_per_person2.csv')

# print(menu)
df_list = pd.merge(menu,menu_per_person)
# df_list['amount'] = df_list['per_person'] * df_list['number']
df_list['amount'] = df_list['per_person'] * 7
print(df_list)

unit_dict = dict(zip(df_list["food"], df_list["unit"]))
category_dict = dict(zip(df_list["food"], df_list["category"]))

# df_food_list = df_list.groupby(('food', 'amount'), as_index=False).sum()
# df_food_list = df_list[['food', 'amount', 'unit']].groupby('food', as_index=False).sum()
df_food_list = df_list[['food', 'amount']].groupby('food').sum(). round()
df_food_list['unit'] = pd.DataFrame.from_dict(unit_dict, 'index')
df_food_list['category'] = pd.DataFrame.from_dict(category_dict, 'index')
df_food_list = df_food_list.sort_values('category')

# df_food_list.to_csv("shopping_list5.csv", encoding='cp932')
print(df_food_list)