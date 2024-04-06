from django.shortcuts import render, redirect
from .models import Contact, Profile, Signup
from django.contrib import messages

# Create your views here.
def contact_view(request):
    if request.method == 'POST':
        # extract info from the form
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        if len(name)> 0 and len(email)> 0 and len(subject)> 0 and len(message)> 0:
            # save the data to the database
            contact = Contact(name=name, email=email, subject=subject, message=message)
            contact.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
        else:
            messages.error(request, "Please fill in all the fields!")
    return render(request, 'contact.html')

def profile_view(request):
    if request.method == 'POST':
        # extract info from the form
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        organization = request.POST.get('organization')
        location = request.POST.get('location')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        image = request.FILES.get('image')
        if len(username)> 0 and len(firstname)> 0 and len(lastname)> 0 and len(organization)> 0 and len(location)> 0 and len(email)> 0 and len(phone)> 0 and len(address)> 0 and image:
            # save the data to the database
            profile = Profile(username=username, firstname=firstname, lastname=lastname, organization=organization, location=location, email=email, phone=phone, address=address, image=image)
            profile.save()
            messages.success(request, "Your profile has been created successfully!")
            return redirect('profile')
        else:
            messages.error(request, "Please fill in all the fields!")
    profiles = Profile.objects.all()
    return render(request, 'profile.html', {'profiles': profiles})


def signup_view(request):
    if request.method == 'POST':
        # extract info from the form
        email = request.POST.get('email')
        password = request.POST.get('password')
        if len(email)> 0 and len(password)> 0:
            # save the data to the database
            signup = Signup(email=email, password=password)
            signup.save()
            messages.success(request, "Your account has been created successfully!")
            return redirect('signup')
        else:
            messages.error(request, "Please fill in all the fields!")
    return render(request, 'signup.html')
