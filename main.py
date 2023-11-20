from dlm import dlm
from database import MongoDB
import pandas as pd
import indicators
import requests
import json

strategy = """Buy 1000 COCACOLA HBC A shares when Value is Above average over last week, 
             sell 1000 COCACOLA HBC A shares when Value is Below average over last week. show over 3 months"""

def get_response(strategy):
             dlm_response = dlm.create_trade_dict(strategy)
             print(dlm_response)
             # dlm_response['symbol'] = 'CCH'
             # dlm_response['timeframe'] = 20230502
             print(dlm_response)
             filter = {
             'trading_day': {
             '$gte': 20230501,
             '$lte': 20230502
             },
             'symbol': dlm_response['symbol']
             }
             #filter = {'symbol': dlm_response['symbol'], "trading_day": dlm_response['timeframe']}
             rep = MongoDB().get('data',filter)
             data = pd.DataFrame(rep)
             data['trade_consideration'] = pd.to_numeric(data['trade_consideration'], errors='coerce')  # Convert to numeric, coerce non-numeric values to NaN
             trades = indicators.simple_moving_average(data, 'trade_consideration', 'agreed_time')
             trades_df = indicators.tracking_trades(trades,  'trade_consideration', dlm_response['quantity'])
             trades_df, pnl_df = indicators.profit_loss(data, trades_df)
             report = openai_report(json.loads(pnl_df.tail(100).to_json()), strategy)
             return trades_df, pnl_df, report



def openai_report(data,strategy):


    messages = [{"role": "system", 
          "content": f"""
                          You are an AI Stock Trading Bot Expert. Give an expert analysis on the data below.

                          You are given the total Profit & Loss (P&L) made based on the strategy made over the period and 
                          compare it with the P&L of simply buying and holding shares for the same time period.

                          STRATEGY: {strategy}

                          Give a comprehensive report on the Profit and loss data you are provided with. 
                """},
         {"role": "user", 
          "content":f"""Profit & Loss (P&L) data: {data}"""}
    ]
    #messages.extend(data)

    openai_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer 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"
    }

    payload = {
        "model": "gpt-3.5-turbo-16k-0613",
        "messages": messages,
        "temperature": 0.3,
        "max_tokens": 750
        }
    #print("context context context",context)

    # send the API request using the POST method
    response = requests.post(openai_url, headers=headers, data=json.dumps(payload))
    print("sssssssssssssssssss",response.json())
    result = response.json()['choices'][0]['message']['content']

    return result