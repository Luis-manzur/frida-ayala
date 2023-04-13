from django.http import JsonResponse

from frida_ayala.locations.models import Municipality


def municipalities_for_state(request):
    if request.is_ajax() and request.GET and 'state_id' in request.GET:
        objs = Municipality.objects.filter(state=request.GET['state_id'])
        return JsonResponse([{'id': o.id, 'name': str(o)}
                             for o in objs])
    else:
        return JsonResponse({'error': 'Not Ajax or no GET'})
