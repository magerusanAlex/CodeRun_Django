from django.shortcuts import render, redirect, get_object_or_404
from .models import Instruction
from .forms import InstructionForm


# View for '/compass'
def compass_view(request):
    # Handle the Form submission (POST)
    if request.method == 'POST':
        form = InstructionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compass')  # Reload page to show new data
    else:
        form = InstructionForm()

    # Get all instructions for the list below the form
    instructions = Instruction.objects.all()

    return render(request, 'our_app/compass.html', {
        'form': form,
        'instructions': instructions
    })


# View for 'instructions/<id>'
def instruction_detail_view(request, instruction_id):
    instruction = get_object_or_404(Instruction, pk=instruction_id)

    # Summary Logic (Placeholder for now)
    # To calculate the route to the end, you will need a loop that finds
    # the 'next' instruction using the reverse relationship.

    return render(request, 'our_app/detail.html', {
        'instruction': instruction
    })