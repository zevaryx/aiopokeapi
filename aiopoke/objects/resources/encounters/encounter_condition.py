from typing import Tuple
from typing import TYPE_CHECKING

from aiopoke.objects.utility.common_models import Name
from aiopoke.objects.utility.common_models import NamedResource

from aiopoke.utils.minimal_resources import MinimalResource

if TYPE_CHECKING:
    from aiopoke.objects.resources.encounters import EncounterConditionValue


class EncounterCondition(NamedResource):
    values: Tuple[MinimalResource["EncounterConditionValue"], ...]
    names: Tuple["Name", ...]

    def __init__(self, data) -> None:
        super().__init__(data)
        self.values = tuple(
            MinimalResource(encounter_condition_value)
            for encounter_condition_value in data["values"]
        )
        self.names = tuple(Name(name_data) for name_data in data["names"])
