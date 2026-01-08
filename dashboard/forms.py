from .models import Child
from django import forms
from tasks.models import AGE_GROUP_CHOICES, Task



class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['name','date_of_birth' ]
        widgets = {
             "name": forms.TextInput(attrs={"class": "form-control"}),
             "date_of_birth": forms.DateInput(attrs={"type": "date", "class": "form-control"}),
        }

class AssignChoresForm(forms.Form):
    child = forms.ModelChoiceField(
        queryset=Child.objects.none(),
        widget=forms.Select(attrs={"class": "form-select"})
    )

    chores = forms.ModelMultipleChoiceField(
        queryset=Task.objects.none(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user", None)
        super().__init__(*args, **kwargs)
        # Get all the children that belong to the loged in parent
        children_list = Child.objects.filter(parent=user)
        self.fields["child"].queryset = children_list

        # choose selected child the dropdown box, otherwise first child
        child_id = self.data.get("child")
        selected_child = None

        if child_id:
            try:
                selected_child = Child.objects.get(id=child_id, parent=user)
            except Child.DoesNotExist:
                selected_child = None
        else:
            selected_child = children_list.first()
            if selected_child:
                self.initial["child"] = selected_child

        # show only chores for that child's age group
        if selected_child:
            self.fields["chores"].queryset = Task.objects.filter(
                age_group=selected_child.age_group()
            )
        else:
            self.fields["chores"].queryset = Task.objects.none()