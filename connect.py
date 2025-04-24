#import pyvisa

#rm = pyvisa.ResourceManager('@py')  # Use the PyVISA-py backend
#print(rm.list_resources())

#scope = rm.open_resource('/dev/usbtmc0')  # Adjust as needed
#print(scope.query('*IDN?'))
# above is not working for the system to communicate

with open("/dev/usbtmc0", "wb+") as f:
    f.write(b"*IDN?\n")
    f.flush()
    response = f.read(1024)
    print(response.decode().strip())


#for permissions to run this script, send command in shell
#sudo chmod a+rw /dev/usbtmc0

