from app import classify_intent


def test_insurance_detection():
    result = classify_intent("best insurance roofing company after hail in Alpharetta")
    assert "insurance-documentation" in result["tags"]
    assert "trust-selection" in result["tags"]


def test_repair_detection():
    result = classify_intent("roof leak repair in Milton")
    assert "repairability" in result["tags"]
