#######################################################################################################################
###                             Training Onboard & Underwater Radiated Noise & Vibrations                           ###
#######################################################################################################################
#
# Example - Mass Spring System (undamped)
# 
# Author: Kevin Runge
# Last Updated: 3-Sept-2025
#  
# (License information at the end of this file)
# 
#######################################################################################################################


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# --------------------------------------------------------------- 
# Constants
# ---------------------------------------------------------------
k = 4           # [N / m]
m = 1           # [kg]

# --------------------------------------------------------------- 
# initial conditions
# ---------------------------------------------------------------
x0 = 0.1    # [m]
v0 = 0      # [m/s]

# simulation settings
t_end = 10  # [s]
fps = 30    # [1/s]
t = np.linspace(0,t_end, t_end * fps + 1)

# --------------------------------------------------------------- 
# Solution to equation of motion
# ---------------------------------------------------------------
nfreq = np.sqrt(k / m) # [rad/s]
solution = x0 * np.cos(nfreq * t) + (v0 / nfreq) * np.sin(nfreq * t) 



#######################################################################################################################
#
# Utilities
#
#######################################################################################################################

STATIC_PLOT = True
ANIMATE_PLOT = True

# --------------------------------------------------------------- 
# Plot
# ---------------------------------------------------------------
if STATIC_PLOT:
    fig = plt.figure("Mass Spring System")
    plt.plot(t, solution, "b", lw=2, label=r"$x$")
    plt.title(f"Spring Mass System (undamped). Natural Freq. = {round(nfreq,3)} [rad/s]")
    plt.legend(['solution'], loc="lower left")
    plt.xlabel("time [seconds]")
    plt.ylabel(r"$x$ (m)")
    plt.grid()
    plt.show()

# --------------------------------------------------------------- 
# Animation
# ---------------------------------------------------------------
if ANIMATE_PLOT:
    fig, ax = plt.subplots()
    plt.get_current_fig_manager().set_window_title("Mass Spring System")
    x_motion, = ax.plot(t[0], solution[0], "b", lw=2, label=r"$x$")
    plt.title(f"Spring Mass System (undamped). Natural Freq. = {round(nfreq / (2 * np.pi), 3)} [Hz]")
    plt.legend(['solution'], loc="lower left")
    ax.set(xlim=[0, t_end], ylim=[np.min(solution[:]), np.max(solution[:])], xlabel="time [s]", ylabel="x [m]")
    plt.grid()

    def animate_step(frame):
        x_motion.set_xdata(t[:frame])
        x_motion.set_ydata(solution[:frame])

    anim = animation.FuncAnimation(fig, func=animate_step, frames=len(t), interval=1)
    plt.show()

    # anim.save('mass_spring.gif', writer="pillow")


#######################################################################################################################
#
# Released under MIT License
#
# Copyright 2025, TNO
#
# Permission is hereby granted, free of charge, to any person obtaining a copy of this 
# software and associated documentation files (the “Software”), to deal in the Software 
# without restriction, including without limitation the rights to use, copy, modify, 
# merge, publish, distribute, sublicense, and/or sell copies of the Software, and to 
# permit persons to whom the Software is furnished to do so, subject to the following 
# conditions:
#
# The above copyright notice and this permission notice shall be included in all copies 
# or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
# INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A 
# PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE 
# OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#######################################################################################################################