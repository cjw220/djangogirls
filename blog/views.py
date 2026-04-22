from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post # 檢查這行有沒有 Post
from .forms import PostForm # 補上這行
from django.utils import timezone

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    # 這裡就是會發生 NameError 的地方，確保上面有 import Post 和 get_object_or_404
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk) # 存完後跳轉到文章詳細頁
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()  # 這行就是魔法，會直接從資料庫移除
    return redirect('post_list')  # 刪完後飛回首頁