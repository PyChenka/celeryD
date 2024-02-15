from django.views.generic import CreateView

from main.forms import ContactForm
from main.models import Contact
from main.service import send


class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'
    template_name = 'contact.html'

    def form_valid(self, form):
        form.save()
        send(form.instance.email)
        return super().form_valid(form)