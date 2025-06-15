from django.shortcuts import render
from django.http import JsonResponse
from .bot import get_bot_response  # Your chatbot logic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm
from .models import ChatHistory
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import login_required
from .models import ChatHistory

def chatbot_home(request):
    return render(request, 'chatbot/chat.html')

def chatbot_response(request):  # Handles AJAX GET request
    user_input = request.GET.get("message")
    response = get_bot_response(user_input)
    return JsonResponse({"response": response})

def welcome_page(request):
    return render(request, 'chatbot/welcome.html')

@login_required
def get_response(request):
    user_message = request.GET.get('message')
    # Your bot logic here, e.g.:
    bot_response = "This is a dummy bot reply."  # Replace with real response

    # Save chat history
    ChatHistory.objects.create(user=request.user, user_message=user_message, bot_response=bot_response)

    return JsonResponse({'response': bot_response})

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('chatbot_home')
    else:
        form = RegisterForm()
    return render(request, 'chatbot/register.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('chatbot_home')
            else:
                error = "Invalid username or password."
                return render(request, 'chatbot/login.html', {'form': form, 'error': error})
    else:
        form = LoginForm()
    return render(request, 'chatbot/login.html', {'form': form})

def dashboard(request):
    if request.user.is_authenticated:
        chats = chats.objects.filter(user=request.user).order_by('-timestamp')
        return render(request, 'dashboard.html', {'chats': chats})
    return redirect('login')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard_view(request):
    # Fetch chat history for the logged-in user, order by latest first
    chats = ChatHistory.objects.filter(user=request.user).order_by('-timestamp')

    return render(request, 'chatbot/dashboard.html', {
        'chats': chats,
    })
