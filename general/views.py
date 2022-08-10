from django.shortcuts import redirect, render
from .models import Testimony, Website, Enquiry
from Blog.models import blog_post
from .forms import EnquiryForm
# Create your views here.

def home_view(request):
    context = {
        'testimonies': Testimony.objects.all(),
        'websites': Website.objects.all(),
        'blog_posts': blog_post.objects.all()
    }
    

    if request.method == "POST" and request.POST['type'] == 'enquiry':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            Enquiry(name = form.cleaned_data['name'], email = form.cleaned_data['email'], subject = form.cleaned_data['subject'], message = form.cleaned_data['message']).save()
            return redirect('/')
    return render(request, 'index.html', context)

def flex_view(request, *args, **kwargs):
    context = {
        'website': Website.objects.get(abbreviation = kwargs['abbreviation'])
    }
    
    return render(request, 'portfolio-details.html', context)