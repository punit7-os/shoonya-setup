from bsedata.bse import BSE
import pandas as pd

b = BSE()
print(b)
# Output:
# Driver Class for Bombay Stock Exchange (BSE)

# to execute "updateScripCodes" on instantiation
b = BSE(update_codes = True)
bs = b.getScripCodes()
df= pd.DataFrame(bs, index=[1])

print(df)
# Output too large to display in docs
# returns a dictionary with scrip codes as keys and respective company names as values


b = BSE()
codelist = ["500116", "512573"]
for code in codelist:
    quote = b.getQuote(code)
    print(quote["companyName"])
    print(quote["currentValue"])
    print(quote["updatedOn"])