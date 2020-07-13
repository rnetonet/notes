from django.http import HttpResponseBadRequest


def require_AJAX(fx):
    def wrapper(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()
        else:
            return fx(request, *args, **kwargs)

    wrapper.__doc__ = fx.__doc__
    wrapper.__name__ = fx.__name__

    return wrapper

