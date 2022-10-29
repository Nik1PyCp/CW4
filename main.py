class BuildingError(Exception):
    def __str__(self):
        return "With so much material the house cennot be built!"
def check_material(amount, limit_value):
    if amount > limit_value:
        return "enought material"
    else:
        raise BuildingError(amount)

check_material(300, 300)
