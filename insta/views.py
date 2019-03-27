from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import AddPicForm, AddProfileForm
from .models import Image, Profile, Follow
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login/')
def feed(request):
    current_user = request.user
    follow = Follow.get_followers(current_user.id)
    print(follow)
    if follow == None:
        message = 'Please follow a user for example tote or aris or create an account then upload images and follow that account ;)'
        return render(request, 'feed.html', {"message": message, "user": current_user})

    else:
        images = Image.get_images_by_id(follow.profile_id)
        current_user = None
        for item in images:
            current_user = User.objects.filter(id = item.id).first()
        # print(images)
        return render(request, 'feed.html', {"images": images, "user": current_user})
       
@login_required(login_url='/accounts/login/')
def add_picture(request):
    current_user = request.user
    profile = Profile.get_profile(current_user)
    if request.method == 'POST':
        form = AddPicForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            image.user = current_user
            image.profile = profile
            image.save()
        return redirect('feed')

    else:
        form = AddPicForm()
    return render(request, 'add_pic.html', {"form": form})

@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user = request.user
    profile = Profile.get_profile(current_user)
    if profile == None:
        return redirect('add_profile')
    else:
        images = Image.get_images_by_id(profile.id)
        return render(request, 'profile.html', {"images": images, "profile": profile})

@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = AddProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('my_profile')

    else:
        form = AddProfileForm()
    return render(request, 'add_profile.html', {"form": form})

@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'user' in request.GET and request.GET["user"]:
        profile = None
        search_term = request.GET.get("user")
        current_user = User.objects.filter(username__icontains = search_term)
        for item in current_user:
            profile = Profile.get_many_profiles(item)
            print(item)
        message = f"{search_term}"
        
        return render(request, 'search.html',{"results": profile, "user": current_user, "message":message})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def profile(request, profile_id):
    profile = Profile.get_profile_id(profile_id)
    images = Image.get_images_by_id(profile.id)
    return render(request, 'user_profile.html', {"images": images, "profile": profile})

@login_required(login_url='/accounts/login/')
def follow(request, profile_id):
    current_user = request.user
    profile = Profile.get_profile_id(profile_id)
    follow_user = Follow(user=current_user, profile=profile)
    follow_user.save()
    print(profile_id)
    myprofile_id= str(profile.id)
    return redirect('feed')

@login_required(login_url='/accounts/login/')
def like_image(request, image_id):
    image = Image.objects.get(pk =image_id)
    fav = image.likes
    if fav == None:
        fav = 0
    like = fav
    like +=1
    image = Image.update_image(image_id, like)
    return redirect('feed')
