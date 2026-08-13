from drbd_check import degraded

# Empty
assert degraded('') == []
# Header only
assert degraded('| Resource | Node | Layers | Usage | Conns | State |') == []
# All healthy
e = """| Resource | Node | Layers | Usage | Conns | State |
| r1 | a | DRBD | Unused | Ok | UpToDate |
| r2 | a | DRBD | Unused | Ok | Diskless |"""
assert degraded(e) == []
# StandAlone with healthy state
e2 = """| Resource | Node | Layers | Usage | Conns | State |
| r3 | a | DRBD | Unused | StandAlone | UpToDate |"""
assert degraded(e2) == ['r3']
# Duplicates
e3 = """| Resource | Node | Layers | Usage | Conns | State |
| r4 | a | DRBD | Unused | Ok | Inconsistent |
| r4 | b | DRBD | Unused | Ok | Inconsistent |"""
assert degraded(e3) == ['r4']
# Main example
ex = """| Resource | Node | Layers | Usage | Conns | State              |
| pvc-aaaa | baldar | DRBD   | Unused | Ok    | UpToDate           |
| pvc-aaaa | skuld  | DRBD   | Unused | Ok    | UpToDate           |
| pvc-bbbb | baldar | DRBD   | InUse  | Ok    | Diskless           |
| pvc-cccc | skuld  | DRBD   | Unused | Ok    | SyncTarget(44.66%) |
| pvc-dddd | thor   | DRBD   | Unused | StandAlone | Inconsistent  |"""
assert degraded(ex) == ['pvc-cccc', 'pvc-dddd']
print('All tests passed')
