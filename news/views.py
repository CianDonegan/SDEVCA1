from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import NewsArticle

class NewsListView(ListView):
    model = NewsArticle
    template_name = 'news_list.html'

    
class NewsDetailView(DetailView):
    model = NewsArticle
    template_name = 'news_detail.html'


class NewsUpdateView(UpdateView, LoginRequiredMixin,UserPassesTestMixin):
    model = NewsArticle
    fields = ('title', 'body')
    template_name = 'news_edit.html'


    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class NewsDeleteView(DeleteView, LoginRequiredMixin,UserPassesTestMixin):
    model = NewsArticle
    template_name = 'news_delete.html'
    success_url = reverse_lazy('news_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user