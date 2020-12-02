import websocket
def create_web_socket(onmessage,onerror,onclose,onopen):
    # websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://127.0.0.1:8000/ws/orderEngine/",
                                on_message=onmessage,
                                on_error=onerror,
                                on_close=onclose)
    ws.on_open = onopen
    return ws