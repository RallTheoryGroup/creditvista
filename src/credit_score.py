def calculate_credit_score(payment_history: float, credit_utilization: float) -> int:
    """Calculate a simplified credit score between 300 and 850."""
    if not (0 <= payment_history <= 1):
        raise ValueError("payment_history must be between 0 and 1")
    if not (0 <= credit_utilization <= 1):
        raise ValueError("credit_utilization must be between 0 and 1")

    base_score = 300
    history_weight = 350
    utilization_weight = 200

    score = base_score + (payment_history * history_weight) + ((1 - credit_utilization) * utilization_weight)
    return min(int(score), 850)