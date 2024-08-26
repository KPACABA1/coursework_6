from django.forms import ModelForm, BooleanField

from mailing.models import Message, Customer, Mailing


class StyleFormMixin:
    """Класс для стилизации форм"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = "form-check-input"
            else:
                field.widget.attrs['class'] = "form-control"


class MessageForm(StyleFormMixin, ModelForm):
    """Класс форма для сообщений для рассылки"""
    class Meta:
        model = Message
        fields = '__all__'


class CustomerForm(StyleFormMixin, ModelForm):
    """Класс форма для клиентов сервиса"""
    class Meta:
        model = Customer
        fields = '__all__'


class MailingForm(StyleFormMixin, ModelForm):
    """Класс форма для рассылок"""
    class Meta:
        model = Mailing
        exclude = ('date_and_time_of_first_mailing', 'mailing_status', 'date_letter_was_sent')
