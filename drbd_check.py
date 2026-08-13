def degraded(listing: str) -> list[str]:
    degraded_resources = set()

    for line in listing.strip().splitlines():
        line = line.strip()
        if not line or line.startswith('| Resource'):
            continue

        cells = [cell.strip() for cell in line.split('|')]
        cells = [c for c in cells if c]

        if len(cells) < 6:
            continue

        resource = cells[0]
        conns = cells[4]
        state = cells[5]

        healthy_states = ('UpToDate', 'Diskless')

        if state not in healthy_states or conns == 'StandAlone':
            degraded_resources.add(resource)

    return sorted(degraded_resources)
