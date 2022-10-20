from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.cadastros.forms import *
from .models import *
from django.forms import inlineformset_factory


################ LIST ################

def list_formulario(request):
    formulario = Formulario.objects.all()
    context = {'formulario': formulario}
    return render(request, 'cadastros/list/list_formulario.html', context)
    

################ CREATE ################

def create_formulario(request):
    formulario = Formulario()
    inline_formset = inlineformset_factory(Formulario, AcordoParcelamento, form=AcordoParcelamentoForm, extra=0, can_delete=False, min_num=1, validate_min=True)
    
    if request.method == 'POST': 
        form = Ente_Formulario(request.POST or None, instance=formulario, prefix='main')
        formset = inline_formset(request.POST or None, instance=formulario, prefix='id')
        if form.is_valid() and formset.is_valid():
            form.save()
            formset.save()
            return redirect('list_formulario')
    else:
        form = Ente_Formulario(request.POST or None, instance=formulario, prefix='main')
        formset = inline_formset(request.POST or None, instance=formulario, prefix='id')
    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'cadastros/create/create_formulario.html', context)