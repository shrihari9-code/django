from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Device
from django.utils import timezone

def device_list(request):
    devices = Device.objects.all()
    return render(request, 'devices/device_list.html', {'devices': devices})

def add_device(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        new_device = Device.objects.create(name=name, description=description)
        new_device.modified_date = timezone.now()
        new_device.save()
        
        return redirect('device_list')
    return render(request, 'devices/add_device.html')

    
def update_device(request, device_id):
    device = get_object_or_404(Device, id=device_id)
    device.modified = timezone.now()  # Import timezone if not already imported
    device.save()
    return redirect('device_list')
