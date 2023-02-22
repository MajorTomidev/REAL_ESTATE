from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

# Create your models here.

# PROPERTY MODEL -----------------------------------------------------------------------------

PROPERTY_CHOICES = (
    ('2 Bedroom Apartment', '2 Bedroom Apartment'),
    ('3 Bedroom Apartment', '3 Bedroom Apartment'),
    ('4 Bedroom Apartment', '4 Bedroom Apartment'),
    ('Duplex', 'Duplex'),
    ('Terrace', 'Terrace'),
    ('Penthouse ', 'Penthouse'),
)

STATUS_CHOICES = (
    ('Sale', 'Sale'),
    ('Rent', 'Rent'),
) 

class PropertyAmenities(models.Model):
    amenities = models.CharField(max_length=200)

    def __str__(self):
        return self.amenities
    
    class Meta:
        verbose_name_plural = 'Property amenities'



class PropertyImage(models.Model):
    image = models.ImageField(default='property.jpg', upload_to='album_pictures', null=True, blank=True)

class Property(models.Model):
    property_name = models.CharField(max_length=100)
    property_location = models.TextField()
    property_zipcode = models.PositiveIntegerField(null=True, blank=True)
    house_number = models.PositiveIntegerField(null=True, blank=True)
    property_description = models.TextField(null=True, blank=True)
    property_image = models.ManyToManyField(PropertyImage)
    video = models.FileField(upload_to='videos_uploaded', null=True, blank=True, validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    property_price =models.FloatField()
    property_type = models.CharField(choices= PROPERTY_CHOICES, max_length=100)
    property_status = models.CharField(choices=STATUS_CHOICES, max_length=100)
    property_squaremeter = models.PositiveIntegerField()
    beds = models.PositiveIntegerField()
    baths = models.PositiveIntegerField()
    garage = models.PositiveIntegerField()
    floorplan_image = models.ImageField(upload_to='images_uploaded', null=True, blank=True)
    amenities= models.ManyToManyField(PropertyAmenities)

    def __str__(self):
        return self.property_name
    
    class Meta:
        verbose_name_plural = 'Properties'


# CONTACT AGENT MODEL ----------------------------------------------------------------------

class ContactAgentImage(models.Model):
    image = models.ImageField(default='contact.jpg', upload_to='album_pictures', null=True, blank=True)

    def __str__(self):
        return self.image.url

class Agent(models.Model):
    agent_image = models.ManyToManyField(ContactAgentImage)
    agent_name = models.CharField(max_length=100)
    agent_description = models.TextField()
    agent_mobilenumber = models.PositiveBigIntegerField()
    agent_email= models.EmailField()
    
    def __str__(self):
        return self.agent_name
    

# MESSAGE MODEL ----------------------------------------------------------------------------

class CommentReply(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.URLField(max_length=250)
    comment = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Comment replies'

    

# COMPANY DETAILS MODEL ----------------------------------------------------------------

class CompanyDetails(models.Model):
    company_description = models.TextField()
    company_phonenumber = models.PositiveBigIntegerField()
    company_email = models.EmailField()
    company_location = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.company_email
    
    class Meta:
        verbose_name_plural = 'Company details'


# ABOUT MODEL --------------------------------------------------------------------------

class About(models.Model):
    about_headline = models.CharField(max_length=100)
    about_description = models.TextField()

    def __str__(self):
        return self.about_headline
    
    class Meta:
        verbose_name_plural = 'About'


# BLOG MODEL ---------------------------------------------------------------------------

class BlogImage(models.Model):
    image = models.ImageField(default='blog.jpg', upload_to='album_pictures', null=True, blank=True)  

class Blog(models.Model):
    blog_headline = models.CharField(max_length=100)
    blog_image = models.ManyToManyField(BlogImage, null=True, blank=True)
    blog_content = models.TextField()
    date_published= models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    blog_category = models.CharField(max_length=100)

    def __str__(self):
        return self.blog_headline

# CONTACT MODEL ---------------------------------------------------------------------------

class Contact(models.Model):
    contact_name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    contact_subject = models.CharField(max_length=100)
    contact_message = models.TextField()

    def __str__(self):
        return self.contact_name
    
# MESSAGE MODEL ----------------------------------------------------------------------------

class Message(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()

    def __str__(self):
        return self.name


# SERVICE MODEL -----------------------------------------------------------------------------

class Service(models.Model):
    service_headline = models.CharField(max_length=100)
    service_description = models.TextField()

    def __str__(self):
        return self.service_headline


# TESTIMONIALS MODEL -------------------------------------------------------------------------

class TestimonialImage(models.Model):
    image = models.ImageField(default='testimonials.jpg', upload_to='album_pictures', null=True, blank=True)

class Testimonial(models.Model):
    image = models.ManyToManyField(TestimonialImage)
    name = models.CharField(max_length=100)
    testimonal_description =models.TextField()
    

    def __str__(self):
        return self.name


# ----------------------------------------------------------------------------------------------



