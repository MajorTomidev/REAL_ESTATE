from django import forms
from .models import CommentReply, Contact, Message

class CommentReplyForm(forms.ModelForm):
    class Meta:
        model = CommentReply
        fields = '__all__'

class ContactForm(forms.ModelForm):
    class Meta:
        model= Contact
        fields =['contact_name', 'contact_email', 'contact_subject', 'contact_message']

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
