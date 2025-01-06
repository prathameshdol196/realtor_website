from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Listing
from django.core.paginator import Paginator
from django.conf import settings


#  Login ad Logout
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

#  Registration
from django.contrib.auth.forms import UserCreationForm


def home(request):
    query = request.GET.get('q', '')
    if query:
        listings = Listing.objects.filter(title__icontains=query)
    else:
        listings = Listing.objects.all()

    category = request.GET.get('category')
    if category:
        listings = Listing.objects.filter(category=category)
    else:
        listings = Listing.objects.all()
    
    paginator = Paginator(listings, 6)  # Show 6 listings per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(settings.EMAIL_HOST_USER)
    print(settings.EMAIL_HOST_PASSWORD)
    print(settings.DEFAULT_CONTACT_EMAIL)
    return render(request, 'listings/home.html', {'page_obj': page_obj, 'listings': listings, 'query': query})


def detail(request, pk):
    #listing = get_object_or_404(Listing, pk=pk)
    #return render(request, 'listings/detail.html', {'listing': listing})
    listing = get_object_or_404(Listing, pk=pk)
    return render(request, 'listings/detail.html', {'listing': listing})


#  Form requests
from django.core.mail import send_mail
from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import BadHeaderError
from django.contrib import messages
from django.conf import settings


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            full_message = f"Email : \n {email} \n\n Message : \n {message}"
            try:
                send_mail(
                    subject=f"New message from {name}",
                    message=full_message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.DEFAULT_CONTACT_EMAIL],  # Replace with your email
                )
                messages.success(request, "Your message was sent successfully!")
                print(f"name = {name}")
                print(f"email = {email}")
                print(f"message = {message}")
                print(f"from email = {settings.EMAIL_HOST_USER}")
                print(f"reciepent = {settings.DEFAULT_CONTACT_EMAIL}")

                return redirect('contact')
            

            except BadHeaderError:
                messages.error(request, "Invalis Header found.")
    else:
        form = ContactForm()

    return render(request, 'listings/contact.html', {'form': form})


#  Search 
from django.db.models import Q

def search(request):
    query = request.GET.get('q', '')
    listings = []
    if query:
        listings = Listing.objects.filter(
            Q(title__icontains=query) |
            Q(category__icontains=query) |
            Q(price__icontains=query)
        )
    return render(request, 'listings/search.html', {'listings': listings, 'query': query})


def about(request):
    return render(request, "listings/about.html")


def investment(request):
    listings = Listing.objects.all()
    return render(request, 'listings/investment.html',{'listings': listings})

