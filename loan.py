def annuity_rate_R(n,r,facevalue):
    # print(r,n,facevalue)
    # r = 0.03
    # n = 15
    # facevalue = 100
    # print(r,n,facevalue)

    q = 1 + r
    part1 = pow(q,n)*r
    part2 = pow(q,n)-1
    return (part1/part2)*facevalue
    

def annuity_redemption(S0, r, n, t):
    # r = 0.03
    part1 = r
    part2 = pow(1+r,n)-1
    return (part1/part2) *S0* pow(1+r,t-1)
  
def calc_cashflows(n,r):    
    redemption_payments = []
    interest_payments = []
    labels = []
    cashflow_table = []
    facevalue = 100
    r = float(r)
    n = int(n)
    r_new = r/100
    rate = annuity_rate_R(n,r_new,facevalue)
    balance = facevalue


   # print('rate',rate,'r/100',r/100, 'n',n)
    
    for year in range(1,n+1):
        red_rate = round(annuity_redemption(facevalue, r/100, n, year),2)
        redemption_payments.append(red_rate)
        # print('red_rate',red_rate)
        interest_paymnet = round(rate - red_rate,2)
        balance = round(balance - red_rate,2)
        interest_payments.append(interest_paymnet)
        cashflow_table.append({'year':year,'rate':round(rate,2),'interest':interest_paymnet,'redemption':red_rate,'balance':balance})
        labels.append(year)

    #print('interest_payments',interest_payments)
    #print('labels',labels)

    return {
        'labels':labels,
        'cashflows':[{'data': interest_payments,'label':'Interest'},{'data': redemption_payments,'label':'Principal'}],
        'cashflow_table':cashflow_table}