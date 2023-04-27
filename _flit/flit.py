from domain.flake import Flake
from domain.recipe.base_flake_recipe import BaseFlakeRecipe

class Flit(BaseFlakeRecipe):

    """
    Represents a nix flake recipe for flit-based projects.
    """
    def __init__(self, flake: Flake):
        """Creates a new flit flake recipe instance"""
        super().__init__(id)
        self._flake = flake

    @classmethod
    def matches(cls, flake):
        return flake.python_package.get_package_type() == "flit"
