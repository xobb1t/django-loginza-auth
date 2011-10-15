from django.dispatch import Signal


post_associate = Signal(providing_args=['instance'])
