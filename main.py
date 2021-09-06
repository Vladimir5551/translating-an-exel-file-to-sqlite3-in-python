import sqlite3
import pandas as pd

con = sqlite3.connect("name of the database .db")     # название базы данных которая будет создана
wb = pd.read_excel('Name exel file .xlsx')  #название фаила exel
for sheet in wb:
    wb[sheet].to_sql(sheet, con, index=False)

con.commit()
con.close()
# обратите внимание что база данных фомируется только из 1 листа, возможно в будущием добавлю возможность несколькихgit add README.md листов