Below are the functions used in the code and their description:

1) getCompoundInterest:
This function is used to calculate the compound interest. This function is pure as it does not require to acess state variables.

reqLoan:
This is for the creditor to calculate the final amount to be paid to the owner using getCompoundInterest function and issues the amount of loan of the creditor in the loans mapping. After that it emits the request after adding the load on the mapping.

viewDues:
This is for the owner to view the pending amount of loan which needs to be settled. We type the creditor’s address and it returns the pending amount. Since it is a view-only method, it doesn’t cause any state changes.

settleDues:
This is a ‘owner-only-accesible’ method too, but might lead to state changes. It takes the creditor’s address, and if the loan is settled, it marks the dues as zero and returns true. It will return false if the dues remain unsettled.

Below is an example as to how the functions run:

Suppose there are two accounts, X of owner and Y of creditor. Suppose Y takes a loan of 100 units for 3 years with interest rate of 7% . We call reqLoan function with above parameters. It returns 121 and makes an entry in the loans mapping under key Y. Now we call viewDues from X to get the amount it has to get back. Next we call settleDues to clear the loan and change the amount. Y owes to zero now and hence the loan has been cleared successfully.
