from django.shortcuts import render
from users.forms import UserRegisterForm
from django.views import generic
from users.serializers import UsersSerializers
from rest_framework import generics
from users.models import CustomUser

# def register(request):
#     if request.method == "POST":
#         user_form = UserRegisterForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(user_form.cleaned_data["password"])
#             new_user.save()
#             return render(request, "registration/register_done.html", {"user": new_user})

#     else:
#         user_form = UserRegisterForm()
#     return render(request, "registration/register.html", {"form": user_form})        


class UsersListAPIView(generics.ListAPIView):
    serializer_class = UsersSerializers
    queryset = CustomUser.objects.all()

class RegisterView(generic.View):
    form_class = UserRegisterForm
    template_name = 'registration/register.html'

    def get(self, request):
        form = self.form_class
        return render(request, 'registration/register.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data["password"])
            new_user.save()
            return render(request, "registration/register_done.html", {"user": new_user})
            

        return render(request, 'registration/register.html', {'form': form})


