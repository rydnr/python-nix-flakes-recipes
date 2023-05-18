from domain.flake.flake import Flake
from domain.flake.recipe.base_flake_recipe import BaseFlakeRecipe

class SetuppyFetchPypi(BaseFlakeRecipe):

    """
    Represents a nix flake recipe for setup.py-based projects using fetchPypi.
    """
    def __init__(self, flake: Flake):
        """Creates a new setup.py+fetchPypi flake recipe instance"""
        super().__init__(flake)

    def usesPipSha256(self):
        return True

    @classmethod
    def type_matches(cls, flake) -> bool:
        return flake.python_package.get_type() == "setup.py" and flake.python_package.package_in_pypi()
