from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . forms import MusicForm, MyUserCreationForm
from . models import Musics, User


def home(request):
    user = request.user

    # Retrieve music files based on category and ownership
    if user.is_authenticated:
        # Fetch music files uploaded by the logged-in user
        own_files = Musics.objects.filter(uploaded_by=user)

        # Fetch public music files uploaded by other users
        public_files = Musics.objects.filter(
            category='public').exclude(uploaded_by=user)

        # Fetch protected music files for which the user has access
        protected_files = Musics.objects.filter(
            category='protected', email_addresses_with_access__icontains=user.email)

        # Concatenate the queryset to display all accessible music files
        music_files = own_files | public_files | protected_files
    else:
        # If the user is not logged in, only display public music files
        music_files = Musics.objects.filter(category='public')

    return render(request, 'base/home.html', {'music_files': music_files})


def loginPage(request):
    page = 'login'

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist.')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username OR password does not exist.')

    context = {'page': page}
    return render(request, 'base/login_register.html', context)


@login_required()
def logoutUser(request):
    logout(request)
    return redirect('home')


def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occured during registration')

    return render(request, 'base/login_register.html', {'form': form})

#funciton fon uploading Music
@login_required(login_url='login')
def uploadMusic(request):
    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            music_file = form.save(commit=False)
            music_file.uploaded_by = request.user
            music_file.save()
            return redirect('home')
    else:
        form = MusicForm()

    return render(request, 'base/music_upload.html', {'form': form})
