from django.shortcuts import render, redirect
from .models import Contact, Profile, Upload_cv
from django.contrib import messages
from django.contrib.auth.models import User

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

# def profile_view(request):
#     if request.method == 'POST':
#         # extract info from the form
#         username = request.POST.get('username')
#         firstname = request.POST.get('firstname')
#         lastname = request.POST.get('lastname')
#         organization = request.POST.get('organization')
#         location = request.POST.get('location')
#         email = request.POST.get('email')
#         phone = request.POST.get('phone')
#         address = request.POST.get('address')
#         image = request.FILES.get('image')
#         if len(username)> 0 and len(firstname)> 0 and len(lastname)> 0 and len(organization)> 0 and len(location)> 0 and len(email)> 0 and len(phone)> 0 and len(address)> 0 and image:
#             # save the data to the database
#             profile = Profile(username=username, firstname=firstname, lastname=lastname, organization=organization, location=location, email=email, phone=phone, address=address, image=image)
#             profile.save()
#             messages.success(request, "Your profile has been created successfully!")
#             return redirect('profile')
#         else:
#             messages.error(request, "Please fill in all the fields!")
#     profiles = Profile.objects.all()
#     return render(request, 'profile.html', {'profiles': profiles})


def profile_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        organization = request.POST.get('organization')
        location = request.POST.get('location')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        image = request.FILES.get('image')

        if username and firstname and lastname and organization and location and email and phone and address and image:
            profile = Profile(
                username=username,
                firstname=firstname,
                lastname=lastname,
                organization=organization,
                location=location,
                email=email,
                phone=phone,
                address=address,
                image=image
            )
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
        name= request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if len(email)> 0 and len(password)> 0:
            # save the data to the database
            user = User.objects.create_user(username=name, email=email, password=password)
            user.first_name = name
            user.save()
            messages.success(request, "Your account has been created successfully!")
            return redirect('signup')
        else:
            messages.error(request, "Please fill in all the fields!")
    return render(request, 'signup.html')

def signin_view(request):
    if request.method == 'POST':
        # extract info from the form
        email = request.POST.get('email')
        password = request.POST.get('password')
        if len(email)> 0 and len(password)> 0:
            # save the data to the database
            user = User.objects.create_user(username=email, email=email, password=password)
            user.save()
            messages.success(request, "Your account has been created successfully!")
            return redirect('signin')
        else:
            messages.error(request, "Please fill in all the fields!")
    return render(request, 'signup.html')

def upload_view(request):
    if request.method == 'POST':
        # extract info from the form
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')
        if len(firstname)> 0 and len(email)> 0 and len(phone_number)> 0 and len(message)> 0:
            # save the data to the database
            upload_cv = Upload_cv(firstname=firstname, lastname=lastname ,email=email, phone_number=phone_number, message=message)
            upload_cv.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('upload_cv')
        else:
            messages.error(request, "Please fill in all the fields!")
    return render(request, 'upload_cv.html')
