import os

client_filename = "clients.txt"
transaction_filename = "transactions.txt"

def add_client(client_name):
    with open(client_filename,'a') as file:
        file.write(client_name+"\n")
      
def add_transaction(debtor, creditor, amount):
    with open(transaction_filename,'a') as file:
        file.write(debtor+" "+creditor+" "+str(amount)+"\n")
        
def get_clients():
    pass

def get_transactions():
    pass
