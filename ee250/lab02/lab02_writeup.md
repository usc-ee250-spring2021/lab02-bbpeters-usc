Link to demo video: 

Q4.1:  
git clone git@github.com:my-name/my-imaginary-repo.git  
cd my-imaginary-repo  
touch my_second_file.py  
git add my_second_file.py  
git commit -m "Created my second file"  
git push origin master  

Q4.2:
The workflow I adopted was to edit the files directly on
my raspberry pi using nano. To be more efficient in the
future I need to practice with nano's shortcuts and learn
the basic git commands.

Q4.3:
There is a constant delay becuase  the ultrasonicRead()
definition has a delay of 60 ms to wait out the hardware's
delay of 50 ms. The Raspberry Pi uses I2C to communicate with 
the Atmega328P on the GrovePi when it tries to read the 
ultrasonic ranger output.
