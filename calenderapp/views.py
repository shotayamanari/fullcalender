# redirectをインポート
from django.shortcuts import render,redirect
# Viewをインポート
from django.views import View

# Modelをインポート
from .models import Todo
# Formをインポート
from .forms import TodoForm

# ------------------------------------------------
class IndexView(View):
    def get(self, request, *args, **kwargs):

        context             = {}
        context["todos"]    = Todo.objects.order_by("deadline","dt")

        return render(request, "calenderapp/index.html", context)
    
    def post(self, request, *args, **kwargs):

        form = TodoForm(request.POST)

        if form.is_valid():
            form.save()
        
        return redirect("calenderapp:index")

index = IndexView.as_view()


class DoneView(View):
    def post(self, request, pk, *args, **kwargs):
        todo      = Todo.objects.filter(id=pk).first()
        todo.done = not todo.done
        todo.save()

        return redirect("calenderapp:index")

done = DoneView.as_view()