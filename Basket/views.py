from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms



def update_todo_view(request, id):
    todo_id = get_object_or_404(models.Order, id=id)
    if request.method == 'POST':
        form = forms.OrderForm(request.POST, instance=todo_id)
        if form.is_valid():
            form.save()
            return HttpResponse('Задача успешно изменена')
    else:
        form = forms.OrderForm(instance=todo_id)
    return render(request, template_name='todo/update_todo.html',
                  context={
                      'form': form,
                      'todo_id': todo_id
                  })
