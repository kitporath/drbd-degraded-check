"""Check LINSTOR resource list for degraded resources."""

from typing import List


def degraded(listing: str) -> List[str]:
    """Return sorted unique resource names that are NOT healthy.

    Healthy states are exactly 'UpToDate' and 'Diskless'.
    Any other State, or a Conns of 'StandAlone', is degraded.
    """
    degraded_resources = set()

    lines = listing.strip().splitlines()
    if not lines:
        return []

    # Skip the header line
    header_line = lines[0]
    data_lines = lines[1:]

    for line in data_lines:
        # Strip leading/trailing whitespace from the line
        line = line.strip()
        if not line:
            continue

        # Split by '|' and strip each cell
        cells = [cell.strip() for cell in line.split('|')]

        # Remove empty cells from leading/trailing pipes
        cells = [c for c in cells if c != '']

        if len(cells) < 6:
            continue

        resource = cells[0]
        # cells[1] = Node, cells[2] = Layers, cells[3] = Usage
        conns = cells[4]
        state = cells[5]

        is_degraded = False

        if state not in ('UpToDate', 'Diskless'):
            is_degraded = True

        if conns == 'StandAlone':
            is_degraded = True

        if is_degraded:
            degraded_resources.add(resource)

    return sorted(degraded_resources)
