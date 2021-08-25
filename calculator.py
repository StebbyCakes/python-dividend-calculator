initial_investment = int(input('Initial investment: '))
yearly_investment = int(input('Yearly investment: '))
yearly_increase = int(input('Percent the portfolio price increases per year: '))
yield_investment = int(input('Average portfolio yield: '))
yield_increment = int(input('Percent the yield increases per year: '))
years = int(input('How many years will you invest: '))

current_year = 0



for i in range(0, years):
    if ( i < 1):
        current_year += 1
        capitol = initial_investment + yearly_investment
        dividend = (capitol * (yield_investment / 100))
        yearly_capitol = (((capitol + dividend) * (yearly_increase / 100)) + (capitol + dividend))
        formatted_yearly_capitol = "{:.2f}".format(yearly_capitol)
        print(f" Year: {current_year} Capitol: ${formatted_yearly_capitol} Dividend: ${dividend} yield: {yield_investment}%")
        yearly_yield = yield_investment * (yield_increment / 100) + yield_investment
    else:
        current_year += 1
        dividend = (yearly_capitol * (yearly_yield / 100))
        yearly_capitol = (((yearly_capitol + dividend + yearly_investment) * (yearly_increase / 100)) + (yearly_capitol + dividend + yearly_investment))
        formatted_yearly_capitol = "{:.2f}".format(yearly_capitol)
        formatted_dividend = "{:.2f}".format(dividend)
        formatted_yearly_yield = "{:.2f}".format(yearly_yield)
        print(f"Year: {current_year} Capitol: ${formatted_yearly_capitol} Dividend: ${formatted_dividend} yield: {formatted_yearly_yield}%")
        yearly_yield = yearly_yield * (yield_increment / 100) + yearly_yield
