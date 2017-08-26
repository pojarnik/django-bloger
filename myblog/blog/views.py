from django.shortcuts import render
from .forms import PostForm

from .models import Post

# Create your views here.
def post_list(request):
    # try:
    #    name = request.GET['name']
    # except KeyError:
    #     name = 'simple none'

    name = request.GET.get('name', 'no name!')
    return render(request, 'blog/post_list.html', {'name':name})

def post_new(request):
    if request.method == 'POST':
        print('POST method is took\n', request.POST)
        form = PostForm(request.POST)
        form2 = Post()
        form2.name = "YOOO"
        form2.surname = "HARDDDDD"
        form2.publish()
        form.save()
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form':form})

def post_edit(request, key, key2):
    print('parametr key = ', key, 'parametr key2 = ', key2)
    print('name contains 44:', Post.objects.filter(name__contains='44'))
    return render(request, 'post_new.html', {'key':key, 'key2':key2})