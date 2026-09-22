from django.dispatch import receiver
from django.db.models.signals import post_save
from .models import Order
from django.core.mail import send_mail
from django.core.mail import EmailMessage

@receiver(post_save, sender = Order)
def order_receiver(sender, instance, created, **kwargs):
   print("New Order has been created.")
   # send_mail(
   #    subject="Order",
   #    message="New Order has been created.",
   #    from_email = 'demo@gmail.com',
   #    recipient_list=['dia@gmail.com','ram@gmail.com'])
   

   message = EmailMessage(
      subject="You are awesome!",
      body="Congrats for sending test email with Mailtrap!",
      from_email="hello@demomailtrap.com",
      to=["shtdia0@gmail.com"],
      reply_to=["support@example.com"],
   )
   message.esp_extra = {
      "category": "Integration Test",
      "custom_variables": {"test_variable": "abc"},
   }
   message.send()




# @receiver(post_save, sender = Order)
# new_function