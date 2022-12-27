import os
import pandas as pd

Transcription_Profiles_Of_Cell_Lines = pd.read_csv("dbs/CCLE_expression-2.csv",index_col=0)
print(Transcription_Profiles_Of_Cell_Lines)