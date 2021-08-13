from collections import deque
from copy import deepcopy
from typing import Any, Dict
from tiger_card.data_models.model_exceptions import UnreachableZoneException


class ZoneIdentifier:
    # TODO: Move this identification logic- TellDontAsk
    @staticmethod
    def distinguish_zone_data(zones_map: Dict[str, Any], from_zone: str, to_zone: str) -> Dict[str, Any]:
        if from_zone == to_zone:  # same zone
            zone_data = zones_map[from_zone]
        else:  # cross zone
            neighbors = zones_map[from_zone]["neighbors"]
            try:
                zone_data = neighbors[to_zone]
            except Exception:
                raise UnreachableZoneException("Destination zone is not reachable from {} zone".format(from_zone))
        return zone_data
