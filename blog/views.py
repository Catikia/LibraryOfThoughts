from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# Create your views here.

#this is the view for the home page
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    cats = Category.objects.all()
    ordering = ['-thought_date']#order by reverse date
    #ordering = ['-id']#negative id to be reverse order when there is no date field

    #this adds drop-down in menu on this page
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all() #pulls all from model - there is only 'name' in it, so .all() works
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

class CategoryListView(ListView):
    model = Post
    template_name = 'category_list.html'

def CategoryListView2(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})

def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-',' '))
    return render(request, 'categories.html', {'cats':cats.title().replace('-',' '), 'category_posts':category_posts})

#this is the view for the details page
class BlogpostDetailView(DetailView):
    model = Post
    template_name = 'blogpost_details.html'

    #this adds drop-down in menu on this page
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all() #pulls all from model - there is only 'name' in it, so .all() works
        context = super(BlogpostDetailView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

#this is the view for the Add category page
class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = '__all__' #<-- if wanting default form instead of forms.py -->
    #field = ('title', 'body') <--if not all fields wanted then list instead -->

    #this adds drop-down in menu on this page
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all() #pulls all from model - there is only 'name' in it, so .all() works
        context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

#this is the view for the Add thought page
class AddThoughtView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm #used for using forms.py
    template_name = 'add.html'
    #fields = '__all__' <-- if wanting default form instead of forms.py -->
    field = ('title', 'category', 'subject', 'thoughts')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    #this adds drop-down in menu on this page
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all() #pulls all from model - there is only 'name' in it, so .all() works
        context = super(AddThoughtView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

#this is the view for the Edit thought page
class EditThoughtView(UpdateView):
    model = Post
    form_class = EditForm #used for using forms.py
    template_name = 'edit_thought.html'

    #this adds drop-down in menu on this page
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all() #pulls all from model - there is only 'name' in it, so .all() works
        context = super(EditThoughtView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context

#this is the view for the Remove Thought page
class RemoveThoughtView(DeleteView):
    model = Post
    template_name = 'remove_thought.html'
    #reverse does not work on delete, reverse_lazy is needed instead to send back home page
    success_url = reverse_lazy('home')

    #this adds drop-down in menu on this page
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all() #pulls all from model - there is only 'name' in it, so .all() works
        context = super(RemoveThoughtView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
