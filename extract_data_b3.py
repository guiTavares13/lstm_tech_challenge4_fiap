import sys
from datetime import datetime, timedelta
import yfinance as yf

class ExtractDataB3():
  def __init__(self, start_date, end_date) -> None:
    self.start_date = start_date
    self.end_date = end_date

  def extract(self):
    symbol = 'DIS'
    df = yf.download(symbol, start=self.start_date, end=self.end_date)
    return df

  def save_data(self, df):
    csv_data = df.to_csv('out.csv')
      


#date_parameter = sys.argv[1].split("T")[0]
date_parameter = '2024-06-11'
end_date = datetime.strptime(date_parameter, '%Y-%m-%d')
start_date_temp = end_date - timedelta(days=628)
start_date = start_date_temp.strftime('%Y-%m-%d')

try:
  extract_data_b3 = ExtractDataB3(start_date, end_date)
  df = extract_data_b3.extract()
  extract_data_b3.save_data(df)
except Exception as e:
  print(f'Não foi possível extrair os dados - {e}')
