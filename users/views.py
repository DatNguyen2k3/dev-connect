from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import CustomUserCreationFrom
from .forms import ProfileForm, SkillForm
from .models import Profile, Skill
from .utils import check_profile_is_owner_skill, search_profiles
from devsearch.utils import CustomPaginator
from .utils import login_web


# Create your views here.
def profiles_view(request):
    search_query, searched_profiles = search_profiles(request)
    searched_page, page_range = CustomPaginator.paginate_query_set(
        request, searched_profiles
    )

    context = {
        "search_query": search_query,
        "searched_page": searched_page,
        "page_range": page_range,
    }

    return render(request, "users/profiles.html", context=context)


def single_profile_view(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    context = {
        "profile": profile,
    }
    return render(request, "users/single-profile.html", context=context)


def login_view(request):
    page = "login"

    if request.user.is_authenticated:
        return redirect("users:profiles")

    if request.method == "POST" and login_web(request):
        return redirect("users:profiles")

    return render(request, "users/login-register.html", {"page": page})


def logout_view(request):
    logout(request)
    messages.info(request, "User was logged out")
    return redirect("users:login")


def register_view(request):
    page = "register"
    form = CustomUserCreationFrom()

    if request.method == "POST":
        form = CustomUserCreationFrom(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User was created successfully")
            login(request, user)
            return redirect("users:profiles")
        else:
            messages.error(request, "An error has occurred during registration")

    return render(request, "users/login-register.html", {"page": page, "form": form})


@login_required(login_url="users:login")
def account_view(request):
    profile = request.user.profile
    context = {"profile": profile}
    return render(request, "users/account.html", context=context)


@login_required(login_url="users:login")
def edit_profile_view(request):
    profile = Profile.objects.get(user=request.user)
    profile_form = ProfileForm(instance=profile)

    if request.method == "POST":
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect("users:account")
        else:
            messages.error(request, "Profile is not valid!")

    return render(request, "users/profile-form.html", {"form": profile_form})


@login_required(login_url="users:login")
def add_skill_view(request):
    skill_form = SkillForm()
    if request.method == "POST":
        skill_form = SkillForm(request.POST)
        if skill_form.is_valid():
            skill = skill_form.save(commit=False)
            skill.owner = request.user.profile
            skill.save()
        else:
            messages.error(request, "Skill is not valid!")

        return redirect("users:account")

    return render(request, "users/skill-form.html", {"form": skill_form})


@login_required(login_url="users:login")
def edit_skill_view(request, skill_id):
    check_profile_is_owner_skill(request.user.profile, skill_id)
    skill = Skill.objects.get(id=skill_id)
    skill_form = SkillForm(instance=skill)

    if request.method == "POST":
        skill_form = SkillForm(request.POST, instance=skill)
        if skill_form.is_valid:
            skill_form.save()
            return redirect("users:account")

    return render(request, "users/skill-form.html", {"form": skill_form})


@login_required(login_url="users:login")
def delete_skill_view(request, skill_id):
    check_profile_is_owner_skill(request.user.profile, skill_id)
    skill = Skill.objects.get(id=skill_id)

    if request.method == "POST":
        skill.delete()
        return redirect("users:account")

    return render(request, "users/delete-skill.html", {"skill": skill})


