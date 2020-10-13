import turtle

turtle.setup(width=600, height=500)
turtle.reset()
turtle.hideturtle()
turtle.speed(0)

turtle.bgcolor('black')

c = 0
x = 0

colors = [
# reddish colors
(1.00, 0.00, 0.00), (1.00, 0.03, 0.00), (1.00, 0.05, 0.00), (1.00, 0.07, 0.00), (1.00, 0.10, 0.00), (1.00, 0.12, 0.00),
(1.00, 0.15, 0.00), (1.00, 0.17, 0.00), (1.00, 0.20, 0.00), (1.00, 0.23, 0.00), (1.00, 0.25, 0.00), (1.00, 0.28, 0.00),
(1.00, 0.30, 0.00), (1.00, 0.33, 0.00), (1.00, 0.35, 0.00), (1.00, 0.38, 0.00), (1.00, 0.40, 0.00), (1.00, 0.42, 0.00),
(1.00, 0.45, 0.00), (1.00, 0.47, 0.00),
# orangey colors
(1.00, 0.50, 0.00), (1.00, 0.53, 0.00), (1.00, 0.55, 0.00), (1.00, 0.57, 0.00), (1.00, 0.60, 0.00), (1.00, 0.62, 0.00),
(0.70, 0.65, 0.00), (1.00, 0.60, 0.00), (1.00, 0.70, 0.00), (1.00, 0.72, 0.00), (1.00, 0.75, 0.00), (1.00, 0.78, 0.00),
(0.40, 0.80, 0.00), (1.00, 0.82, 0.00), (1.00, 0.85, 0.00), (1.00, 0.88, 0.00), (1.00, 0.90, 0.00), (1.00, 0.93, 0.00),
(0.10, 0.95, 0.00), (1.00, 0.97, 0.00),
# yellowy colors
(1.00, 1.00, 0.00), (0.95, 1.00, 0.00), (0.90, 1.00, 0.00), (0.85, 1.00, 0.00), (0.80, 1.00, 0.00), (0.75, 1.00, 0.00),
(1.00, 1.00, 0.00), (0.65, 1.00, 0.00), (0.60, 1.00, 0.00), (0.55, 1.00, 0.00), (0.50, 1.00, 0.00), (0.45, 1.00, 0.00),
(1.00, 1.00, 0.00), (0.35, 1.00, 0.00), (0.30, 1.00, 0.00), (0.25, 1.00, 0.00), (0.20, 1.00, 0.00), (0.15, 1.00, 0.00),
(0.10, 1.00, 0.00), (0.05, 1.00, 0.00),
# greenish colors
(0.00, 1.00, 0.00), (0.00, 0.95, 0.05), (0.00, 0.90, 0.10), (0.00, 0.85, 0.15), (0.00, 0.80, 0.20), (0.00, 0.75, 0.25),
(0.00, 0.70, 0.30), (0.00, 0.65, 0.35), (0.00, 0.60, 0.40), (0.00, 0.55, 0.45), (0.00, 0.50, 0.50), (0.00, 0.45, 0.55),
(0.00, 0.40, 0.60), (0.00, 0.35, 0.65), (0.00, 0.30, 0.70), (0.00, 0.25, 0.75), (0.00, 0.20, 0.80), (0.00, 0.15, 0.85),
(0.00, 0.10, 0.90), (0.00, 0.05, 0.95),
# blueish colors
(0.00, 0.00, 1.00), (0.05, 0.00, 1.00), (0.10, 0.00, 1.00), (0.15, 0.00, 1.00), (0.20, 0.00, 1.00), (0.25, 0.00, 1.00),
(0.30, 0.00, 1.00), (0.35, 0.00, 1.00), (0.40, 0.00, 1.00), (0.45, 0.00, 1.00), (0.50, 0.00, 1.00), (0.55, 0.00, 1.00),
(0.60, 0.00, 1.00), (0.65, 0.00, 1.00), (0.70, 0.00, 1.00), (0.75, 0.00, 1.00), (0.80, 0.00, 1.00), (0.85, 0.00, 1.00),
(0.90, 0.00, 1.00), (0.95, 0.00, 1.00)
]


while x < 1000:
	idx = int(c)
	color = colors[idx]
	turtle.color(color)
	turtle.forward(x)
	turtle.right(98)
	x = x + 1
	c = c + 0.1

turtle.exitonclick()