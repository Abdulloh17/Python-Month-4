from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from posts.models import Post, Comment
from django.views import generic
from django.urls import reverse_lazy
from posts.forms import CommentForm


# def hello(request):
#     return HttpResponse("GeekTech")


# def hello(request):
#     my_list = [1, 2, 3, 4]
#     return HttpResponse(my_list)


def hello(request):
    body = '''
    <h1>Привет</h1>
    <p>Параграф</p>
    '''
    return HttpResponse(body)

# def hello(request):
#     my_dict = ["name": "Alex"]
#     return HttpResponse

# def hello(request):
#     return HttpResponse("GeekTech", status=200, headers={"name": "Alby"})

def index(request):
    return render(request, "posts/index.html", context=None)


class IndexView(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status = True)
    context_object_name = "posts"
    extra_context = {"title": "Главная страница"}
    template_name = "posts/index.html"

class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post"
    template_name = "posts/post_detail.html"
    extra_context = {"form": CommentForm()}


    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["form"] = CommentForm()
    #     return context


    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        form = CommentForm(request.POST)

        if form.is_valid():
            pre_saved_comment = form.save(commit=False)
            pre_saved_comment.post = post
            pre_saved_comment.save()


        return redirect("post-detail", pk)
    # def post(self, request, pk):
    #     post = Post.objects.get(pk=pk)
    #     name = request.POST.get("name", None)
    #     text = request.POST.get("text", None)

    #     if name and text:
    #         comment = Comment.objects.create(name=name, text=text, post=post)
    #         comment.save()

    #     return redirect("post-detail", pk)



class PostCreateView(generic.CreateView):
    model = Post
    template_name = "posts/post_create.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("main-page") 


class PostDeleteView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy("main-page")

class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = "posts/post_update.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("main-page")

# def get_post(request, post_id):
#     try:
#         post = Post.objects.get(id=post_id)
#     except Post.DoesNotExist:
#         raise Http404('Такого поста нет')
#     return render(request, "post_detail.html", {"post": post})
    
     

def about(request):
    context = {
        "title": "О нас",
    }
    return render(request, "posts/about.html") 