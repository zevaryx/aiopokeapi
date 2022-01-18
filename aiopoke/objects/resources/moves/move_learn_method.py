from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.objects.utility.common_models import Description
from aiopoke.objects.utility.common_models import Name
from aiopoke.objects.utility.common_models import NamedResource

from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources import VersionGroup


class MoveLearnMethod(NamedResource):
    description: str
    descriptions: Tuple["Description", ...]
    names: Tuple["Name", ...]
    version_groups: Tuple[MinimalResource["VersionGroup"], ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.description = tuple(
            description_data["description"]
            for description_data in data["descriptions"]
            if description_data["language"]["name"] == "en"
        )[0]
        self.descriptions = tuple(
            Description(description_data) for description_data in data["descriptions"]
        )
        self.names = tuple(Name(name_data) for name_data in data["names"])
        self.version_groups = tuple(
            MinimalResource(version_group_data)
            for version_group_data in data["version_groups"]
        )
