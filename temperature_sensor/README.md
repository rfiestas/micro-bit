micro:bit temperature_sensor
=============

Description
-------
The micro:bit does not have a dedicated temperature sensor. Instead, the temperature provided is actually the temperature of the silicon die on the main CPU. As the processor generally runs cold though (it is a high efficiency ARM core), the temperature is a good approximation of the ambient temperature.

The temperature are mesured on the celsius scale.
By defect each point is equivalent a one celsius degrees.
Positive degrees start on left corner, and negative degrees start on
right corner side.

With button B you can change the temperature scale to represent temperatures biger than 25, then each point is equivalent to 2 celsius degrees.
Press button B to activate or deactivate this function.

Press button A, is a way to display the numerical temperature on the display.

Usage
-------
Clone this repository and flash *main.ts* to your micro:bit.
