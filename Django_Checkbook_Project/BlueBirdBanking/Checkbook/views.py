from django.shortcuts import render, redirect, get_object_or_404
from .forms import AccountForm, TransactionForm
from .models import Account, Transaction

# this function will render the home page when requested
def home(request):
    form = TransactionForm(data=request.POST or None)
 #  checks if request method is post
    if request.method == 'POST':
         pk = request.POST['account']  # if the form is submitted, retrieve which account the user wants to view
         return balance(request, pk)  # call balance function to render that account's balance sheet
    content = {'form': form}  # pass content to the template in a dictionary
     # adds content of form to page
    return render(request, 'checkbook/index.html', content)


#this function will render the Create New Account page when requested
def create_account(request):
    form = AccountForm(data=request.POST or None)  # retrieves the account form
    # checks if request method id post
    if request.method == 'POST':
        if form.is_valid():  # check to see if the submitted form is valid and if so, saves the form
            form.save()  # Saves the new account
            return redirect('index')  # returns user back to home page
    content = {'form': form} # saves the content to the template as a dictionary
    return render(request, 'checkbook/CreateNewAccount.html', content)




  # this function will render the balance page when requested
def balance(request, pk):
    account = get_object_or_404(Account, pk=pk)  # retrieve the requested account using its primary key
    transactions = Transaction.Transactions.filter(account=pk) # retrieve all of that account's transactions
    current_total = account.initial_deposit  # create account total variable, starting with the initial deposit
    table_contents = {}  # create a dictionary into which transaction information will be placed
    for t in transactions: # loop through transactions and determine which is a deposit or withdrawal
        if t.type == 'Deposit':
            current_total += t.amount # if deposited add amount to balance
            table_contents.update({t: current_total}) # add transactions and total to the dictionary
        else:
            current_total -= t.amount  # if withdrawal subtract amount from balance
            table_contents.update({t: current_total})  #add transactions and total to the dictionary
    content = {'account': account, 'table_contents': table_contents, 'balance': current_total}
    return render(request, 'checkbook/BalanceSheet.html', content)


# this function will render the transaction page when requested
def transaction(request):
    form = TransactionForm(data=request.POST or None)
    # checks if request method is post
    if request.method == 'POST':
        if form.is_valid(): # checks to see if the submiteted form is valid and if so saves
            pk = request.POST['account']  # retrieve which account the transaction was for
            form.save() # saves the transaction form
            return balance(request, pk)  # redirects user to home page after form submission
        # pass content to the template in the dictionary
    content = {'form': form}
    return render(request, 'checkbook/AddTransaction.html', content)