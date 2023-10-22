from .models import*
from rest_framework.serializers import *

class GPT_Mess(ModelSerializer):

    class Mota:
        model=GPT

        fields=[
            "messages"
        ]