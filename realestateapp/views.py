from django.shortcuts import render, redirect
from .models import Property, About, Agent, CommentReply, Contact, Message, Blog, Service, Testimonial, CompanyDetails
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .forms import ContactForm, MessageForm, CommentReplyForm
from django.urls import reverse

# Create your views here.

# HOME VIEW ------------------------------------------------------
# def HomePage(request):
#     property = Property.objects.all()
#     services = Service.objects.all()
#     return render(request, 'realestateapp/home/home.html', {"property": property, 'services': services})

def home_2(request):
    service = Service.objects.all()
    property = Property.objects.all()
    agents = Agent.objects.all()
    blogs = Blog.objects.all()
    testimonial = Testimonial.objects.all()
    companydetail = CompanyDetails.objects.all()
    return render(request, 'realestateapp/home/home_2.html', {"property": property, 'service': service, 'agents': agents, 'blogs': blogs, 'testimonial': testimonial, 'companydetail': companydetail})

# SEARCH VIEW ----------------------------------------------------

def SearchPage(request):
    if request.method == 'POST':
       searched = request.POST['searched']
       properties = Property.objects.filter(property_name__contains=searched)


       return render (request, 'realestateapp/search/search.html',{'searched': searched, 'properties': properties})
    else:
        return render (request, 'realestateapp/search/search.html',{})


# PROPERTY VIEW ----------------------------------------------------

# class PropertyView(ListView):
#     model = Property
#     template_name = 'realestateapp/property/property-grid.html'
#     context_object_name = 'property'


def PropertyView(request):
    property = Property.objects.all()
    companydetail = CompanyDetails.objects.all()
    return render(request, 'realestateapp/property/property-grid.html', {"property": property, 'companydetail': companydetail})



# class PropertyDetailView(DetailView):
#     model = Property
#     template_name = 'realestateapp/property/property-single.html'
#     context_object_name = 'property'

# def PropertyDetailView(request):
#     property = Property.objects.all()
    # agents = Agent.objects.all()
#     companydetail = CompanyDetails.objects.all()
#     return render(request, 'realestateapp/property/property-single.html', {"property": property, 'agents': agents, 'companydetail': companydetail})



# ABOUT VIEW ---------------------------------------------------------

def AboutView(request):
    about = About.objects.all()
    agents = Agent.objects.all()
    companydetail = CompanyDetails.objects.all()
    return render(request, 'realestateapp/about/about.html', {"about": about,  'agents': agents, 'companydetail': companydetail})


# AGENT VIEW -----------------------------------------------------------



def AgentView(request):
    agents = Agent.objects.all()
    companydetail = CompanyDetails.objects.all()
    return render(request, 'realestateapp/agent/agents-grid.html', {'agents': agents, 'companydetail': companydetail})


class AgentDetailView(DetailView):
    model = Agent
    template_name= 'realestateapp/agent/agent-single.html'
    context_object_name = 'agent'


# BLOG VIEW ---------------------------------------------------------------------

# class BlogView(ListView):
#     model = Blog
#     template_name= 'realestateapp/blog/blog-grid.html'
#     context_object_name = 'blog'

def BlogView(request):
    blog = Blog.objects.all()
    companydetail = CompanyDetails.objects.all()
    return render(request, 'realestateapp/blog/blog-grid.html', {  'blog': blog, 'companydetail': companydetail})



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
        commentreply.save()
        messages.success(request, 'Your comment has been sent successfully')
        return redirect('/')
        
    else: 

        return render(request, 'realestateapp/home/home.html')
    


def CommentReplyTest(request):
    if request.method == 'POST':
        form = CommentReplyForm(request.POST)
        
        form.save()
    else:
        form = CommentReplyForm()
    context = {'form': form}
    return render(request, 'realestateapp/test/test.html', context)


# CONTACT_FORM VIEW----------------------------------------------------------------

def ContactPage(request):
    contact = Contact.objects.all()
    companydetail = CompanyDetails.objects.all()
    context = {"contact": contact, 'companydetail': companydetail }

    if request.method == 'POST':
        contact_name = request.POST.get('name')
        contact_email = request.POST.get('email')
        contact_subject = request.POST.get('subject')
        contact_message = request.POST.get('comment')
        

        contact_company = Contact.objects.create(contact_name=contact_name, contact_email=contact_email, contact_subject=contact_subject, contact_message=contact_message)

        
        contact_company.save()
        messages.success(request, 'Your message has been sent to one of our agents, They will reach out to you shortly.')
        return redirect('contactpage')
        
    else: 

        return render(request, 'realestateapp/contact/contact.html', context)
    


def ContactViewTest(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        form.save()
        messages.success(request, 'Your message has been sent to one of our agents, They will reach out to you shortly.')
    else:
        form = ContactForm()
    context = {'form': form}
    return render(request, 'realestateapp/test/test.html', context)



# MESSAGE_FORM VIEW -------------------------------------------------------------------

def PropertyDetailView(request, pk):
    property = Property.objects.get(id=pk)
    agents = Agent.objects.all()[0]
    companydetail = CompanyDetails.objects.all()
    context = {"property": property, 'companydetail': companydetail, 'agents': agents }

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        

        commentreply = Message.objects.create(name=name, email=email, comment=comment)

        
        commentreply.save()
        messages.success(request, 'Your message has been sent successfully')
        return redirect(reverse('propertydetailpage', kwargs={'pk':request.pk}))
        
    else: 

        return render(request, 'realestateapp/property/property-single.html', context)
    
#  def PropertyDetailView(request):
#     property = Property.objects.all()
    # agents = Agent.objects.all()
#     companydetail = CompanyDetails.objects.all()
#     return render(request, 'realestateapp/property/property-single.html', {"property": property, 'agents': agents, 'companydetail': companydetail})




def MessageViewTest(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        
        form.save()
    else:
        form = MessageForm()
    context = {'form': form}
    return render(request, 'realestateapp/test/test.html', context)

# SERVICE VIEW -------------------------------------------------------------------

