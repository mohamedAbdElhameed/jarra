from django.db import models


# Create your models here.
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import EmailMessage


class MyUser(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    processor_id = models.CharField(max_length=50)
    order_id = models.IntegerField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class OrderSchema(models.Model):
    order_id = models.IntegerField(default=85216)

    def __str__(self):
        return self.order_id


@receiver(post_save, sender=MyUser)
def send_email(sender, instance, **kwargs):
    email_body = """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
    </head>
    <body>
    <b>
    <table align="center" border="10">
    <tr>
        <td align="right">""" + instance.name + """</td>
        <td align="right">الاســـــــــم</td>
    </tr>
    <tr>
        <td align="right">""" + instance.email + """</td>
        <td align="right">البريد الإلكتروني</td>
    </tr>
    <tr>
        <td align="right">""" + instance.phone_number+"""</td>
        <td align="right">رقم الهاتف</td>
    </tr>
    <tr>
        <td align="right">""" + str(instance.order_id)+"""</td>
        <td align="right">رقم الطلب</td>
    </tr>
    </table>
    </b>
    </body>
    </html>
    """ + "\n"
    email = EmailMessage('تطبيق جرة', email_body, to=[instance.email])
    email.content_subtype = "html"
    email.send()
