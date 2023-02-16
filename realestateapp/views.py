from django.shortcuts import render, redirect
from .models import Property, About, Agent, CommentReply, Contact, Message, Blog, Service
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .forms import ContactForm, MessageForm, CommentReplyForm

# Create your views here.

# HOME VIEW ------------------------------------------------------
def HomePage(request):
    property = Property.objects.all()
    return render(request, 'realestateapp/home/home.html', {"property": property}, {'services': services})

def home_2(request):
    property = Property.objects.all()
    return render(request, 'realestateapp/home/home_2.html', {"property": property})

# SEARCH VIEW ----------------------------------------------------

def SearchPage(request):
    if request.method == 'POST':
       searched = request.POST['searched']
       properties = Property.objects.filter(property_name__contains=searched)


       return render (request, 'realestateapp/search/search.html',{'searched': searched, 'properties': properties})
    else:
        return render (request, 'realestateapp/search/search.html',{})


# PROPERTY VIEW ----------------------------------------------------

class PropertyView(ListView):
    model = Property
    template_name = 'realestateapp/property/property-grid.html'
    context_object_name = 'property'


class PropertyDetailView(DetailView):
    model = Property
    template_name = 'realestateapp/property/property-single.html'
    context_object_name = 'property'



# ABOUT VIEW ---------------------------------------------------------

class AboutView(ListView):
    model = About
    template_name= 'realestateapp/about/about.html'
    context_object_name = 'about'



# AGENT VIEW -----------------------------------------------------------

class AgentView(ListView):
    model = Agent
    template_name= 'realestateapp/agent/agents-grid.html'
    context_object_name = 'agent'

class AgentDetailView(DetailView):
    model = Agent
    template_name= 'realestateapp/agent/agent-single.html'
    context_object_name = 'agent'


# BLOG VIEW ---------------------------------------------------------------------

class BlogView(ListView):
    model = Blog
    template_name= 'realestateapp/blog/blog-grid.html'
    context_object_name = 'blog'

class BlogDetailView(DetailView):
    model = Blog
    template_name= 'realestateapp/blog/blog-single.html'
    context_object_name = 'blog'


# COMMENT_REPLY_FORM VIEW --------------------------------------------------------

def CommentReplyView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        website = request.POST.get('website')
        comment = request.POST.get('comment')
        

        commentreply = CommentReply.objects.create(name=name, email=email, website=website, comment=comment)

        if commentreply.is_valid():
            commentreply.save()
            messages.success(request, 'Your comment has been sent successfully')
            return redirect('/')
        
    else: 

        return render(request, 'realestateapp/home/home.html')
    


def CommentReplyTest(request):
    if request.method == 'POST':
        form = CommentReplyForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CommentReplyForm()
    context = {'form': form}
    return render(request, 'realestateapp/test/test.html', context)


# CONTACT_FORM VIEW----------------------------------------------------------------

def ContactPage(request):
    return render(request, 'realestateapp/contact/contact.html')

def ContactView(request):
    if request.method == 'POST':
        contact_name = request.POST.get('name')
        contact_email = request.POST.get('email')
        contact_subject = request.POST.get('subject')
        contact_message = request.POST.get('comment')
        

        contact_company = Contact.objects.create(contact_name=contact_name, contact_email=contact_email, contact_subject=contact_subject, contact_message=contact_message)

        if contact_company.is_valid():
            contact_company.save()
            messages.success(request, 'Your message has been sent to one of our agents, They will reach out to you shortly.')
            return redirect('/')
        
    else: 

        return render(request, 'realestateapp/home/home.html')
    


def ContactViewTest(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'realestateapp/test/test.html', context)



# MESSAGE_FORM VIEW -------------------------------------------------------------------
def MessageView(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        

        commentreply = Message.objects.create(name=name, email=email, comment=comment)

        if commentreply.is_valid():
            commentreply.save()
            messages.success(request, 'Your message has been sent successfully')
            return redirect('/')
        
    else: 

        return render(request, 'realestateapp/home/home.html')
    


def MessageViewTest(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = MessageForm()
    context = {'form': form}
    return render(request, 'realestateapp/test/test.html', context)

# SERVICE VIEW -------------------------------------------------------------------

class Service(ListView):
    model = Service
    template_name = 'service.html'
    context_object_name = 'services'