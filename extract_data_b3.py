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
    csv_data = df.to_csv(index=False)
    try:
      mounts = dbutils.fs.ls('/mnt/streaming-avro/tech_challenge/extracao/')
    except Exception as e:
      print(f'Erro: Montagem não encontrada - {e}')
      return
    dbutils.fs.put(
      f'/mnt/streaming-avro/tech_challenge/extracao/{self.end_date.strftime("%Y%m%d")}/extracao_lote_{self.start_date}_{self.end_date.strftime("%Y-%m-%d")}.csv', 
      csv_data
    )

date_parameter = sys.argv[1].split("T")[0]
#date_parameter = '2024-11-18'
end_date = datetime.strptime(date_parameter, '%Y-%m-%d')
seven_days_before = end_date - timedelta(days=730)
start_date = seven_days_before.strftime('%Y-%m-%d')

try:
  extract_data_b3 = ExtractDataB3(start_date, end_date)
  df = extract_data_b3.extract()
  extract_data_b3.save_data(df)
except Exception as e:
  print(f'Não foi possível extrair os dados - {e}')
