from tcomms_sample.reporting import Kpi, generate_summary


def test_generate_summary_basic():
    kpis = [Kpi("A", 10, 5), Kpi("B", 3, 5)]
    s = generate_summary(kpis)
    assert s["count"] == 2
    assert 0.49 < s["pct_on_target"] < 0.51


def test_generate_summary_empty():
    assert generate_summary([]) == {"count": 0, "pct_on_target": 0.0}
