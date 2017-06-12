from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from blog.models import Blog

class BlogList(ListView):
    model = Blog

class BlogCreate(CreateView):
    model = Blog
    fields = ['name', 'post']
    success_url = reverse_lazy('blog:blog_list')

class BlogUpdate(UpdateView):
    model = Blog
    fields = ['name', 'post']
    success_url = reverse_lazy('blog:blog_list')

class BlogDelete(DeleteView):
    model = Blog
    success_url = reverse_lazy('blog:blog_list')