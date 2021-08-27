initial_investment = int(input('Initial investment: '))
yearly_investment = int(input('Yearly investment: '))
yearly_increase = int(input('Percent the portfolio price increases per year: '))
yield_investment = int(input('Average portfolio yield: '))
yield_increment = int(input('Percent the yield increases per year: '))
years = int(input('How many years will you invest: '))

current_year = 1
dividend_total = 0



for i in range(0, years):
    if ( i < 1):
        capitol = initial_investment + yearly_investment
        dividend = (capitol * (yield_investment / 100))
        dividend_total += dividend
        yearly_capitol = (((capitol + dividend) * (yearly_increase / 100)) + (capitol + dividend))
        dividend_vs_capitol = ((dividend_total / yearly_capitol) * 100)
        formatted_dividend_vs_capitol = "{:.2f}".format(dividend_vs_capitol)
        formatted_yearly_capitol = "{:.2f}".format(yearly_capitol)
        print(f" Year: {current_year} Capitol: ${formatted_yearly_capitol} Dividend: ${dividend} Yield: {yield_investment}% Total dividends paid: {dividend_total} Dividend VS Capitol: {formatted_dividend_vs_capitol}%")
        yearly_yield = yield_investment * (yield_increment / 100) + yield_investment


    else:
        current_year += 1
        dividend = (yearly_capitol * (yearly_yield / 100))
        dividend_total += dividend
        yearly_capitol = (((yearly_capitol + dividend + yearly_investment) * (yearly_increase / 100)) + (yearly_capitol + dividend + yearly_investment))
        dividend_vs_capitol = ((dividend_total / yearly_capitol) * 100)
        formatted_dividend_vs_capitol = "{:.2f}".format(dividend_vs_capitol)
        formatted_yearly_capitol = "{:.2f}".format(yearly_capitol)
        formatted_dividend = "{:.2f}".format(dividend)
        formatted_yearly_yield = "{:.2f}".format(yearly_yield)
        formatted_dividend_total = "{:.2f}".format(dividend_total)
        print(f"Year: {current_year} Capitol: ${formatted_yearly_capitol} Dividend: ${formatted_dividend} Yield: {formatted_yearly_yield}% Total dividends paid: {formatted_dividend_total} Dividend VS Capitol: {formatted_dividend_vs_capitol}%")
        yearly_yield = yearly_yield * (yield_increment / 100) + yearly_yield
