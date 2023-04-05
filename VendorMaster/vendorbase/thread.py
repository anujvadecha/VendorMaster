class thread:
    help = 'Process to send gold ticker data'
    def background_process():
        import time
        print("process started")
        time.sleep(100)
        print("process finished")

    def index(request):
        import threading
        t = threading.Thread(target=handle, args=(), kwargs={})
        t.setDaemon(True)
        t.start()
        return HttpResponse("main thread content")

 
    def handle(self, *args, **options):
        while True:
            tick={
                    "type":"tick",
                    "gold_tick":
                    {
                        "bid": randint(40000, 60000),
                        "ask": randint(40000, 60000)
                    }
                }
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                settings.SOCKET_GROUP,
                tick
            )
            update_high_low.delay(tick)
            time.sleep(1)