from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ImageCreateForm,ImageCreateImageForm, SearchForm
from django.shortcuts import get_object_or_404
from .models import Image,Comment
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from common.decorators import ajax_required
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from actions.utils import create_action
import redis
from django.conf import settings
from django.contrib.postgres.search import SearchVector,SearchQuery,SearchRank

r = redis.StrictRedis(host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB)

@login_required
def image_create(request):

    if request.method == 'POST':
        form = ImageCreateForm(data=request.POST,
                               files=request.FILES)

        if form.is_valid():
            new_item = form.save(commit=False)
            # assign current user to the item
            new_item.user = request.user
            create_action(request.user, 'عکسی را اضافه کرد با عنوان', new_item)
            new_item.save()
            messages.success(request, 'Image added successfully')
            # redirect to new created item detail view
            return redirect('/account/edit/')
    else:
        # build form with data provided by the bookmarklet via GET
        form = ImageCreateForm(data=request.GET)
        data = request.GET
        return render(request,
                      'images/image/create.html',
                      {'section': 'images',
                       'data': data,
                       'form': form})

    return render(request,
                  'images/image/create.html',
                  {'section': 'images',
                   'form': form})

@login_required
def image_create_image(request):

    if request.method == 'POST':
        form = ImageCreateImageForm(data=request.POST,
                               files=request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            # assign current user to the item
            new_item.user = request.user
            create_action(request.user, 'عکسی را آپلود کرد با عنوان', new_item)
            new_item.save()
            messages.success(request, 'Image added successfully')
            # redirect to new created item detail view
            return redirect('/account/edit/')
    else:
        # build form with data provided by the bookmarklet via GET
        form = ImageCreateImageForm(data=request.GET)
    return render(request,
                  'images/image/create_image.html',
                  {'section': 'images',
                   'form': form})

def image_detail(request, id, slug):
    image = get_object_or_404(Image, id=id, slug=slug)
    total_views = r.incr('{}'.format(image.id))
    # increment image ranking by 1
    r.zincrby('image_ranking', 1, image.id)

    if request.is_ajax():

        if request.method == 'POST':
            body = request.POST.get('body')
            user = request.user
            image=image
            if body and image:
                Comment.objects.get_or_create(
                    user=user,
                    body=body,
                    image=image)
                # assign current user to the item
                create_action(request.user, 'نظری منتشر کرد بر روی عکسی با عنوان ', image)
                # redirect to new created item detail view
                return JsonResponse({'status': 'ok'})
            return JsonResponse({'status': 'ko'})

        return render(request,
                      'images/image/detail_ajax.html',
                      {'section': 'images',
                        'image': image,
                      })
    return render(request,
        'images/image/detail.html',
        {'section': 'images',
        'image': image,
        'total_views': total_views,
         })

@ajax_required
@login_required
@require_POST
def image_like(request):
    image_id = request.POST.get('id')
    action = request.POST.get('action')
    if image_id and action:
        try:
            image = Image.objects.get(id=image_id)
            if action == 'like':
                image.users_like.add(request.user)
                create_action(request.user, 'عکسی را لایک کرد با عنوان', image)
            else:
                image.users_like.remove(request.user)
            return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ko'})

@login_required
def image_list(request):
    images = Image.objects.all()
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
              'images/image/list_ajax.html',
              {'section': 'images', 'images': images})

    return render(request,
                  'images/image/list.html',
                  {'section': 'images',
                    'images': images
                   })

@login_required
def image_ranking(request):
    # get image ranking dictionary
    image_ranking = r.zrange('image_ranking', 0, -1,
                             desc=True)[:10]
    image_ranking_ids = [int(id) for id in image_ranking]
    # get most viewed images
    most_viewed = list(Image.objects.filter(
        id__in=image_ranking_ids))
    most_viewed.sort(key=lambda x: image_ranking_ids.index(x.id))
    return render(request,
                  'images/image/ranking.html',
                  {'section': 'images',
                   'most_viewed': most_viewed})

@login_required
def image_search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            search_vector = SearchVector('title', weight='A') + SearchVector('description',
                                                                             weight='B')
            search_query = SearchQuery(query)
            results = Image.objects.annotate(
                search=search_vector,
                rank=SearchRank(search_vector, search_query)
            ).filter(rank__gte=0.1).order_by('-rank')

            paginator = Paginator(results, 4)
            page = request.GET.get('page')

            try:
                results = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer deliver the first page
                results = paginator.page(1)
            except EmptyPage:
                if request.is_ajax():
                    # If the request is AJAX and the page is out of range
                    # return an empty page
                    return HttpResponse('')
                    # If page is out of range deliver last page of results
                results = paginator.page(paginator.num_pages)

    if request.is_ajax():
        return render(request,
                      'images/search/search_ajax.html',
                      {'section': 'images', 'results': results})

    return render(request,
        'images/search/search.html',
        {'section': 'images',
         'form': form,
        'query': query,
        'results': results})