from domain.flake import Flake
from domain.recipe.base_flake_recipe import BaseFlakeRecipe

class Setuptools(BaseFlakeRecipe):

    """
    Represents a nix flake recipe for setuptools-based projects.
    """
    def __init__(self, flake: Flake):
        """Creates a new setuptools flake recipe instance"""
        super().__init__(flake)
