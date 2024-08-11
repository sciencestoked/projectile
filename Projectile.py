import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

def projectile(u, angg):
    ang = np.radians(angg)

    st.write(f"The Angle in Radians is = {ang:.2f}")

    vy = u * np.sin(ang)
    vx = u * np.cos(ang)

    st.write(f"The velocity in x is {vx:.2f} m/s and the velocity in y is {vy:.2f} m/s")

    T = 2 * vy / 9.8
    T = int(100 * T)

    cm_range = int(vx * T) + 1
    cm_height = int(100 * vy * vy / 19.6) + 1

    st.write(f"Max Range is {cm_range} cm, Max Height is {cm_height} cm, and Time of Flight is {T / 100:.2f} s")

    array = np.zeros([cm_height, cm_range])

    for t in range(0, T):
        x = vx * t
        y = vy * t - 4.9 * t * t / 100
        x = int(x)
        y = cm_height - int(y) - 1
        array[y, x] = 1

    # Plot the trajectory
    plt.figure(figsize=(5, 5))
    plt.imshow(array, 
               cmap='Blues_r', 
               interpolation='none'
               )
    plt.axis('off')  # Hide axes
    st.pyplot(plt)  # Display the plot in Streamlit

# Streamlit interface
st.title('Projectile Motion Simulation')

# Replace number_input with sliders
u = st.slider('Select the velocity of the projectile (m/s)', min_value=0.0, max_value=30.0, value=10,step=0.1)
a = st.slider('Select the angle of projection (degrees)', min_value=0.0, max_value=90.0, value=60,step=0.1)

# Update the plot continuously
projectile(u, a)
