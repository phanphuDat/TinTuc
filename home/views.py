from django.shortcuts import render

# Create your views here.
from django.views import View

from home.models import Post, KhachHang


class Index(View):
    def get(self, request):
        sql = "SELECT * From home_post ORDER BY post_id DESC "
        post = Post.objects.raw(sql)
        post2 = post[:2]
        context = {
            'post': post,
            'post2': post2
        }
        return render(request, 'home/index.html', context)

    def post(self, request):
        fname = request.POST.get('fname')
        email = request.POST.get('email')
        new_KH = KhachHang()
        new_KH.email = email
        new_KH.tenDayDu = fname
        new_KH.save()
        sql = "SELECT * From home_post ORDER BY post_id DESC "
        post = Post.objects.raw(sql)
        post2 = post[:2]
        context = {
            'post': post,
            'post2': post2,
            'mess':'Đăng ký nhận tin thành công'
        }
        return render(request, 'home/index.html', context)


class Post_(View):
    def get(self, request,post_id):
        sql = "SELECT * From home_post where post_id ='"+str(post_id)+"'"
        post = Post.objects.raw(sql)

        context = {
            'post': post,

        }
        return render(request, 'home/blog.html', context)
