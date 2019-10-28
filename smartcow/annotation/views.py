import json
import os
import random
import csv
from django.conf import settings
from django.contrib.auth import login, authenticate
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from annotation.forms import SignUpForm, PhotoForm, AnnotateForm
from django.views import View
from annotation.models import Photo, Profile, Annotate


def annotate(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    photo = Photo.objects.get(id=id)
    return render(request, "annotation/annotate.html", {'photo': photo})


def check_my_annotate_n_csv_download(request, id):
    if not request.user.is_authenticated:
        return redirect('login')
    photo = Photo.objects.get(id=id)
    annotate = Annotate.objects.get(image=photo.id)
    annotate_dict = {
        "id": annotate.id,
        "coordinates": annotate.coordinates.replace("label", "text"),
        "image": annotate.image
    }
    return render(request, "annotation/check-my-annotate.html", {'photo': photo, 'annotate': annotate_dict})


def downloadcsv(request, id, coordinates=None):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="smart-cow-annotations.csv"'
    annotate = Annotate.objects.get(id=id)
    photo = Photo.objects.get(id=annotate.image)
    coordinates = annotate.coordinates[1:-1]
    writer = csv.writer(response)
    res_dict_co = coordinates.replace("\"", "\'")
    dict = eval(res_dict_co)
    for coordinate in dict:
        writer.writerow([photo.file, coordinate['left'], coordinate['top'], coordinate['width'], coordinate['height']])
    return response


def myannonate(request):
    if not request.user.is_authenticated:
        return redirect('login')
    project_name_obj = Profile.objects.get(user_id=request.user.id)
    photos_list = Photo.objects.filter(project=project_name_obj.id, istagged=True)
    return render(request, "annotation/myannotate.html", {'photos': photos_list})


class UploadView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        project_name_obj = Profile.objects.get(user_id=request.user.id)
        photos_list = Photo.objects.filter(project=project_name_obj.id, istagged=False)
        return render(self.request, 'annotation/upload.html', {'photos': photos_list})

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        form = PhotoForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            photo = form.save()
            data = {'is_valid': True, 'name': photo.file.name, 'url': photo.file.url}
        else:
            data = {'is_valid': False}
        return JsonResponse(data)


def signup(request):
    if request.user.is_authenticated:
        return redirect('login')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal

            # Creating user specific directory
            project_dir_name = form.cleaned_data.get('project_name')
            check_folder = os.path.isdir(settings.MEDIA_ROOT + '/' + project_dir_name)
            dir_name = project_dir_name
            if not check_folder:
                os.makedirs(settings.MEDIA_ROOT + '/' + project_dir_name, 0o777)
            else:
                dir_name = dir_name + str(random.randint(1, 10000000))
                os.makedirs(settings.MEDIA_ROOT + '/' + dir_name, 0o777)

            user.profile.project_name = dir_name
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def confirm(request, id):
    image = Photo.objects.get(id=id)
    if request.method == "POST":
        form = AnnotateForm(request.POST)
        if form.is_valid():
            ann_obj = Annotate(coordinates=request.POST.get('annotation'), image=image.id)
            ann_obj.save()
            image.istagged = True
            image.save()
            return redirect('/myannonate')
    else:
        return redirect('/upload')
