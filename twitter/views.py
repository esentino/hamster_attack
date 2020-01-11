from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView

from twitter.models import Picture


class AddPicture(LoginRequiredMixin, CreateView):
    model = Picture
    success_url = '/'
    fields = ['path']

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        user = self.request.user
        self.object = form.save(commit=False)
        self.object.author = user
        self.object.save()
        return super().form_valid(form)

class PicturesView(ListView):
    model = Picture
    context_object_name = 'pictures'
    