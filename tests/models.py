from otree.common import money_range
from otree.db import models
import otree.models
import otree.widgets

from otree.fields import RandomCharField


class SimpleModel(otree.models.BaseMatch):
    name = models.CharField()


class FormFieldModel(otree.models.BaseMatch):
    null_boolean = models.NullBooleanField()
    big_integer = models.BigIntegerField()
    boolean = models.BooleanField()
    char = models.CharField()
    comma_separated_integer = models.CommaSeparatedIntegerField()
    date = models.DateField()
    date_time = models.DateTimeField()
    alt_date_time = models.DateTimeField(widget=otree.widgets.SplitDateTimeWidget)
    decimal = models.DecimalField()
    email = models.EmailField()
    file = models.FileField()
    file_path = models.FilePathField()
    float = models.FloatField()
    image = models.ImageField()
    ip_address = models.IPAddressField()
    generic_ip_address = models.GenericIPAddressField()
    positive_integer = models.PositiveIntegerField()
    positive_small_integer = models.PositiveSmallIntegerField()
    slug = models.SlugField()
    small_integer = models.SmallIntegerField()
    text = models.TextField()
    alt_text = models.TextField(widget=otree.widgets.TextInput)
    time = models.TimeField()
    url = models.URLField()
    many_to_many = models.ManyToManyField('SimpleModel')
    one_to_one = models.OneToOneField('SimpleModel')

    money = models.MoneyField()
    random_char = RandomCharField()

    sent_amount = models.MoneyField(choices=money_range(0, 0.75))