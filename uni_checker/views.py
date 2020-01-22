from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import (
    UpdateView,
    ListView,
    CreateView,
    DeleteView,
)
from .models import Item, Row
from django.urls import reverse
from .forms import ExampleFormSetHelper, CreateRowFormSet, ItemForm, UpdateRowFormSet
from crispy_forms.layout import Submit


class ItemCreateView(CreateView):
    model = Item

    template_name = "uni_checker/item_create.html"
    form_class = ItemForm

    def get_context_data(self, **kwargs):
        data = super(ItemCreateView, self).get_context_data(**kwargs)
        helper = ExampleFormSetHelper()
        helper.add_input(Submit("submit", "Save"))
        data["helper"] = helper
        if self.request.POST:
            data['formset'] = CreateRowFormSet(self.request.POST)
        else:
            data['formset'] = CreateRowFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        context['formset'] = CreateRowFormSet(self.request.POST)
        formset = context['formset']
        if formset.is_valid() and form.is_valid():
            form.save()
            for temp_form in formset:
                instance = temp_form.save(commit=False)
                instance.item = form.save()
                instance.save()
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('uni_checker:main_editor')


class ItemReadQuestionIncrease(UpdateView):
    model = Item
    fields = ['id']

    def form_valid(self, form):
        data = self.get_context_data()
        temp_id = data['item'].id
        form.instance.number_of_read_questions = Item.objects.get(pk=temp_id).number_of_read_questions
        if form.instance.number_of_read_questions < form.instance.number_of_questions:
            form.instance.number_of_read_questions += 1
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('uni_checker:exam_mode')


class ItemReadQuestionDecrease(UpdateView):
    model = Item
    fields = ['id']

    def form_valid(self, form):
        data = self.get_context_data()
        temp_id = data['item'].id
        form.instance.number_of_read_questions = Item.objects.get(pk=temp_id).number_of_read_questions
        if form.instance.number_of_read_questions > 0:
            form.instance.number_of_read_questions -= 1
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('uni_checker:exam_mode')


class IndexView(ListView):
    template_name = "uni_checker/index.html"
    model = Item

    def get_context_data(self, **kwargs):
        data = super(IndexView, self).get_context_data(**kwargs)

        temp_sum = 0
        for item in Item.objects.all():
            temp_sum += item.get_progress

        if Item.objects.all().count() == 0:
            data['overall_progress'] = 100
        else:
            data['overall_progress'] = int(temp_sum / Item.objects.all().count())
        return data


class ItemUpdateView(UpdateView):
    model = Item
    template_name = "uni_checker/item_create.html"
    form_class = ItemForm

    def get_context_data(self, **kwargs):
        data = super(ItemUpdateView, self).get_context_data(**kwargs)
        helper = ExampleFormSetHelper()
        helper.add_input(Submit("submit", "Save"))
        data["helper"] = helper
        if self.request.POST:
            data['formset'] = UpdateRowFormSet(self.request.POST, instance=self.object)
        else:
            data['formset'] = UpdateRowFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        formset = context['formset']
        if form.is_valid() and formset.is_valid():
            form.save()
            for temp_form in formset:
                instance = temp_form.save(commit=False)
                instance.item = form.save()
                instance.save()
            return super().form_valid(form)
        else:
            return super().form_invalid(form)

    def get_success_url(self):
        return reverse('uni_checker:main_editor')


class ItemDestructView(SuccessMessageMixin, DeleteView):
    model = Item

    def delete(self, request, *args, **kwargs):
        message = 'Deleted successfully....'
        messages.success(self.request, message)
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('uni_checker:main_editor')


class RowBoolChangeView(UpdateView):
    model = Row
    fields = ['is_completed', 'id']

    def form_valid(self, form):
        data = self.get_context_data()
        temp_id = data['row'].id
        form.instance.is_completed = Row.objects.get(pk=temp_id).is_completed
        form.instance.bool_change()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('uni_checker:main_editor')


class ExamView(ListView):
    template_name = "uni_checker/exam_mode.html"
    model = Item

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        temp_sum = 0
        for item in Item.objects.all():
            temp_sum = temp_sum + item.get_exam_progress
        if Item.objects.all().count() == 0:
            data['overall_exam_progress'] = 100
        else:
            data['overall_exam_progress'] = int(temp_sum / Item.objects.all().count())
        return data


class RowDeleteView(DeleteView):
    model = Row
    success_message = 'deleted...'

    def delete(self, request, *args, **kwargs):
        message = 'deleted successfully'
        messages.success(self.request, message)
        return super().delete(request, *args, **kwargs)

    def get_success_url(self):
        item_id = self.get_context_data()['row'].item_id
        return reverse('uni_checker:item_update', args=[item_id])
