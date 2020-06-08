from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, UserRegistrationForm,UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from .models import Contact
from actions.utils import create_action
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from actions.models import Action
from django.db.models import Count

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                username=cd['username'],
                password=cd['password'])

            if user is not None:

                if user.is_active:

                    login(request, user)
                    return HttpResponse('Authenticated '\
                    'successfully')

                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})
# Create your views here.

@login_required
def dashboard(request):

    return render(request,
        'account/dashboard.html',
        {'section': 'dashboard',})

@login_required
def notification(request):
    # Display all actions by default
    actions = Action.objects.exclude(user=request.user)
    following_ids = request.user.following.values_list('id',
                                                       flat=True)
    if following_ids:
        # If user is following others, retrieve only their actions
        actions = actions.filter(user_id__in=following_ids)
    actions = actions.select_related('user', 'user__profile').prefetch_related('target')[:10]

    return render(request,
        'account/notification.html',
        {'section': 'dashboard',
         'actions': actions})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
        # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            new_user.username=user_form.cleaned_data['username']
            new_user.email = user_form.cleaned_data['email']
            # Save the User object
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request,
                'account/register_done.html',
                {'new_user': new_user,
                 'user_form':user_form})

    else:
        user_form = UserRegistrationForm()

    return render(request,
    'account/register.html',
    {'user_form': user_form})

@login_required
def edit(request):
    images = request.user.images_created.all()

    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
            data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile,
            data=request.POST,
            files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated ' \
                              'successfully')
        else:
            messages.error(request, 'Error updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(
            instance=request.user.profile)
        paginator = Paginator(images, 9)
        page = request.GET.get('page')
        try:
            images = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer deliver the first page
            images = paginator.page(1)
        except EmptyPage:
            if request.is_ajax():
                # If the request is AJAX and the page is out of range
                # return an empty page
                return HttpResponse('')
                # If page is out of range deliver last page of results
            images = paginator.page(paginator.num_pages)
        if request.is_ajax():
            return render(request,
                          'account/edit_ajax.html',
                          {'section': 'profile', 'images': images})
    return render(request,
    'account/edit.html',
    {'user_form': user_form,
    'profile_form': profile_form,
     'user': request.user,
     'images': images})

@login_required
def user_list(request):
    users = User.objects.filter(is_active=True)
    return render(request,
        'account/user/list.html',
        {'section': 'people',
        'users': users})

@login_required
def user_detail(request, username):
    user = get_object_or_404(User,
    username=username,
        is_active=True)
    return render(request,
        'account/user/detail.html',
        {'section': 'people',
        'user': user})

@ajax_required
@require_POST
@login_required
def user_follow(request):
    user_id = request.POST.get('id')
    action = request.POST.get('action')
    if user_id and action:
        try:
            user = User.objects.get(id=user_id)
            if action == 'follow':
                Contact.objects.get_or_create(
                    user_from=request.user,
                    user_to=user)
                create_action(request.user, 'is following', user)
            else:
                Contact.objects.filter(user_from=request.user,
                    user_to=user).delete()
            return JsonResponse({'status':'ok'})
        except User.DoesNotExist:
            return JsonResponse({'status':'ko'})
    return JsonResponse({'status':'ko'})

@login_required
def user_follower(request):
    user = request.user
    user_follower = user.followers.all()
    user_followers = user_follower.annotate(follow_user=Count('followers')).order_by('-follow_user')
    paginator = Paginator(user_followers, 12)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        images = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            # If the request is AJAX and the page is out of range
            # return an empty page
            return HttpResponse('')
            # If page is out of range deliver last page of results
        images = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request,
                      'account/follow/follower_ajax.html',
                      {'section': 'profile', 'user_followers': images})
    return render(request,
        'account/follow/follower.html',
        {'section': 'profile',
        'user': user,
         'user_followers':user_followers})

@login_required
def user_following(request):
    user = request.user
    user_followin = user.following.all()
    user_following = user_followin.annotate(follow_user=Count('following')).order_by('-follow_user')
    paginator = Paginator(user_following, 12)
    page = request.GET.get('page')
    try:
        images = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        images = paginator.page(1)
    except EmptyPage:
        if request.is_ajax():
            # If the request is AJAX and the page is out of range
            # return an empty page
            return HttpResponse('')
            # If page is out of range deliver last page of results
        images = paginator.page(paginator.num_pages)
    if request.is_ajax():
        return render(request,
                      'account/follow/following_ajax.html',
                      {'section': 'profile', 'user_following': images})
    return render(request,
        'account/follow/following.html',
        {'section': 'profile',
        'user': user,
         'user_following':user_following})

