from domain.flake.flake import Flake
from domain.flake.recipe.base_flake_recipe import BaseFlakeRecipe

class SetuppyFetchfromgithubMonorepo(BaseFlakeRecipe):

    """
    Represents a nix flake recipe for setup.py-based monorepo projects, using fetchFromGitHub
    """
    def __init__(self, flake: Flake):
        """Creates a new setup.py+fetchFromGitHub monorepo flake recipe instance"""
        super().__init__(flake)

    def usesGitrepoSha256(self):
        return True

    @classmethod
    def type_matches(cls, flake) -> bool:
        return flake.python_package.git_repo.in_github() and flake.python_package.get_type() == "setup.py" and not flake.python_package.package_in_pypi() and flake.python_package.git_repo.is_monorepo()
