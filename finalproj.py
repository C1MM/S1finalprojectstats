import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

#open file
fhand = open("finalproject.csv")
lum=[]
error=[]
velocity=[]

#put data in above lists
for line in fhand:
    line=line.strip().split(',')
    if not line[0][0].isalpha():
        velocity.append(float(line[0]))
        error.append(np.log10(float(line[1])))
        lum.append(4.83+2.5*np.log10(float(line[2])))
slope, intercept, r, p, err = stats.linregress(lum,velocity)
print(slope,intercept,r)

#plot scatterplot
plt.plot(lum,velocity,'r.')
plt.xlabel("Absolute magnitude")
plt.ylabel("Radial velocity (km)")

#obtain residuals and plot
residuals=[]
for x in range(len(lum)):   
    residuals.append(velocity[x]-(slope*lum[x]+intercept))
plt.plot(lum,residuals,'.g')
plt.xlabel("Absolute magnitude")
plt.ylabel("Residuals")

#regression line
plt.plot([0,18],[intercept,slope*18.0+intercept],'tab:orange')

#plot histograms
fig, axs = plt.subplots(2,1)
axs[0].hist(velocity,bins='auto',color='red')
axs[0].set_xlim(-175,175)
axs[0].set_xlabel("Radial velocity (km/s)")
axs[0].set_ylabel("Frequency")
axs[1].hist(lum,bins='auto')
axs[1].set_xlim(0,14)
axs[1].set_xlabel("Absolute magnitude")
axs[1].set_ylabel("Frequency")
fig.tight_layout()
plt.ylabel("Frequency")

#show plot and close file
plt.show()
fhand.close()
