from django.test import TestCase
from .models import Item, Row


class ItemTestCase(TestCase):
    def setUp(self) -> None:
        item1 = Item.objects.create(item_name='test_item_1')
        Row.objects.create(item=item1, row_name='row1', is_completed=True)

        item2 = Item.objects.create(item_name='test_item_2')
        Row.objects.create(item=item2, row_name='row2', is_completed=True)
        Row.objects.create(item=item2, row_name='row3')
        Row.objects.create(item=item2, row_name='row4')

    def test_item_progress(self):
        """ Item progress is calculated correctly """
        item1 = Item.objects.get(item_name='test_item_1')
        self.assertEqual(item1.get_progress(), 1.00)

        item2 = Item.objects.get(item_name='test_item_2')
        self.assertEqual(item2.get_progress(), round(1/3, 2))
