import numpy as np

# 초기 투자금, 매달 투자금, 증가액, 투자 기간 설정
initial_investment = 3000 * 10**4  # 3000만원
monthly_investment = 200 * 10**4  # 200만원
increase_amount = 50 * 10**4  # 50만원
years = 40
increase_interval = 5
target_amount = 70 * 10**9  # 70억원

# 분리과세 구간 설정
split_tax_threshold = 2 * 10**8  # 2억원
split_tax_rate = 0.099
holding_tax_rate = 0.154

# 누진세율 구간 설정
progressive_tax_brackets = [1400 * 10**4, 5000 * 10**4, 8800 * 10**4, 15000 * 10**4, 30000 * 10**4, 50000 * 10**4, 100000 * 10**4]
progressive_tax_rates = [0.06, 0.15, 0.24, 0.35, 0.38, 0.40, 0.42, 0.45]
progressive_deductions = [0, 126 * 10**4, 576 * 10**4, 1544 * 10**4, 1994 * 10**4, 2594 * 10**4, 3594 * 10**4, 6594 * 10**4]

# 근로소득 계산 (매달 투자금 + 50만원)
monthly_salary = monthly_investment + 50 * 10**4

def calculate_future_value(pv, rate, n):
    """Calculate the future value of an investment"""
    return pv * ((1 + rate) ** n)

def calculate_tax(income):
    """Calculate the progressive tax based on the income"""
    if income <= progressive_tax_brackets[0]:
        return income * progressive_tax_rates[0]
    for i in range(1, len(progressive_tax_brackets)):
        if income <= progressive_tax_brackets[i]:
            return income * progressive_tax_rates[i] - progressive_deductions[i]
    return income * progressive_tax_rates[-1] - progressive_deductions[-1]

# 투자금과 연평균 수익률을 기반으로 한 미래 가치 계산
def simulate_investment_rate(rate):
    total_value = initial_investment
    for year in range(years):
        # 투자금 계산
        current_monthly_investment = monthly_investment + (year // increase_interval) * increase_amount
        # 매달 투자
        for month in range(12):
            total_value += current_monthly_investment
            total_value = calculate_future_value(total_value, rate/12, 1)
        # 세금 계산
        if total_value <= split_tax_threshold:
            total_value -= total_value * split_tax_rate
        else:
            excess = total_value - split_tax_threshold
            total_value = split_tax_threshold * (1 - split_tax_rate) + excess * (1 - holding_tax_rate)
        # 근로소득 포함
        total_value += 12 * monthly_salary
    return total_value

# 목표 금액을 달성하기 위한 연평균 수익률 찾기
def find_annual_rate(target, tolerance=1e-2, max_iter=1000):
    low, high = 0, 1
    for _ in range(max_iter):
        mid = (low + high) / 2
        future_value = simulate_investment_rate(mid)
        if abs(future_value - target) < tolerance:
            return mid
        elif future_value < target:
            low = mid
        else:
            high = mid
    return mid

# 연평균 수익률 계산
annual_rate = find_annual_rate(target_amount)
annual_rate * 100  # 퍼센트로 표현