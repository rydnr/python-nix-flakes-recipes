from domain.flake import Flake
from domain.recipe.base_flake_recipe import BaseFlakeRecipe

class SetuppyFetchfromgithub(BaseFlakeRecipe):

    """
    Represents a nix flake recipe for setup.py-based projects, using fetchFromGitHub
    """
    def __init__(self, flake: Flake):
        """Creates a new setup.py+fetchFromGitHub flake recipe instance"""
        super().__init__(id)
        self._flake = flake

    def usesGitrepoSha256(self):
        return True

    @classmethod
    def type_matches(cls, flake) -> bool:
        return flake.python_package.get_type() == "setup.py" and not flake.python_package.package_in_pypi()
