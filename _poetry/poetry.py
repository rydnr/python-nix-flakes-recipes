from domain.flake import Flake
from domain.recipe.base_flake_recipe import BaseFlakeRecipe

class Poetry(BaseFlakeRecipe):

    """
    Represents a nix flake recipe for Poetry-based projects.
    """
    def __init__(self, flake: Flake):
        """Creates a new Poetry flake recipe instance"""
        super().__init__(flake)

    @classmethod
    def matches(cls, flake):
        return flake.python_package.get_package_type() == "poetry"
