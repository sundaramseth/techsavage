from django.views import generic
from django.views.generic import ListView
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render, redirect
from django.db.models import Q
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from .models import Subscriber
from .form import SubscriberForm
from .form import ContactForm
import random
from django.core.mail import send_mail, BadHeaderError
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail




class PostList(generic.ListView):
     model = Post
     context_object_name = 'featurepost'
     template_name = 'bloggy.html'
     paginate_by = 10
     queryset = Post.objects.filter(status=1).order_by('-created_on')

     def get_context_data(self, **kwargs):
         context = super(PostList, self).get_context_data(**kwargs)
         context['Latestpost'] = Post.objects.filter(status=1).order_by('-created_on')
         context['featuredpost'] = Post.objects.filter(tag__contains='featuredpost')
         return context



def post_detail(request, slug):
    template_name = 'post_details.html'
    post = get_object_or_404(Post, slug=slug)
    return render(request, template_name, {'post': post})




class AngularList(generic.ListView):
     model = Post
     template_name = 'angular.html'
     paginate_by = 9
     queryset = Post.objects.filter(title__contains='Angular')

     def __str__(self):
        return self.title


class ReactList(generic.ListView):
     model = Post
     template_name = 'react.html'
     paginate_by = 9
     queryset = Post.objects.filter(title__contains='react')

     def __str__(self):
        return self.title



class DjangoList(generic.ListView):
     model = Post
     template_name = 'django.html'
     paginate_by = 9
     queryset = Post.objects.filter(title__contains='Django')

     def __str__(self):
        return self.title


class NodeList(generic.ListView):
     model = Post
     template_name = 'node.html'
     paginate_by = 9
     queryset = Post.objects.filter(title__contains='node')

     def __str__(self):
        return self.title


class ProgramBlog(generic.ListView):
     model = Post
     template_name = 'program.html'
     paginate_by = 5
     queryset = Post.objects.filter(title__contains='Program')

     def __str__(self):
        return self.title

class PythonBlog(generic.ListView):
     model = Post
     template_name = 'python.html'
     paginate_by = 5
     queryset = Post.objects.filter(title__contains='Python')

     def __str__(self):
        return self.title

class JavaBlog(generic.ListView):
     model = Post
     template_name = 'javascript.html'
     paginate_by = 5
     queryset = Post.objects.filter(title__contains='Java Scripts')

     def __str__(self):
        return self.title

class DataScience(generic.ListView):
     model = Post
     template_name = 'datascience.html'
     paginate_by = 5
     queryset = Post.objects.filter(title__contains='DATA SCIENCE')

     def __str__(self):
        return self.title

class SearchResultsView(ListView):
    model = Post
    template_name = 'search_result.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
            )

        return object_list

class BasicProgram(generic.ListView):
     model = Post
     template_name = 'basicprogram.html'
     paginate_by = 5
     queryset = Post.objects.filter(tag__contains='pbasic')

     def __str__(self):
        return self.title

class ListofProgram(generic.ListView):
     model = Post
     template_name = 'listofprogram.html'
     paginate_by = 5
     queryset = Post.objects.filter(tag__contains='lpall')

     def __str__(self):
         return self.title

class PhysicsLecture(generic.ListView):
     model = Post
     template_name = 'physicslecture.html'
     paginate_by = 10
     queryset = Post.objects.filter(tag__contains='Pshivam')

     def __str__(self):
        return self.title




def science(request):
    return render(request, 'science.html')

def chemistry(request):
    return render(request, 'chemistry.html')

def gate(request):
    return render(request, 'gate.html')

def sciencesyllabus(request):
    return render(request, 'science-syllabus.html')

def upsc(request):
    return render(request, 'upsc.html')

def library(request):
    return render(request, 'library.html')

def tutorial(request):
    return render(request, 'tutorial.html')



def about(request):
    return render(request, 'about.html')


def disclaimer(request):
    return render(request, 'disclaimer.html')

def privacy(request):
    return render(request, 'privacy.html')


# Helper Functions
def random_digits():
    return "%0.12d" % random.randint(0, 999999999999)



@csrf_exempt
def new(request):
    if request.method == 'POST':
        sub = Subscriber(email=request.POST['email'], conf_num=random_digits())
        sub.save()
        message = Mail(
            from_email=settings.FROM_EMAIL,
            to_emails=sub.email,
            subject='Newsletter Confirmation',
            html_content='Thank you for signing up for our weekly newsletter! \
                Please complete the process by \
                <a href="{}/confirm/?email={}&conf_num={}"> clicking here to \
                confirm your registration</a>.'.format(request.build_absolute_uri('/confirm/'),
                                                    sub.email,
                                                    sub.conf_num))
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        return render(request, 'subscribe.html', {'email': sub.email, 'action': 'added', 'form': SubscriberForm()})
    else:
        return render(request, 'subscribe.html', {'form': SubscriberForm()})

def confirm(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.confirmed = True
        sub.save()
        return render(request, 'confirm.html', {'email': sub.email, 'action': 'confirmed'})
    else:
        return render(request, 'confirm.html', {'email': sub.email, 'action': 'denied'})

def delete(request):
    sub = Subscriber.objects.get(email=request.GET['email'])
    if sub.conf_num == request.GET['conf_num']:
        sub.delete()
        return render(request, 'subscribe.html', {'email': sub.email, 'action': 'unsubscribed'})
    else:
        return render(request, 'subscribe.html', {'email': sub.email, 'action': 'denied'})


def emailView(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
                subject= form.cleaned_data["subject"]
                message = form.cleaned_data["message"]
                from_email=form.cleaned_data["from_email"]
                recipent = ['sundaramseth.ucer@gmail.com']
                try:
                    send_mail(subject,message,from_email,recipent, fail_silently=True)
                except BadHeaderError:
                    return HttpResponse('BadHeaderError')
                return HttpResponse('Your email is successfully send..')
    return render(request, "contact.html", {'form': form})
