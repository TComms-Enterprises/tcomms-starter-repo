
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Kpi:
    name: str
    value: float
    target: float

def generate_summary(kpis: List[Kpi]) -> Dict[str, float]:
    count = len(kpis)
    if count == 0:
        return {"count": 0, "pct_on_target": 0.0}
    on_target = sum(1 for k in kpis if k.value >= k.target)
    return {"count": count, "pct_on_target": on_target / count}
