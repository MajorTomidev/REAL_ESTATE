from django.urls import path
from .views import SearchPage, PropertyView, PropertyDetailView, AboutView, AgentView, AgentDetailView, BlogView, BlogDetailView,  CommentReplyTest,  ContactViewTest, MessageViewTest, ContactPage, home_2

urlpatterns = [
    path('search/', SearchPage, name='searched'),
    path('property/', PropertyView, name='propertypage'),
    path('property/<int:pk>/', PropertyDetailView, name='propertydetailpage'),
    path('about/', AboutView, name='aboutpage'),
    path('agent/', AgentView, name='agentpage'),
    path('agent/<int:pk>/', AgentDetailView.as_view(), name='agentdetailpage'),
    path('blog/', BlogView, name='blogpage'),
    path('blog/<int:pk>/', BlogDetailView.as_view(), name='blogdetailpage'),
    path('contact/', ContactPage, name='contactpage'),
    path('testcomment/', CommentReplyTest, name='test_cmt'),
    path('testcontact/', ContactViewTest, name='test_cnt'),
    path('testmessage/', MessageViewTest, name='test_msg'),
    path('', home_2, name='home'),
    
]