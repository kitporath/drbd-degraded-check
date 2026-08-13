
from drbd_check import degraded
FIX = """| Resource | Node   | Layers | Usage  | Conns | State              |
| pvc-aaaa | baldar | DRBD   | Unused | Ok    | UpToDate           |
| pvc-aaaa | skuld  | DRBD   | Unused | Ok    | UpToDate           |
| pvc-bbbb | baldar | DRBD   | InUse  | Ok    | Diskless           |
| pvc-cccc | skuld  | DRBD   | Unused | Ok    | SyncTarget(44.66%) |
| pvc-dddd | thor   | DRBD   | Unused | StandAlone | Inconsistent  |"""
def test_flags(): assert degraded(FIX) == ["pvc-cccc", "pvc-dddd"]
def test_healthy_only():
    h = "| Resource | Node | Layers | Usage | Conns | State |\n| r1 | n1 | DRBD | Unused | Ok | UpToDate |"
    assert degraded(h) == []
