import pytest
from src.credit_score import calculate_credit_score


def test_perfect_score():
    score = calculate_credit_score(1.0, 0.0)
    assert score == 850


def test_minimum_score():
    score = calculate_credit_score(0.0, 1.0)
    assert score == 300


def test_average_score():
    score = calculate_credit_score(0.7, 0.3)
    assert 500 <= score <= 700


def test_invalid_payment_history():
    with pytest.raises(ValueError):
        calculate_credit_score(1.5, 0.5)


def test_invalid_credit_utilization():
    with pytest.raises(ValueError):
        calculate_credit_score(0.5, -0.1)