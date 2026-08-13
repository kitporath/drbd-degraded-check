def degraded(listing: str) -> list[str]:
    healthy = {'UpToDate', 'Diskless'}
    seen = set()
    result = []
    for line in listing.strip().splitlines():
        if line.strip().startswith('| Resource'):
            continue
        cells = [c.strip() for c in line.split('|')]
        cells = [c for c in cells if c]
        if len(cells) < 6:
            continue
        resource = cells[0]
        state = cells[5]
        if state not in healthy or 'StandAlone' in cells[4]:
            if resource not in seen:
                seen.add(resource)
                result.append(resource)
    return sorted(result)
