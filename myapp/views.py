from django.shortcuts import render
from .forms import Form
from .models import Post

articles = [
    {
        'title': 'rgdgrd',
        'content': 'wdaf',
        'img': 'https://images.unsplash.com/photo-1566275529824-cca6d008f3da?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8cGhvdG98ZW58MHx8MHx8&w=1000&q=80'
    },
    {
        'title': 'wad',
        'content': 'sefesfes',
        'img': 'https://images.unsplash.com/photo-1566275529824-cca6d008f3da?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8cGhvdG98ZW58MHx8MHx8&w=1000&q=80'
    },
    {
        'title': 'hdrhrd',
        'content': 'rdgdrg',
        'img': 'https://images.unsplash.com/photo-1566275529824-cca6d008f3da?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8cGhvdG98ZW58MHx8MHx8&w=1000&q=80'
    },
]


def index(request):
    if request.method == 'POST':
        title = request.POST['title']
        url = request.POST['url']
        content = request.POST['content']
        Post.objects.create(title=title, url=url, content=content)
        # Post.save()
    return render(request, 'index.html', context={'articles': Post.objects.all()})


def form(request):
    if request.method == 'POST':
        form = Form(request.POST)
        if form.is_valid():
            return render(request, 'form.html', context={
                'form': form,
                'data': request.POST
            })
    else:
        form = Form()
    
    print([i for i in form])
    
    return render(request, 'form.html', {'form': Form})
