# mesh points
#mansour k

x = linspace(0, L, Nx+1)    # mesh points in space
dx = x[1] - x[0]
t = linspace(0, T, Nt+1)    # mesh points in time
dt = t[1] - t[0]
F = a*dt/dx**2
u   = zeros(Nx+1)
u_1 = zeros(Nx+1)


for i in range(0, Nx+1):
    u_1[i] = I(x[i])

for n in range(0, Nt):

    for i in range(1, Nx):
        u[i] = u_1[i] + F*(u_1[i-1] - 2*u_1[i] + u_1[i+1])


    u[0] = 0;  u[Nx] = 0


    u_1[:]= u