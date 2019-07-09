import numpy as np
import matplotlib.pyplot as plt
from numpy.fft import fft, fftfreq, ifft

##Setup for domain
#number of points

n =1000

#distance (in metres) or time period (in seconds)

Lx = 100

#angular frequency

omg = 2.0*np.pi/Lx

##creating individual signals
x=np.linspace(0,Lx,n)
y1=1.0*np.cos(5.0*omg*x)
y2=1.0*np.sin(10.0*omg*x)
y3=0.5*np.sin(20.0*omg*x)

##full signal
y=y1+y2+y3

print(5*omg)
print(10*omg)
print(20*omg)

#preparatory steps
#creates all the necessary frequencies
freqs = fftfreq(n)

#mask array to be used for power spectra
#ignoring half the values, as they are complex conjugates of the other
mask = freqs>0

##FFT and power spectra calculations
##fft values
fft_vals = fft(y)

##true theoretical fft
fft_theo = 2.0*np.abs(fft_vals/n)

plt.figure(1)
plt.title('Original signal')
plt.plot(x,y,color='xkcd:salmon', label = 'original')


plt.figure(2)
plt.plot(freqs[mask], fft_theo[mask], label='true fft values')
plt.title('True fft values')
plt.show()
