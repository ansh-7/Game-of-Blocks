getCompoundInterest:
This function calculates the compound interest depending on p, r and t values. Rate is in percent and to remove any overflow variables have been typecasted. It calculates the amount iteratively. It doesn’t require to acess state variables, hence its pure.

reqLoan:
This is for the creditor to calculate the final amount he has to pay to the owner using getCompoundInterest function and issues the amount of loan in the name of the creditor in the loans mapping. After that it emits the request after adding the load on the mapping.

viewDues:
This is for the owner to view the pending amount of loan which needs to be settled. We type the creditor’s address and it returns the pending amount. Since it is a view-only method, it doesn’t cause any state changes.

settleDues:
This is a ‘owner-only-accesible’ method too, but might lead to state changes. It takes the creditor’s address, and if the loan is settled, it marks the dues as zero and returns true. It will return false if the dues remain unsettled.

Example:

Suppose there are two accounts, X of owner and Y of creditor.

Suppose Y takes a loan of 100 units with interest rate of 7% which he will pay back in 3 years. We will call reqLoan function with above parameters with Y. It returns 121 and makes an entry in the loans mapping under key Y.

Now we call viewDues from X to get the amount it has to get back. Next we call settleDues to clear the loan and change the amount. Y still owes to 0 hence the loan has been cleared successfully.
