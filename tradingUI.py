from graphics import *
import sys
import os
import ccxt
#matplotlib.use('Tkagg')

def validateClient():
    key = os.environ.get('KUCOIN_KEY')
    secret = os.environ.get('KUCOIN_SECRET')
    passphrase = os.environ.get('KUCOIN_PASSPHRASE')
    kucoin = ccxt.kucoinfutures({'apiKey':key,'secret':secret,'password':passphrase})
    return kucoin

def long(ticker, kucoin):
    try:
        balance = kucoin.fetchBalance()['info']['data']['availableBalance']
        kucoin.createOrder(symbol=ticker, type='market', side='buy', amount=10,params={'leverage':'10',
                                                                                        'size':balance*0.1})
    
    except ccxt.base.errors.BadSymbol:
        print('Error: {}'.format(ccxt.base.errors.BadSymbol))
    
def short(ticker, kucoin):
    try:
        balance = kucoin.fetchBalance()['info']['data']['availableBalance']
        kucoin.createOrder(symbol=ticker, type='market', side='sell', amount=10,params={'leverage':'10',
                                                                                        'size':balance*0.1})

    except ccxt.base.errors.BadSymbol:
        print('Error: {}'.format(ccxt.base.errors.BadSymbol))


def show(win, tickerEntry, kucoin):

    while True:
        pt = win.getMouse()

        # GET TICKER WHEN LONG/SHORT

        if (pt.getX()) > 230 and (pt.getX() < 330):
            if (pt.getY()) > 70 and (pt.getY()) < 110:
                ticker = tickerEntry.getText().upper() + 'USDTM'
                long(ticker, kucoin)
                show(win, tickerEntry, kucoin)
            else:
                show(win, tickerEntry, kucoin)

        if (pt.getX()) > 230 and (pt.getX() < 330):
            if (pt.getY()) > 120 and (pt.getY()) < 160:
                ticker = tickerEntry.getText().upper() + 'USDTM'
                short(ticker, kucoin)
                show(win, tickerEntry, kucoin)
            else: show(win, tickerEntry, kucoin)
        
        if (pt.getX()) > 380 and (pt.getX()) < 400:
            if (pt.getY()) > 0 and (pt.getY()) < 20:
                win.close()
                sys.exit()
        else:
            pass

def gui():
    
    # MAKE GUI

# gui square
    win = GraphWin('NEWS TRADE TERMINAL', 400, 200)
    win.setBackground("black")

#title and button
    title = Text(Point(200,40), "NEWS TRADE TERMINAL")
    title.setSize(15)
    title.setTextColor("white")
    title.draw(win)

    titleButton = Rectangle(Point(100,25), Point(300, 55))
    titleButton.setOutline('white')
    titleButton.draw(win)

#ticker text and entry
    tickerText = Text(Point(70, 120), 'TICKER: ')
    tickerText.setTextColor('white')
    tickerText.setSize(20)
    tickerText.setStyle('bold')
    tickerText.draw(win)

    tickerEntry = Entry(Point(150, 120), 10)
    tickerEntry.setTextColor('black')
    tickerEntry.draw(win)

#long and short button
    longButton = Rectangle(Point(230, 70), Point(330, 110))
    longButton.setOutline('black')
    longButton.setFill('green')
    longButton.draw(win)

    longText = Text(Point(280, 90), 'LONG')
    longText.setSize(20)
    longText.setStyle('bold')
    longText.setTextColor('white')
    longText.draw(win)


    shortButton = Rectangle(Point(230, 120), Point(330, 160))
    shortButton.setOutline('black')
    shortButton.setFill('red')
    shortButton.draw(win)

    shortText = Text(Point(280, 140), 'SHORT')
    shortText.setSize(20)
    shortText.setStyle('bold')
    shortText.setTextColor('white')
    shortText.draw(win)

#exit cross button
    exitButton = Rectangle(Point(380,0), Point(400, 20))
    exitButton.setOutline("red")
    exitButton.setFill("red")
    exitButton.draw(win)

    exitText = Text(Point(390,10), "X")
    exitText.setTextColor("white")
    exitText.setSize(10)
    exitText.draw(win)

    return win, tickerEntry


if __name__=='__main__':
    kucoin = validateClient()  # function from KucoinFuturesBot.ipynb script
    win, tickerEntry = gui()
    show(win,tickerEntry, kucoin)  # runs function