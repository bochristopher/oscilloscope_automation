import vxi11
import time

# Connect to the oscilloscope using its IP address
try:
    scope = vxi11.Instrument("192.168.55.127")
    
    # Verify connection by retrieving device identification
    idn = scope.ask("*IDN?")
    print(f"Successfully connected to: {idn}")
    
    # Example: Get a screenshot
    scope.write("SCDP")
    time.sleep(1)  # Give the scope time to prepare the image
    img_data = scope.read_raw()
    
    # Save the screenshot
    with open('scope_screenshot.png', 'wb') as f:
        f.write(img_data)
    print("Screenshot saved as 'scope_screenshot.png'")
    
    # Example: Read vertical scale from Channel 1
    ch1_scale = scope.ask("C1:VDIV?")
    print(f"Channel 1 vertical scale: {ch1_scale}")
    
    # Close the connection
    scope.close()
    
except Exception as e:
    print(f"Connection error: {e}")