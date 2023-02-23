from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
from pyVim.connect import SmartConnectNoSSL, Disconnect

# Connect to vSphere
si = SmartConnectNoSSL(host="<vCenter name>",
                       user="< User ID>",
                       pwd="<Password>")

# Search for the VM by name
vm_name = '<VM to be cloned>'
#vm = si.content.searchIndex.FindByInventoryPath(f'/{vm_name}')

vm = None
for vm_obj in si.content.viewManager.CreateContainerView(si.content.rootFolder, [vim.VirtualMachine], True).view:
    if vm_obj.name == vm_name:
        vm = vm_obj
        break

if vm is None:
    print(f"Virtual machine '{vm_name}' not found.")
    Disconnect(si)
    exit(1)

# Create the clone specification
clone_spec = vim.vm.CloneSpec()

# Set mandatory properties for the clone
clone_spec.location = vim.vm.RelocateSpec()
clone_spec.powerOn = False
clone_spec.template = False

# Clone the VM
clone_task = vm.Clone(name='<Name for cloned VM>', folder=vm.parent, spec=clone_spec)

# Wait for the clone to complete
while clone_task.info.state == vim.TaskInfo.State.running:
    continue


# Disconnect from vSphere
Disconnect(si)
