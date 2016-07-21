from django.shortcuts import render, render_to_response, redirect
from capture.models import Packet
import socket
from struct import *


def home_page(request):
    return render(request, 'home.html')

def capture(request):
    if request.method == 'GET':
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
        cnt = 3
        while cnt != 0:
            data = s.recv(65536)
            packet_list = Packet.objects.create(context=data)
            cnt -= 1
        return redirect('/')

    return render(request, 'home.html')
