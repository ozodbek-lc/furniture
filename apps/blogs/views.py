from django.shortcuts import render

def blogs_list_view(request):
    return render(request,'blog-list-sidebar-left.html')