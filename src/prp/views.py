from django.shortcuts import render

def home(request):
    return render(request, 'home.html', {
        'her_name': 'PIDDU',
        'your_name': 'Himanshu'
    })

def yes_page(request):
    return render(request, 'yes.html', {
        'her_name': 'PIDDU',
        'your_name': 'Himanshu'
    })
