import sqlalchemy as db
import pandas as pd
import streamlit as st
from datetime import date

engine = db.create_engine('sqlite:///wellnesssurvey4.db')
conn = engine.connect()



# Reflect the Survey table
metadata = db.MetaData()
Survey = db.Table('Survey', metadata, autoload_with=engine)

# Query all data from the Survey table
query = db.select(Survey)
result_proxy = conn.execute(query)

# Convert query results into a Pandas DataFrame
df = pd.DataFrame(result_proxy.fetchall(), columns=result_proxy.keys())

# Display the DataFrame as a table
st.write(df)

# Export the DataFrame to an Excel file
df.to_excel(f"SurveyData_{date.today()}.xlsx", index=False)

print("Data has been successfully exported to SurveyData.xlsx!")
