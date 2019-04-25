from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate
from signup.forms import SignUpForm
from django.views.generic import View
from signup.models import MyUser
# from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=email, password=raw_password)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


# class UserProfileView(View):
#     def get(self, request, user_id):

#         try:
#             user = MyUser.objects.get(id=user_id)
#         except:
#             user = None

#         context = {
#             "viewed_user": user
#         }

#         return render(request, "user_profile.html", context)
# @login_required
def profile(request, user_id):
    user = get_object_or_404(MyUser, pk=user_id)
    context = {
        'user': user,
    }
    return render(request, 'user_profile.html', context)
