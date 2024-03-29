from django.conf import settings


def custom_pagination(queryset, request):
    try:
        page = request.query_params.get("page", 1)
        page = int(page)
    except ValueError:
        page = 1

    page_size = settings.PAGE_SIZE
    start = (page - 1) * page_size
    end = start + page_size

    return queryset[start:end]
