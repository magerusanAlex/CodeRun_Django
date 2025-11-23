from django.shortcuts import render, redirect, get_object_or_404
from .forms import InstructionForm
from django.shortcuts import render, get_object_or_404
from .models import Instruction

def compass_view(request):
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
    instruction = get_object_or_404(Instruction, pk=instruction_id)

    show_summary = False
    total_distance = 0
    average_risk = 0

    if request.GET.get('summary') == 'true':
        show_summary = True

        current_node = instruction
        total_risk_sum = 0
        count = 0

        while current_node:
            total_distance += current_node.distance
            total_risk_sum += current_node.risk_level
            count += 1

            if hasattr(current_node, 'next_instruction'):
                current_node = current_node.next_instruction
            else:
                current_node = None

        if count > 0:
            average_risk = total_risk_sum / count

    return render(request, 'our_app/detail.html', {
        'instruction': instruction,
        'show_summary': show_summary,
        'total_distance': total_distance,
        'average_risk': average_risk
    })