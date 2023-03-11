from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ShortCutsCreateForm


@login_required
def short_create(request):
    if request.method == 'POST':
        # form is sent
        form = ShortCutsCreateForm
        if form.is_valid():
            cd = form.cleaned_data
            new_image = form.save(commit=False)
            # assign current user to the item
            new_image.user = request.user
            new_image.save()
            messages.success(request,
                             'Shortcut added successfully')
            # redirect to new created item detail view
            return redirect(new_image.get_absolute_url())
    else:
        # build form with data provided by the bookmarklet via GET
        form = ShortCutsCreateForm(data=request.GET)
    return render(request,
                  'shortcuts/shortcut/create.html',
                  {'section': 'shortcuts',
                   'form': form})
