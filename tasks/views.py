from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from tasks.forms import TaskForm
from tasks.models import Task


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/list_task.html"
    context_object_name = "tasks"
    paginate_by = 5

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/add_task.html"
    success_url = reverse_lazy("web:list_task_web")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["title", "description"]
    template_name = "tasks/edit_task.html"
    success_url = reverse_lazy("web:list_task_web")

    def get_object(self, queryset=None):
        task = super().get_object(queryset)
        if task.user != self.request.user:
            raise PermissionDenied(
                "You do not have permission to edit this task."
            )
        return task


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = "tasks/delete_task.html"
    success_url = reverse_lazy("web:list_task_web")

    def get_object(self, queryset=None):
        task = super().get_object(queryset)
        if task.user != self.request.user:
            raise PermissionDenied(
                "You do not have permission to delete this task."
            )
        return task
