from django.shortcuts import render, redirect, get_object_or_404
from .forms import InstructionForm
from django.shortcuts import render, get_object_or_404
from .models import Instruction

# View for '/compass'
def compass_view(request):
    # Handle the Form submission (POST)
    if request.method == 'POST':
        form = InstructionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('compass')
    else:
        form = InstructionForm()

    instructions = Instruction.objects.all()

    return render(request, 'our_app/compass.html', {
        'form': form,
        'instructions': instructions
    })

def instruction_detail_view(request, instruction_id):
    # 1. Get the current instruction
    instruction = get_object_or_404(Instruction, pk=instruction_id)

    # 2. Prepare variables for the summary
    show_summary = False
    total_distance = 0
    average_risk = 0

    # 3. Check if the "Summary" button was clicked
    # We will assume the button sends a GET parameter ?summary=true
    if request.GET.get('summary') == 'true':
        show_summary = True

        # --- THE PATH FINDING ALGORITHM ---
        current_node = instruction
        total_risk_sum = 0
        count = 0

        # Loop through the chain until there is no next instruction
        while current_node:
            total_distance += current_node.distance
            total_risk_sum += current_node.risk_level
            count += 1

            # Try to move to the next one
            # We use hasattr because if there is no next instruction,
            # accessing .next_instruction would throw an error.
            if hasattr(current_node, 'next_instruction'):
                current_node = current_node.next_instruction
            else:
                current_node = None  # Stop the loop

        # Calculate Average
        if count > 0:
            average_risk = total_risk_sum / count

    return render(request, 'our_app/detail.html', {
        'instruction': instruction,
        'show_summary': show_summary,
        'total_distance': total_distance,
        'average_risk': average_risk
    })