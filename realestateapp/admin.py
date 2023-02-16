from django.contrib import admin
from .models import PropertyImage, Property, PropertyAmenities, ContactAgentImage, Agent, CommentReply, CompanyDetails, About, BlogImage, Blog, Contact, Message, Service, Testimonial, TestimonialImage

# Register your models here.

admin.site.register(PropertyImage)
admin.site.register(Property)
admin.site.register(PropertyAmenities)
admin.site.register(ContactAgentImage)
admin.site.register(Agent)
admin.site.register(CommentReply)
admin.site.register(CompanyDetails)
admin.site.register(About)
admin.site.register(BlogImage)
admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(Message)
admin.site.register(Service)
admin.site.register(Testimonial)
admin.site.register(TestimonialImage)