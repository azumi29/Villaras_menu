import pandas as pd
import numpy as np
 
# EXCELファイルとCSVファイルを読み込む
menu = pd.read_excel('menu.xlsx')                       # ★★★!!!ファイル名入力!!!★★★
menu = pd.melt(menu)                                    # データを縦に並べる
menu.columns = ['date', 'menu']
menu_per_person = pd.read_csv('menu_per_person2.csv')   # ★★★!!!ファイル名入力!!!★★★

# データを結合してNaNのある行を削除
df_list = pd.merge(menu,menu_per_person)
df_list = df_list.dropna()

# 必要量を新しい列に追加
df_list['amount'] = df_list['per_person'] * 7            # ★★★!!!人数入力!!!★★★
 

# shopping list作成
df_shopping_list = df_list[['food', 'amount']].groupby('food').sum()
df_shopping_list['amount'] = np.ceil(df_shopping_list['amount'])               # 切り上げ
unit_dict = dict(zip(df_list["food"], df_list["unit"]))                        # 列を追加するための辞書
category_dict = dict(zip(df_list["food"], df_list["category"]))                # 列を追加するための辞書
df_shopping_list['unit'] = pd.DataFrame.from_dict(unit_dict, 'index')          # 列の追加
df_shopping_list['category'] = pd.DataFrame.from_dict(category_dict, 'index')  # 列の追加
df_shopping_list = df_shopping_list.sort_values('category')                    # categoryごとの並べ替え
print(df_shopping_list)

# shopping list出力
df_shopping_list.to_csv("shopping_list.csv", encoding='cp932')


# cooking list作成
df_cooking_list = df_list.drop(columns=['date','per_person', 'category'])               # 不要な列の削除
df_cooking_list = df_cooking_list.reindex(columns=['menu', 'food', 'amount', 'unit'])   # columnsの並び変え
df_cooking_list['amount'] = np.ceil(df_cooking_list['amount'])                          # 切り上げ
print(df_cooking_list)

# cooking list出力
df_cooking_list.to_csv("cooking_list.csv", encoding='cp932', index = False)