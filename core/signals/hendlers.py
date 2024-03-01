from store.signals import order_crated
from django.dispatch import receiver


@receiver(order_crated)
def on_order_created(sender, **kwargs):
    print(kwargs["order"])
