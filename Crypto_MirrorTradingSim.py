import requests
import json
import pandas as pd
pd.options.display.max_columns = None
pd.options.display.width=None
from openpyxl import load_workbook

import os
#from binance.client import Client

import time

import urllib.request

import threading
from IPython.display import display

#st_row = 0 #for excel startrow

ethusdt_url_binance = "https://api.binance.com/api/v1/ticker/price?symbol=ETHUSDT"
daieth_url_binance = "https://api.binance.com/api/v1/ticker/price?symbol=ETHDAI"
usdceth_url_binance = "https://api.binance.com/api/v1/ticker/price?symbol=ETHUSDC"

writer = pd.ExcelWriter('thread.xlsx', engine='openpyxl')

def th_ethusdt():
    t0 = time.time()
    print ("Thread 1: " + str(t0) + "\n")

    st_row = 0

    query = """ query {
    swaps(orderBy: timestamp, orderDirection: desc, first: 5, where:
     { pair: "0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852" }
    ) {
         pair {
           token0 {
             symbol
           }
           token1 {
             symbol
           }
         }
         amount0In
         amount0Out
         amount1In
         amount1Out
         amountUSD
         to
         timestamp
     }
    }
    """

    url = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2'
    r = requests.post(url, json={'query': query})
    #print(r.status_code)
    #print(r.text)

    json_data = json.loads(r.text)

    df_data = json_data['data']['swaps']
    df1 = pd.DataFrame(df_data)
    df1 = df1.iloc[::-1]
    
    st_row += len(df1)+1

    data = urllib.request.urlopen(ethusdt_url_binance).read().decode()
    obj = json.loads(data)
    binance_current_price = (obj['price'])
    print(binance_current_price)

    current_price = []
    for x in range(len(df1)):
        current_price.append(binance_current_price)
    
    df1['current_price'] = current_price

    display(df1)
    #writer = pd.ExcelWriter('thread.xlsx', engine='openpyxl')
    df1.to_excel(writer, sheet_name='Sheet1', index=False)
    
    t1 = time.time()
    print ("Thread 1: " + str(t1) + "\n")

    th_ethusdt_loop(st_row, df1)


def th_daieth():
    t0 = time.time()
    print ("Thread 2: " + str(t0) + "\n")
    
    st_row = 0
    
    query = """ query {
    swaps(orderBy: timestamp, orderDirection: desc, first: 5, where:
     { pair: "0xa478c2975ab1ea89e8196811f51a7b7ade33eb11" }
    ) {
         pair {
           token0 {
             symbol
           }
           token1 {
             symbol
           }
         }
         amount0In
         amount0Out
         amount1In
         amount1Out
         amountUSD
         to
         timestamp
     }
    }
    """

    url = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2'
    r = requests.post(url, json={'query': query})
    #print(r.status_code)
    #print(r.text)

    json_data = json.loads(r.text)

    df_data = json_data['data']['swaps']
    df1 = pd.DataFrame(df_data)
    df1 = df1.iloc[::-1]
    
    st_row += len(df1)+1

    data = urllib.request.urlopen(daieth_url_binance).read().decode()
    obj = json.loads(data)
    binance_current_price = (obj['price'])
    print(binance_current_price)

    current_price = []
    for x in range(len(df1)):
        current_price.append(binance_current_price)
    
    df1['current_price'] = current_price

    display(df1)
    #writer = pd.ExcelWriter('thread.xlsx', engine='openpyxl')
    df1.to_excel(writer, sheet_name='Sheet2', index=False)

    t1 = time.time()
    print ("Thread 2: " + str(t1) + "\n")

    th_daieth_loop(st_row, df1)


def th_usdceth():
    t0 = time.time()
    print ("Thread 3: " + str(t0) + "\n")
    
    st_row = 0
    
    query = """ query {
    swaps(orderBy: timestamp, orderDirection: desc, first: 5, where:
     { pair: "0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc" }
    ) {
         pair {
           token0 {
             symbol
           }
           token1 {
             symbol
           }
         }
         amount0In
         amount0Out
         amount1In
         amount1Out
         amountUSD
         to
         timestamp
     }
    }
    """

    url = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2'
    r = requests.post(url, json={'query': query})
    #print(r.status_code)
    #print(r.text)

    json_data = json.loads(r.text)

    df_data = json_data['data']['swaps']
    df1 = pd.DataFrame(df_data)
    df1 = df1.iloc[::-1]
    
    st_row += len(df1)+1

    data = urllib.request.urlopen(usdceth_url_binance).read().decode()
    obj = json.loads(data)
    binance_current_price = (obj['price'])
    print(binance_current_price)

    current_price = []
    for x in range(len(df1)):
        current_price.append(binance_current_price)
    
    df1['current_price'] = current_price

    display(df1)
    #writer = pd.ExcelWriter('thread.xlsx', engine='openpyxl')
    df1.to_excel(writer, sheet_name='Sheet3', index=False)

    t1 = time.time()
    print ("Thread 3: " + str(t1) + "\n")

    th_usdceth_loop(st_row, df1)





def th_ethusdt_loop(st_row, df1):

    t0 = time.time()

    while True:
        # ETH USDT

        query = """ query {
        swaps(orderBy: timestamp, orderDirection: desc, first: 5, where:
         { pair: "0x0d4a11d5eeaac28ec3f61d100daf4d40471f1852" }
        ) {
             pair {
               token0 {
                 symbol
               }
               token1 {
                 symbol
               }
             }
             amount0In
             amount0Out
             amount1In
             amount1Out
             amountUSD
             to
             timestamp
         }
        }
        """

        url = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2'
        r = requests.post(url, json={'query': query})
        #print(r.status_code)
        #print(r.text)

        json_data = json.loads(r.text)

        df_data = json_data['data']['swaps']
        df2 = pd.DataFrame(df_data)
        #df2

        df2 = df2.iloc[::-1]
        #df2

        #print(len(df1))
        #print(len(df2))

        ## get latest price from Binance API
        #btc_price = client.get_symbol_ticker(symbol="BTCUSDT")

        #binance_current_price = btc_price["price"]
        #print(binance_current_price)
    
        data = urllib.request.urlopen(ethusdt_url_binance).read().decode()
        obj = json.loads(data)
        binance_current_price = (obj['price'])
        print(binance_current_price)


        if len(df2) > 0:
            for i in range(len(df2)):
                if df2.loc[i, "timestamp"] <= df1.loc[0, "timestamp"]:
                    df2 = df2.drop([i])
            print(len(df1))
            print(len(df2))
            if len(df2) > 0:
                current_price = []
                for x in range(len(df2)):
                    current_price.append(binance_current_price)
                df2['current_price'] = current_price    
                df1 = df2
                df2.to_excel(writer, sheet_name='Sheet1', index=False,header=False,startrow=st_row)
                st_row += len(df2)
        print(df2)
        time.sleep(3)
        t1 = time.time()
        if(t1-t0)>60:
            break

def th_daieth_loop(st_row, df1):

    t0 = time.time()

    while True:
        # DAI ETH

        query = """ query {
        swaps(orderBy: timestamp, orderDirection: desc, first: 5, where:
         { pair: "0xa478c2975ab1ea89e8196811f51a7b7ade33eb11" }
        ) {
             pair {
               token0 {
                 symbol
               }
               token1 {
                 symbol
               }
             }
             amount0In
             amount0Out
             amount1In
             amount1Out
             amountUSD
             to
             timestamp
         }
        }
        """

        url = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2'
        r = requests.post(url, json={'query': query})
        #print(r.status_code)
        #print(r.text)

        json_data = json.loads(r.text)

        df_data = json_data['data']['swaps']
        df2 = pd.DataFrame(df_data)
        #df2

        df2 = df2.iloc[::-1]
        #df2

        #print(len(df1))
        #print(len(df2))

        ## get latest price from Binance API
        #btc_price = client.get_symbol_ticker(symbol="BTCUSDT")

        #binance_current_price = btc_price["price"]
        #print(binance_current_price)
    
        data = urllib.request.urlopen(daieth_url_binance).read().decode()
        obj = json.loads(data)
        binance_current_price = (obj['price'])
        print(binance_current_price)


        if len(df2) > 0:
            for i in range(len(df2)):
                if df2.loc[i, "timestamp"] <= df1.loc[0, "timestamp"]:
                    df2 = df2.drop([i])
            print(len(df1))
            print(len(df2))
            if len(df2) > 0:
                current_price = []
                for x in range(len(df2)):
                    current_price.append(binance_current_price)
                df2['current_price'] = current_price    
                df1 = df2
                df2.to_excel(writer, sheet_name='Sheet2', index=False,header=False,startrow=st_row)
                st_row += len(df2)
        print(df2)
        time.sleep(3)
        t1 = time.time()
        if(t1-t0)>60:
            break

def th_usdceth_loop(st_row, df1):

    t0 = time.time()

    while True:
        # USDC ETH

        query = """ query {
        swaps(orderBy: timestamp, orderDirection: desc, first: 5, where:
         { pair: "0xb4e16d0168e52d35cacd2c6185b44281ec28c9dc" }
        ) {
             pair {
               token0 {
                 symbol
               }
               token1 {
                 symbol
               }
             }
             amount0In
             amount0Out
             amount1In
             amount1Out
             amountUSD
             to
             timestamp
         }
        }
        """

        url = 'https://api.thegraph.com/subgraphs/name/uniswap/uniswap-v2'
        r = requests.post(url, json={'query': query})
        #print(r.status_code)
        #print(r.text)

        json_data = json.loads(r.text)

        df_data = json_data['data']['swaps']
        df2 = pd.DataFrame(df_data)
        #df2

        df2 = df2.iloc[::-1]
        #df2

        #print(len(df1))
        #print(len(df2))

        ## get latest price from Binance API
        #btc_price = client.get_symbol_ticker(symbol="BTCUSDT")

        #binance_current_price = btc_price["price"]
        #print(binance_current_price)
    
        data = urllib.request.urlopen(usdceth_url_binance).read().decode()
        obj = json.loads(data)
        binance_current_price = (obj['price'])
        print(binance_current_price)


        if len(df2) > 0:
            for i in range(len(df2)):
                if df2.loc[i, "timestamp"] <= df1.loc[0, "timestamp"]:
                    df2 = df2.drop([i])
            print(len(df1))
            print(len(df2))
            if len(df2) > 0:
                current_price = []
                for x in range(len(df2)):
                    current_price.append(binance_current_price)
                df2['current_price'] = current_price    
                df1 = df2
                df2.to_excel(writer, sheet_name='Sheet3', index=False,header=False,startrow=st_row)
                st_row += len(df2)
        print(df2)
        time.sleep(3)
        t1 = time.time()
        if(t1-t0)>60:
            break


if __name__ == "__main__":
    #creating thread
    t1 = threading.Thread(target=th_ethusdt, args=())
    t2 = threading.Thread(target=th_daieth, args=())
    t3 = threading.Thread(target=th_usdceth, args=())
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    writer.close()
    print("done")



