from django.views import generic
from django.urls import reverse_lazy
from .models import NewsStory
from .forms import StoryForm
from django.db.models import Q


class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
        '''Get search query from the request's GET parameters '''
        search_query = self.request.GET.get('search')

        ''' If search is present, filter queryset by author'''
        if search_query:
            queryset = NewsStory.objects.filter(Q(author__username__icontains=search_query) | Q(content__icontains=search_query))
        else:
            '''Display all stories'''
            queryset = NewsStory.objects.all()
        '''Return all news stories.'''
    
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all()[:4]
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    Context_object_name = 'story'

class StoryView(generic.DeleteView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name='story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class UpdateStoryView(generic.UpdateView):
    model = NewsStory
    form_class = StoryForm
    template_name = 'news/updateStory.html'
    context_object_name = 'story'
    success_url = reverse_lazy('news:index')

class DeleteStoryView(generic.DeleteView):
    model = NewsStory
    template_name = 'news/updateStory.html' #use same template as Update view
    context_object_name='story'
    success_url = reverse_lazy('news:index') #redirect to index page upon successful deletion

    def get(self, request, *args, **kwargs):
        #handle GET request to display the confirmation dialog
        return self.post(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        #handle POST request to delete the story
        return super().post(request, *args, **kwargs)