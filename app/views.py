from django.shortcuts import render,get_object_or_404,HttpResponseRedirect,redirect
from .models import Add
from .forms import CrudForm
# Create your views here.


def list(request,context={}):
    context['dataset'] = Add.objects.all()
    form = CrudForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context['form']=form
    return render(request,'list.html',context)


def update(request,id,context={}):
    obj = get_object_or_404(Add, id = id)
    form = CrudForm(request.POST or None, instance = obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/")
    context["form"] = form
    return render(request,'update.html',context)

def delete(request, id,context={}):
    obj = get_object_or_404(Add, id = id)
    if request.method =="POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return redirect("/")
    return render(request,'delete.html',context)

