from django.http import HttpResponse

from .models import Message


def index(request):
    message_list = list(Message.objects.order_by("pub_date"))
    return HttpResponse(message_list)
