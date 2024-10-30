from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from samples.models import Sample

from samples.forms import SampleForm
from samples.models import Sample

def top(request):
    samples = Sample.objects.all()
    context = {"samples": samples}
    return render(request, "samples/top.html", context)


@login_required
def samples_new(request):
    if request.method == 'POST':
        form = SampleForm(request.POST)
        if form.is_valid():
            sample = form.save(commit=False)
            sample.created_by = request.user
            sample.save()
            return redirect(samples_detail, samples_id=sample.pk)
    else:
        form = SampleForm()
    return render(request, "samples/samples_new.html", {'form': form})


@login_required
def samples_edit(request, samples_id):
    samples = get_object_or_404(Sample, pk=samples_id)
    if samples.created_by_id != request.user.id:
        return HttpResponseForbidden("このスニペットの編集は許可されていません。")

    if request.method == "POST":
        form = SampleForm(request.POST, instance=samples)
        if form.is_valid():
            form.save()
            return redirect('samples_detail', samples_id=samples_id)
    else:
        form = SampleForm(instance=samples)
    return render(request, 'samples/samples_edit.html', {'form': form})


def samples_detail(request, samples_id):
    samples = get_object_or_404(Sample, pk=samples_id)
    return render(request, 'samples/samples_detail.html',
                  {'samples': samples})
