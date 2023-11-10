from mac_notifications import client
import json
import websocket
import rel
import webbrowser
import chime
from tradingUI import validateClient, long

def on_open(ws):
    print("\nWebSocket connection established\n\n")

def on_message(ws, message):
    jsonMsg = fix_json(message)
    try:
        if 'source' in jsonMsg:
            print(jsonMsg)
            top=jsonMsg['source']
            subtitle=[]
            for suggestion in jsonMsg['suggestions']:
                subtitle.append(suggestion['coin'] + ' ')
            msg=jsonMsg['title']
            #url = jsonMsg['url']
            url = f'LONG {subtitle[0]}'
            send_push_notification(title=top, subtitle=subtitle, text=msg, link=url)
            print()
        elif 'source' not in jsonMsg:
            print(jsonMsg)
            title = jsonMsg['title']
            subtitle=[]
            for suggestion in jsonMsg['suggestions']:
                subtitle.append(suggestion['coin'] + ' ')
            msg=jsonMsg['body']
            #link = jsonMsg['link']
            link = f'LONG {subtitle[0]}'
            send_push_notification(title=title, subtitle=subtitle, text=msg, link=link)
            print()
    except:
        print(jsonMsg)
        print()

def on_error(ws, error):
    print("WebSocket error:", error)

def on_close(ws):
    print("WebSocket connection closed")

def fix_json(json_string):
    json_string = json_string.replace("'", "\"")
    json_string = json_string.replace(",\n}", "\n}")

    json_dict = json.loads(json_string)

    return json_dict

def send_push_notification(title, subtitle, text, link):
    try:
        client.create_notification(
            title=title,
            subtitle=subtitle,
            text=text,
            action_button_str=link),chime.success()
            #action_callback = lambda: webbrowser.open(link)), chime.success()
    
    except:
        client.create_notification(
            title=title,
            subtitle=subtitle,
            text=text,
            action_button_str=link),chime.success()
            #action_callback = lambda: webbrowser.open(link)), chime.success()


if __name__=='__main__':
    kucoin = validateClient()
    url = "wss://news.treeofalpha.com/ws"
    print("\n\nConnecting to WebSocket: ", url)
    ws = websocket.WebSocketApp(url, on_open=on_open, on_message=on_message,
                                        on_error=on_error, on_close=on_close)
    ws.run_forever(dispatcher=rel, reconnect=5)
    rel.signal(2, rel.abort)
    rel.dispatch()
