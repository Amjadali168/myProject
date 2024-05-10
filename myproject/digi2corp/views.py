from django.shortcuts import render, redirect
from .models import Contact, Profile, Upload_cv
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Upload_resume

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

# def upload_view(request):
#     if request.method == 'POST':
#         # extract info from the form
#         firstname = request.POST.get('firstname')
#         lastname = request.POST.get('lastname')
#         email = request.POST.get('email')
#         phone_number = request.POST.get('phone_number')
#         message = request.POST.get('message')
#         if len(firstname)> 0 and len(email)> 0 and len(phone_number)> 0 and len(message)> 0:
#             # save the data to the database
#             upload_cv = Upload_cv(firstname=firstname, lastname=lastname ,email=email, phone_number=phone_number, message=message)
#             upload_cv.save()
#             messages.success(request, "Your message has been sent successfully!")
#             return redirect('upload_cv')
#         else:
#             messages.error(request, "Please fill in all the fields!")
#     return render(request, 'upload_cv.html')


def upload_view(request):
    if request.method == 'POST':
        # extract info from the form
        firstname = request.POST.get('q3_name[first]')
        lastname = request.POST.get('q3_name[last]')
        email = request.POST.get('q4_email4')
        phone_number = request.POST.get('q14_phoneNumber14[full]')
        message = request.POST.get('q8_message')
        residency = request.POST.get('q6_residencyStatus')
        cv_file = request.FILES.get('q2_uploadYour[]')
        cover_letter_file = request.FILES.get('q7_uploadYour7[]')

        if firstname and email and phone_number and message:
            # save the data to the database
            upload_cv = Upload_cv(
                firstname=firstname,
                lastname=lastname,
                email=email,
                phone_number=phone_number,
                message=message,
                cv=cv_file,
                cover_letter=cover_letter_file,
                residency=residency
            )
            upload_cv.save()
            messages.success(request, "Your message has been sent successfully!")
            return redirect('upload_cv')
        else:
            messages.error(request, "Please fill in all the fields!")

    return render(request, 'upload_cv.html')

# def upload_resume(request):
#     return render(request, 'upload.html')
def upload_resume(request):
    if request.method == 'POST':
        # Get the form data
        email = request.POST.get('email')
        resume_file = request.FILES.get('resume_file')

        # Validate the form data
        if not email:
            messages.error(request, 'Email is required.')
            return redirect('upload_resume')  # Redirect back to the form
        if not resume_file:
            messages.error(request, 'Resume file is required.')
            return redirect('upload_resume')  # Redirect back to the form

        # Save the form data to the database
        upload_resume = Upload_resume(email=email, resume_file=resume_file)
        upload_resume.save()

        messages.success(request, 'Resume uploaded successfully.')
        return redirect('upload_resume')  # Redirect back to the form after successful upload

    return render(request, 'upload.html')
