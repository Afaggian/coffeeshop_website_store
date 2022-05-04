from django.forms import modelformset_factory, inlineformset_factory
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from coffeeshop.forms import UserForm, UserDetailsForm
from django.shortcuts import render, redirect
from django.contrib.auth import login, get_user_model

from .formsets import BaseOrderFormSet
from .utils import *

from coffeeshop.models import Coffee


def Home(request):
    template = loader.get_template('home.html')
    context = {}
    return HttpResponse(template.render(context, request))


def Thanks(request):
    template = loader.get_template('thanks.html')
    context = {}
    return HttpResponse(template.render(context, request))


def Signup(request):
    if request.method == "POST":
        # process the form data
        form = UserForm(request.POST)

        if form.is_valid():
            # validate the data
            # ...
            # redirect to a new URL
            user = form.save()
            login(request, user)  # django's login method
            return redirect('details')

    else:
        # create a blank form
        form = UserForm(initial={'email': '@gmail.com'})
    # option 1
    return render(request, 'signup.html', {'form': form})


def Details(request):
    if request.method == 'POST':
        form = UserDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('thanks')
    else:
        form = UserDetailsForm(initial={'username': request.user.username, 'email': request.user.email})

    return render(request, 'signup.html', {'form': form})


def PlaceOrder(request):
    # OrderFormSet = modelformset_factory(Coffee, fields=['name', 'size', 'quantity'], max_num=10,
    # extra=5, validate_max=True, can_delete=True)  # the syntax here is the following, first argument is the model the form will be created for "Coffee", followed by the fields we want to include, then the Key arguments
    OrderFormSet = inlineformset_factory(get_user_model(), Coffee, formset=BaseOrderFormSet, fields=['name', 'size', 'quantity'], max_num=5,
                                         extra=1, validate_max=True, can_delete=True)
    user = get_user_model().objects.get(username=request.user.username)
    if request.method == 'POST':
        order_formset = OrderFormSet(request.POST, instance=user)
        if order_formset.is_valid():
            order_formset.save()
            return redirect('home')
    else:
        order_formset = OrderFormSet(queryset=Coffee.objects.none(),
                                     instance=user)
    return render(request, 'order.html', {'formset': order_formset})
