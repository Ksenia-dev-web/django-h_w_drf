from django.shortcuts import render
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
       # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def greetings(request):
    response = f'Давайте начнем готовить! Для отображения рецепта блюда используйте строку адреса страницы!'
    return HttpResponse(response)


def recipe_view(request, needed_recipe):
    number_of_guests = int(request.GET.get('servings', 1))
    context = dict()
    if needed_recipe in DATA:
        context['recipe'] = {ingredient: value * number_of_guests for ingredient, value in DATA.get(needed_recipe).items()}
    return render(request, 'calculator/index.html', context)

