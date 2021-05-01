from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import PreferenceForm
from django.contrib import messages

class CustomerForm(FormView):
    form_class = PreferenceForm
    template_name = 'preferences/main.html'




    # redirect to same home page
    def get_success_url(self):
        return self.request.path

    #checking if form is valid
    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.INFO, 'Send Successfully')
        return super().form_valid(form)
        
    def form_invlid(self, form):
        # if form is invalid return
        form.add_error(None, "Ooh...Something went wrong, check form well")
        return super().form_invalid(form)