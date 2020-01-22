from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.core.exceptions import ValidationError

from builtins import str as to_str


# Create your models here.


def validate_test(value):
    if len(value) > 5:
        raise ValidationError(
            'Name is invalid',
            params={'value': value},
        )


class Item(models.Model):
    item_name = models.CharField(max_length=10, unique=True)
    number_of_questions = models.IntegerField(default=0)
    number_of_read_questions = models.IntegerField(default=0, verbose_name='read questions')
    has_deadline = models.BooleanField(default=False)

    @property
    def get_progress(self):
        if self.row_set.all().count() == 0:
            return 1
        else:
            return int(self.row_set.all().filter(is_completed=True).count() / self.row_set.all().count() * 100)

    @property
    def get_exam_progress(self):
        if self.number_of_questions == 0:
            return 100
        else:
            return int(self.number_of_read_questions / self.number_of_questions * 100)

    def __str__(self):
        return self.item_name

    @staticmethod
    def get_absolute_url():
        return reverse('uni_checker:main_editor')

    class Meta:
        ordering = ['item_name']


class Row(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    row_name = models.CharField(max_length=10, default='Lab')
    is_completed = models.BooleanField(default=False)
    deadline = models.DateField(default=timezone.now())

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.row_name

    @property
    def remaining_days(self):
        return (self.deadline - timezone.now().date()) if (self.deadline > timezone.now().date()) else '0 days'

    def bool_change(self):
        if self.is_completed is True:
            self.is_completed = False
        else:
            self.is_completed = True


class ItemDescription(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    description_text = models.TextField()

    def __str__(self):
        return str(self.description_text)


class ItemUrls(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    url_name = models.CharField(blank=True, max_length=10)
    material_link = models.URLField()

    def __str__(self):
        return str(self.material_link)
