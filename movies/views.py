from django.views.generic import ListView, DetailView
from .models import Movie
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

class MoviesView(ListView):
    model = Movie
    paginate_by = 10
    template_name = "movies/index.html"


class MovieView(DetailView):
    model = Movie
    template_name = 'movies/detail.html'



class NewMovie(CreateView):
    model = Movie
    template_name = 'movies/CreateMovies.html'
    fields = ["title", "filmed", "duration", "slug"]
    success_url = reverse_lazy('movies')

    

class UpdateMovie(UpdateView):
    model = Movie
    template_name = 'movies/UpdateMovie.html'
    fields = ["title", "filmed", "duration", "slug"]


    def get_success_url(self):
        return reverse('movie', kwargs={'pk': self.object.pk})
    
class DeleteMovie(DeleteView):
    model = Movie
    template_name = 'movies/DeleteMovie.html'
    success_url = reverse_lazy('movies')

