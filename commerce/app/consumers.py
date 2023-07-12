from channels.generic.websocket import WebsocketConsumer
import json
from asgiref.sync import async_to_sync


class CommentConsumer(WebsocketConsumer):
    def connect(self):
        self.room_group_name = 'comments'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )
        self.accept()
      


    def receive(self, text_data=None, bytes_data=None):
        received_data = json.loads(text_data)
        if received_data=={'message': 'new comment'}:
            async_to_sync(self.channel_layer.group_send)(
                self.room_group_name,
                {
                    'type': 'send_message',
                    'status': 'received'
                }
            # self.send(text_data=json.dumps({'status': 'received'})) 


            )

    def send_message(self, event):
        message = event['status']
        self.send(text_data=json.dumps({'status': message}))

    



          
        


