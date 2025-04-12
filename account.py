import QuantumRingsLib
from QuantumRingsLib import QuantumRingsProvider

"""     Insert Quantum Ring token and name here (I think a name is just email)     """
TOKEN = None
NAME = None

#Acquire the Quantum Rings Provider
provider = QuantumRingsProvider(token=TOKEN,name=NAME)
print("Account Name: ", provider.active_account()["name"], "\nMax Qubits: ", provider.active_account()["max_qubits"])

#Save the account locally.
provider.save_account(token=TOKEN,name=NAME)
print(provider.saved_accounts(False, "default"))