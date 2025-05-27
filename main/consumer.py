from channels.generic.websocket import AsyncJsonWebsocketConsumer
from .models import LikeDislike, Post

class LikeDislikeConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("likes_group", self.channel_name)

    async def receive_json(self, data):
        post = await Post.objects.aget(id=data["post_id"])
        vote, created = await LikeDislike.objects.aget_or_create(user=self.scope["user"], post=post)

        if not created and vote.vote == data["vote"]:
            await self.send_json({"message": "Вы уже голосовали этим способом"})
            return

        vote.vote = data["vote"]
        await vote.asave()

        await self.channel_layer.group_send(
            "likes_group",
            {
                "type": "update_likes",
                "post_id": post.id,
                "total_likes": await LikeDislike.objects.filter(post=post, vote=1).acount(),
                "total_dislikes": await LikeDislike.objects.filter(post=post, vote=-1).acount()
            }
        )

    async def update_likes(self, event):
        await self.send_json(event)
