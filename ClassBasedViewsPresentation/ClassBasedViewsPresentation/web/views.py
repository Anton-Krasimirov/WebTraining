from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

# pure python func
# - called with django request object
# - returns django response
from django101.web.models import Todo


def index(request):
    context = {
        'title': 'Function-based view',
    }

    return render(request, 'index.html', context)


class IndexView(views.View):
    def get(self, request):
        context = {
            'title': 'Class-based view',
        }

        return render(request, 'index.html', context)

    ''' dispatch е метод в основния клас , който наследяват всички,
     препраща към метод който ще биде хендълван, важен е защото ни дава контрол на достъпа '''
    def dispatch(self, request, *args, **kwargs):
        # custom logic
        return super().dispatch(request, *args, **kwargs)


class IndexTemplateView(views.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)# ползваме тази структура защото може да дописваме логика
        context['title'] = 'Class-based with TemplateView'# тук добавяме логика
        return context


class TodosListView(views.ListView):# Generic View , функциите са за къстъмизиране 
    model = Todo
    template_name = 'todos-list.html'
    ordering = ('title', 'category__name')# сортиране
    context_object_name = 'todos'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'My todos'

        return context

    def get_queryset(self):
        queryset = super().get_queryset()

        title_filter = self.request.GET.get('filter', None)
        if title_filter:
            queryset = queryset.filter(title__contains=title_filter)

        return queryset


class TodoDetailsView(views.DetailView):
    model = Todo
    template_name = 'todo-details.html'
    context_object_name = 'todo'

    # def get_object(self, queryset=None):

    # def get_template_names(self):
    #     # if admin => show admin template
    #     # else => show regular template


class CreateTodoForm:
    pass


class TodoCreateView(views.CreateView):
    model = Todo
    template_name = 'todo-create.html'
    success_url = reverse_lazy('todos list')  # ако винаги е едно и също
    fields = ('title', 'description', 'category')

    # form_class = CreateTodoForm

    # def get_form_class(self):
    #     pass

    # When different based on the create  /  да те редиректва на различно място
    # def get_success_url(self):
    #     pass

# def sample():
#     pk = 1
#     Todo.objects.get(pk=pk)
#     Todo.objects.filter(pk=pk).get()

# class RedirectToIndexView(views.RedirectView):
#     def get_redirect_url(self, *args, **kwargs):
#         if ...:
#             return 'place 1'
#         else:
#             return 'place 2'

# class PetDetails(views.DetailView):
#     model = Pet # The model
#     template_name = 'pet-details.html'
