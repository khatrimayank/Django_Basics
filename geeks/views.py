from django.shortcuts import render, redirect

from django.http import HttpResponse

from .forms import PostForm

from .models import PostModel

import datetime


def geeks_view(request):

	curr_time=datetime.datetime.now()

	html="current date and time is : {}".format(curr_time)

	return HttpResponse(html)

# Create your views here.
def home_view(request):
    if request.method == 'POST':
        form = GeeksModelForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Form submitted successfully!')
    else:
        form = GeeksModelForm()
    
    context = {'form': form}
    return render(request, 'home.html', context)


def home(request):

	# check if the request is post 
	if request.method =='POST': 

		# Pass the form data to the form class
		details = PostForm(request.POST)

		# In the 'form' class the clean function 
		# is defined, if all the data is correct 
		# as per the clean function, it returns true
		if details.is_valid(): 

			# Temporarily make an object to be add some
			# logic into the data if there is such a need
			# before writing to the database 
			post = details.save(commit = False)

			# Finally write the changes into database
			post.save() 

			# redirect it to some another page indicating data
			# was inserted successfully
			return HttpResponse("data submitted successfully")
			
		else:
		
			# Redirect back to the same page if the data
			# was invalid
			return render(request, "home.html", {'form':details}) 
	else:

		# If the request is a GET request then,
		# create an empty form object and 
		# render it into the page
		form = PostForm(None) 
		return render(request, 'home.html', {'form':form})

