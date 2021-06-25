import pandas as pd
from datetime import datetime

def get_display_df():
  freeboard_df = pd.read_csv(r'./database/bords/freeboard.csv')
  display_df = freeboard_df[['number', 'title', 'create_date']]
  return display_df

def create_content(title, content):
  freeboard_df = pd.read_csv(r'./database/bords/freeboard.csv')
  next_number = int(freeboard_df.iloc[-1]['number'] + 1)
  create_date = datetime.today().strftime('%Y-%m-%d')
  create_df = pd.DataFrame(data = {'number': [next_number],'title': [title], 'content': [content], 'create_date': [create_date]})

  freeboard_df = freeboard_df.append(create_df)
  freeboard_df.to_csv(r'./database/bords/freeboard.csv', index = False)

  return 'complete'

def read_content(number):
  freeboard_df = pd.read_csv(r'./database/bords/freeboard.csv')
  select_df = freeboard_df.loc[freeboard_df['number'] == number]
  return select_df

def update_content(number, title, content):
  freeboard_df = pd.read_csv(r'./database/bords/freeboard.csv')
  target_index = freeboard_df.loc[freeboard_df['number'] == number].index
  create_date = freeboard_df.loc[freeboard_df['number'] == number]['create_date'].values[0]
  update_df = pd.DataFrame(data = {'number': [number], 'title': [title], 'content': [content], 'create_date': [create_date]}, index=target_index)
  freeboard_df.update(update_df)

  freeboard_df.to_csv(r'./database/bords/freeboard.csv', index = False)

def delete_content(number):
  freeboard_df = pd.read_csv(r'./database/bords/freeboard.csv')
  target_index = freeboard_df.loc[freeboard_df['number'] == number].index
  freeboard_df = freeboard_df.drop(target_index)

  freeboard_df.to_csv(r'./database/bords/freeboard.csv', index = False)
