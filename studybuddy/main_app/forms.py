from django import forms
from .models import Watering, Plant


class WateringForm(forms.ModelForm):
    class Meta:
        model = Watering
        fields = ["date"]
        widgets = {
            "date": forms.DateInput(
                format=("%Y-%m-%d"),
                attrs={"placeholder": "Select a date", "type": "date"},
            ),
        }

    def plant_detail(request, plant_id):
        plant = Plant.objects.get(id=plant_id)
        # instantiate WateringForm to be rendered in the template
        watering_form = WateringForm()
        return render(
            request,
            "plants/detail.html",
            {
                # include the plant and watering_form in the context
                "plant": plant,
                "watering_form": watering_form,
            },
        )
