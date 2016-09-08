from search.forms import FilterForm

def categories_processor(request):
    categories=FilterForm()
    return  {'search_form':categories}