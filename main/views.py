from django.shortcuts import render
import requests
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Zapis
from django.core.exceptions import ValidationError
import json
from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from .models import Post, Like

TELEGRAM_TOKEN = '7490506891:AAF5U3h9Fl6huTxROniSg7AZOmbuemo8dE0'
CHAT_ID = '782253016'

@csrf_exempt  
def feedback_view(request):
    if request.method == 'POST':
        try:
            
            data = json.loads(request.body) if request.content_type == 'application/json' else request.POST
            
            name = data.get('client_name')
            email = data.get('client_email')
            phone = data.get('client_phone')
            excurse = data.get('excurse')
            date = data.get('excursion_date')
            
            booking = Zapis(
                name=name,
                email=email,
                phone=phone,
                excurse=excurse,
                date=date
            )
            booking.full_clean()  
            booking.save()
            
            text = (
                f"Новая запись на экскурсию!\n"
                f"Название: {excurse}\n"
                f"Почта: {email}\n"
                f"ФИО: {name}\n"
                f"Телефон: {phone}\n"
                f"Дата: {date}"
            )
            
            response = requests.post(
                f'https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage',
                json={'chat_id': CHAT_ID, 'text': text}
            )
            
            return JsonResponse({
                'status': 'success' if response.ok else 'error',
                'booking_id': booking.id
            })
            
        except ValidationError as e:
            return JsonResponse({'status': 'error', 'errors': e.message_dict}, status=400)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
    
    return JsonResponse({'status': 'error', 'message': 'Only POST method allowed'}, status=405)

def like_post(request, post_id):
    try:
        post = get_object_or_404(Post, id=post_id)
        data = json.loads(request.body)
        value = data.get("value", True)  # ✅ Получаем значение из запроса

        Like.objects.create(post=post, value=value)  # ✅ Создаём лайк или дизлайк

        likes_count = post.likes.filter(value=True).count()
        dislikes_count = post.likes.filter(value=False).count()

        return JsonResponse({"likes": likes_count, "dislikes": dislikes_count})
    
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)






def thabest(request):
    return render(request, 'main/thabest.html' )

def index(request):
    posts = Post.objects.all()
    for post in posts:
        post.like_count = post.likes.filter(value=True).count()
        post.dislike_count = post.likes.filter(value=False).count()
    return render(request, "main/index.html", {"posts": posts})
