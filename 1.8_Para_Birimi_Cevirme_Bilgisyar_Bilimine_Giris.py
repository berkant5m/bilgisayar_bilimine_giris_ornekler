USD_to_GBP   = 0.66
USD_to_EUR   = 0.77
USD_to_JPY   = 99.18
USD_to_INR   = 59.52
GBP_sign     = '\u00A3'
EUR_sign     = '\u20AC'
JPY_sign     = '\u00A5'
INR_sign     = '\u20B9'
dollars = 1000
pounds       = dollars * USD_to_GBP
euros        = dollars * USD_to_EUR
yen          = dollars * USD_to_JPY
reupees      = dollars * USD_to_INR
print('Today, $' + str(dollars))
print('converts to ' + GBP_sign + str(pounds))
print('converts to ' + EUR_sign + str(euros))
print('converts to ' + JPY_sign + str(yen))
print('converts to ' + INR_sign + str(rupees))
