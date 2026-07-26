
eqList = ["INFY.NS","ITC.NS","WIPRO.NS","TCS.NS", 'HDFCBANK.NS', 'ICICIBANK.NS','BHARTIARTL.NS', 'SBIN.NS', "AUBANK.NS", "HEROMOTOCO.NS"]
#eqList = ["INFY.NS"]
date_volume_dict = {}

import yfinance as yf
#import pandas as pd

def DATA_FETCHER(eqList,per,inte):
  yf_all_stocks_data = yf.download(eqList, group_by='Ticker', period=per, interval=inte)
  return yf_all_stocks_data

  
def OUTPUT_CALCULATOR(o,avg,tf,l):
  x = date_volume_dict[o]
  #print ('l = ',l,tf)
  if x[0] > 2*avg:
    if tf == 'weekly':
      if l == 0:
        print ('\n===> Abnormal volume checked WEEKLY\t=\t')

    if tf == 'monthly':
      if l == 0:
        print ('\n===> Abnormal volume checked MONTHLY\t=\t')
    
    print (f'YES = {x[1]} ({x[0]:,}), because the volume is {x[0]/avg:,} times the average value')


def ABNORMAL_VOLUME_FINDER(time_frame,market_open_days,remaining_days,yf_vol_list,tf):
  a = len(yf_vol_list)            # indexing the list items
  l = 0

  for v in range(0,time_frame):       # First week/month and then looping on further one by one, one at a time
    time_frame_data = []
    for b in range(a-market_open_days,a):   
      x = date_volume_dict[b]
      time_frame_data.append(x[0])
    
    avg = sum(time_frame_data) / market_open_days 
    #print ('timefraeme original = ',time_frame_data)
    #print ('week/month = ',v)
    for b in range(a-market_open_days,a):
      #print ('b =',b)
      x = date_volume_dict[b]
      if x[0] > 2*avg:
        OUTPUT_CALCULATOR(b,avg,tf,l)
        l+=1
    a-=market_open_days

  if remaining_days != 0:
    for v in range(0,remaining_days):
      time_frame_data = []
      x = date_volume_dict[v]
      time_frame_data.append(x[0])
    
    avg = sum(time_frame_data) / len(time_frame_data)
    #print ('timefraeme remaining = ',time_frame_data)
    for v in range(1,remaining_days):
      x = date_volume_dict[v]
      if x[0] > 2*avg:
        #print('remaining')
        OUTPUT_CALCULATOR(v,avg,tf,l)
        l+=1
  l = 0

def WEEKLY_AVERAGE(yf_vol_list):
  market_open_days = 5
  weeks = len(yf_vol_list) // market_open_days
  remaining_days = len(yf_vol_list) % market_open_days
  tf = 'weekly'
  ABNORMAL_VOLUME_FINDER(weeks,market_open_days,remaining_days,yf_vol_list,tf)


def MONTHLY_AVERAGE(yf_vol_list):
  market_open_days = 21
  months = len(yf_vol_list) // market_open_days
  remaining_days = len(yf_vol_list) % market_open_days
  tf = 'monthly'
  ABNORMAL_VOLUME_FINDER(months,market_open_days,remaining_days,yf_vol_list,tf)


if __name__ == "__main__":
  for eq in eqList:
    print ('\n\n')
    yf_data = DATA_FETCHER(eq,'1mo','1d')
    yf_vol_list = yf_data[('Volume')].tolist()
    yf_date_list = yf_data.index.tolist()

    for vd in range(len(yf_date_list)):
      date_volume_dict.update({vd:[yf_vol_list[vd],yf_date_list[vd]]})
    
    print ('=========================================================='*3)
    print ("For the stock = ",eq)
    WEEKLY_AVERAGE(yf_vol_list)
    MONTHLY_AVERAGE(yf_vol_list)
    print ('\n\n\n')