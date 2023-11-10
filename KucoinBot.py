import os
import ccxt

#def validateClient():
    #key = os.environ.get('KUCOIN_KEY')
    #secret = os.environ.get('KUCOIN_SECRET')
    #passphrase = os.environ.get('KUCOIN_PASSPHRASE')
    #return kucoin

def long(ticker, kucoin):
    try:
        balance = kucoin.fetchBalance()['info']['data']['availableBalance']
        kucoin.createOrder(symbol=ticker, type='limit', side='buy', amount=10, price='1.43',params={'leverage':'1',
                                                                                               'size':balance*0.3})
        kucoin.fetchOpenOrders(symbol=ticker)
    
    except Exception as e:
        print(e)

def short(ticker, kucoin):
    try:
        balance = kucoin.fetchBalance()['info']['data']['availableBalance']
        kucoin.createOrder(symbol=ticker, type='limit', side='sell', amount=10, price='1.48',params={'leverage':'1',
                                                                                                'size':balance*0.1})
        kucoin.fetchOpenOrders(symbol=ticker)

    except Exception as e:
        print(e)


