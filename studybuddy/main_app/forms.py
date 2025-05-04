from django import forms
from .models import Message, StudyGroup


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["content"]

    def plant_detail(request, plant_id):
        plant = StudyGroup.objects.get(id=plant_id)
        # instantiate MessageForm to be rendered in the template
        message_form = MessageForm()
        return render(
            request,
            "plants/detail.html",
            {
                # include the plant and message_form in the context
                "plant": plant,
                "message_form": message_form,
            },
        )
