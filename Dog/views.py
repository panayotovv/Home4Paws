from django.conf import settings
from django.template.context_processors import request
from django.views.generic import DetailView, TemplateView
from django.views.generic import ListView
from django.contrib.auth import login
from django.shortcuts import redirect, render
from User.forms import SignUpForm, LoginForm, AdoptionForm
from .models import Dog, Adoption


class IndexView(ListView):
    template_name = "index.html"
    model = Dog

    def get_queryset(self):
        return Dog.objects.all().order_by("name")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["login_form"] = LoginForm()
        context["signup_form"] = SignUpForm()

        return context

    def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()

        if "login" in request.POST:
            login_form = LoginForm(request, data=request.POST)

            if login_form.is_valid():
                user = login_form.get_user()
                login(request, user)
                return redirect("index")

            context = self.get_context_data()
            context["login_form"] = login_form
            context["show_login"] = True
            return self.render_to_response(context)

        elif "signup" in request.POST:
            signup_form = SignUpForm(request.POST, request.FILES)

            if signup_form.is_valid():
                user = signup_form.save(commit=False)
                user.save()
                signup_form.save_m2m()
                login(request, user)
                return redirect("index")

            context = self.get_context_data()
            context["signup_form"] = signup_form
            context["show_signup"] = True
            return self.render_to_response(context)

        return redirect("index")

class DogDetailView(DetailView):
    template_name = 'detail.html'
    model = Dog

    slug_field = 'name'
    slug_url_kwarg = 'name'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dog = self.object
        context["vaccinated_text"] = "Yes" if dog.health_status.filter(name="Vaccinated").exists() else "No"
        context["adoption_form"] = AdoptionForm()
        context["show_success"] = self.request.GET.get("success") == "true"
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        adoption_form = AdoptionForm(request.POST)

        if adoption_form.is_valid():
            dog = self.object
            Adoption.objects.create(
                dog=dog,
                owner=request.user,
                **adoption_form.cleaned_data
            )
            dog.owner = request.user
            dog.save()
            return redirect(f"/dog/{dog.name}/?success=true")
        else:
            context = self.get_context_data(adoption_form=adoption_form, show_success=True)
            return self.render_to_response(context)



def donate_view(request):
    return render(request, "donate.html", {
        "stripe_public_key": settings.STRIPE_PUBLIC_KEY
    })




