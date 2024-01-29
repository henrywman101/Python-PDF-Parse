import fitz
from pprint import pprint
import pandas as pd


new_indice = ['Asian or Asian American','Black or African American','White, non-LatinX','LatinX','Multiracial']
new_columns1 = ['Strongly agree', 'Agree', 'Somewhat agree', 'Somewhat disagree', 'Disagree', 'Strongly disagree', 'Don\'t know']
new_columns2 = ['Strongly agree', 'Agree', 'Somewhat agree', 'Somewhat disagree', 'Disagree', 'Don\'t know']
doc = fitz.open(r"../Sample_short_D-C-E_91-171_D35(125)_C12(137)_E34(171).pdf",stream=None) # open document
length=len(doc)
print(length)
for i in range(0,length-1,2):
   page = doc[i] # get the 1st page of the document
   tabs = page.find_tables() # locate and extract any tables on page
   print(f"{len(tabs.tables)} found on {page}") # display number of found tables
   if tabs.tables:  # at least one table found?.
      df=pd.DataFrame(tabs[0].extract())
      df=df.iloc[:-2,2:-1]
      df=df[df.iloc[:,0]=="Count"]
      df.drop([2],axis=1,inplace=True)
      df.columns=new_columns1
      df.index=new_indice
      df=pd.DataFrame(df.stack(future_stack=False))
      #df.reset_index().melt(id_vars='index')
      flattened_df = df.reset_index()
      #flattened_df.columns=['Ethinity Group','Response','Count']
      print(flattened_df)
   