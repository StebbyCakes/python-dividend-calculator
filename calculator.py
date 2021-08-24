initial_investment = int(input('Initial investment: '))
yearly_investment = int(input('Yearly investment: '))
yield_investment = int(input('Average portfolio yield: '))
yield_increment = int(input('By what percent will the yield increase per year: '))
years = int(input('How many years will you invest: '))



for i in range(0, years):
    if ( i < 1):
        capitol = initial_investment + yearly_investment
        dividend = (capitol * (yield_investment / 100))
        yearly_capitol = capitol + dividend
        print(f"Capitol: ${yearly_capitol} Dividend: ${dividend} yield: {yield_investment}%")
        yearly_yield = yield_investment * (yield_increment / 100) + yield_investment
    else:
        dividend = (yearly_capitol * (yearly_yield / 100))
        yearly_capitol = yearly_capitol + dividend + yearly_investment
        print(f"Capitol: ${yearly_capitol} Dividend: ${dividend} yield: {yearly_yield}%")
        yearly_yield = yearly_yield * (yield_increment / 100) + yearly_yield
