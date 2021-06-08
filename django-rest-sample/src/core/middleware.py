from django.http import JsonResponse


def simple_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        validated = False

        if(validated):
            print("Validated")
        else:
            print("Not Validated")
            return JsonResponse({'message': "Not Validated"})

        response = get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware
