from channels.consumer import SyncConsumer,StopConsumer
from asgiref.sync import async_to_sync
import json
my_channel_name="chat_room"
class MyConsumer(SyncConsumer):
    
    def websocket_connect(self,event):
        # print("connect event...",event)
        async_to_sync(self.channel_layer.group_add)(
            my_channel_name,
            self.channel_name,
        )
        self.send(
            {
                'type':'websocket.accept',
            }
        )
    
    def websocket_receive(self,event):
        # print("receve event... ",event)
        # for i in range(10):
        #     self.send({
        #         "type":"websocket.send",
        #         "text":str(i)
        #     })
        #  sleep(1)
        async_to_sync(awaitable=self.channel_layer.group_send)(
            my_channel_name,
            {
            "type":"chat.send",
            "massage":event,
            'sender_channel_name':self.channel_name
            }
        )

    def chat_send(self,event):
        if self.channel_name!=event["sender_channel_name"]:
            self.send({
            "type":"websocket.send",
            "text":json.dumps(obj=event),
            })
            

    def websocket_disconnect(self,event):
        # print('disconnect ',event)
        raise StopConsumer()