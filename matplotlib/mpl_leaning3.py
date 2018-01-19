import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(0,10,100)
print x
y=np.sin(x)
z=np.cos(x**2)

#plt.figure(figsize=(8,4))
plt.plot(x,y,label="$sin(x)$",color="red",linewidth=2)

plt.plot(x,z,label="$cos(x**2)$",color="green")

plt.xlabel("Times")
plt.ylabel("Volt")

plt.title("Pyplot example")
plt.ylim(-1.2,1.2)
plt.legend()
plt.savefig("test.png",dpi=120)
plt.show()