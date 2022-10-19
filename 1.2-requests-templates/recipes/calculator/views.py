from django.shortcuts import render


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


def calculate_quantity_ingredients(name_recipe: str, servings=1) -> dict or None:
    if name_recipe not in DATA:
        return None
    recipe_calculated = {ingredient: quantity * servings for
                         ingredient, quantity in DATA[name_recipe].items()}
    return {'recipe': recipe_calculated}


def calculator(request, name_recipe):
    input_servings = int(request.GET.get('servings', 1))
    context = calculate_quantity_ingredients(name_recipe=name_recipe, servings=input_servings)
    print(context)
    return render(request, 'calculator/index.html', context)
