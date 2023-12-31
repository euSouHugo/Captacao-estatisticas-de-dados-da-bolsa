import yfinance as yf
from datetime import datetime
import pandas as pd

def download_and_traform(ticker, start_date, end_date):
    try:
        data_inicio = datetime.strptime(start_date, "%Y-%m-%d")
        data_final = datetime.strptime(end_date, "%Y-%m-%d")
        
        dados = yf.download(ticker, start=data_inicio, end=data_final, period='1d')
        dados_reset = dados.reset_index()
        
        df = dados_reset
    
    except Exception as e:
        print(f"Erro ao baixar dados para {ticker} entre {start_date} e {end_date}: {e}")
        df = None

    return df

def filter_by_variation(df, variation):
    v = variation / 100

    if variation < 0:
        condition = (df['Low'] <= ((v * df['Open']) + df['Open']))
        total_gain_condition = (df['Close'] >= ((v * df['Open']) + df['Open']))
        total_loss_condition = (df['Close'] < ((v * df['Open']) + df['Open']))
    else:
        condition = (df['High'] >= (df['Open'] + v * df['Open']))
        total_gain_condition = (df['Close'] <= ((v * df['Open']) + df['Open']))
        total_loss_condition = (df['Close'] > ((v * df['Open']) + df['Open']))

    total_trades = len(df[condition])
    total_gain = len(df[condition & total_gain_condition])
    total_loss = len(df[condition & total_loss_condition])

    percent_gain = (total_gain / total_trades) * 100 if total_trades > 0 else 0
    percent_loss = (total_loss / total_trades) * 100 if total_trades > 0 else 0

    result = {'total_trades': total_trades, 'total_gain': total_gain, 'total_loss': total_loss,
              'percent_gain': percent_gain, 'percent_loss': percent_loss}

    return result