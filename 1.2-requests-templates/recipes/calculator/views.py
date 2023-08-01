from django.shortcuts import render, reverse
from django.http import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def omlet(request):
    template_name = 'calculator/index.html'
    servings = int(request.GET.get("servings", 1))
    ing = {key: val * servings for key, val in DATA['omlet'].items()}
    context = {'context': ing}
    return render(request, template_name, context)


def pasta(request):
    template_name = 'calculator/index.html'
    servings = int(request.GET.get("servings", 1))
    ing = {key: val * servings for key, val in DATA['pasta'].items()}
    context = {'context': ing}
    return render(request, template_name, context)


def buter(request):
    template_name = 'calculator/index.html'
    servings = int(request.GET.get("servings", 1))
    ing = {key: val * servings for key, val in DATA['buter'].items()}
    context = {'context': ing}
    return render(request, template_name, context)
