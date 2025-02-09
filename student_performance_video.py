from manim import *
import numpy as np

class LinearRegressionScene(Scene):
    def construct(self):
        # Scene 1: Title and Introduction
        title = Text("Exploring Linear Regression")
        self.play(Write(title))
        self.wait()
        self.play(title.animate.scale(0.8).to_edge(UP))

        # Create axes and store as instance variables
        axes_group = self.create_axes()
        self.axes = axes_group[0]  # Store the actual axes object
        self.play(Create(axes_group))
        
        # Scene 2: Generate and plot data points
        data_points = self.create_data_points()
        self.play(*[Create(dot) for dot in data_points])
        self.wait()

        # Scene 3: Show the linear equation
        equation = self.create_equation()
        self.play(Write(equation))
        self.wait()
        self.play(equation.animate.to_edge(UP).shift(DOWN))

        # Scene 4: Fit line animation
        line = self.create_fit_line()
        self.play(Create(line))
        
        # Scene 5: Cost function visualization
        cost_function = self.create_cost_visualization()
        self.play(
            *[Create(element) for element in cost_function],
            run_time=2
        )
        self.wait()

        # Scene 6: Gradient descent
        gradient_path = self.create_gradient_descent()
        self.play(MoveAlongPath(gradient_path[0], gradient_path[1]))
        self.wait(2)

    def create_axes(self):
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 90, 10],
            axis_config={
                "stroke_width": 2,
                "include_ticks": True,
                "include_tip": True,
            },
            x_axis_config={"label_direction": DOWN},
            y_axis_config={"label_direction": LEFT}
        )
        labels = axes.get_axis_labels(x_label="x", y_label="y")
        return VGroup(axes, labels)

    def create_data_points(self):
        # Generate synthetic data points with some noise
        x_vals = np.linspace(0, 5, 10)
        y_vals = 15 * x_vals + 20 + np.random.normal(0, 5, 10)
        
        dots = VGroup(*[
            Dot(self.axes.c2p(x, y), color=BLUE)
            for x, y in zip(x_vals, y_vals)
        ])
        return dots

    def create_equation(self):
        equation = MathTex(
            "y", "=", "m", "x", "+", "b",
            substrings_to_isolate=["y", "m", "x", "b"]
        )
        equation.set_color_by_tex_to_color_map({
            "m": BLUE,
            "b": RED
        })
        return equation

    def create_fit_line(self):
        line = Line(
            start=self.axes.c2p(0, 20),
            end=self.axes.c2p(5, 95),
            color=YELLOW
        )
        return line

    def create_cost_visualization(self):
        # Create a smaller coordinate system for cost function
        cost_axes = Axes(
            x_range=[-2, 6],
            y_range=[0, 10],
            x_length=3,
            y_length=2,
        ).to_corner(DR)
        
        # Create the cost function graph
        cost_graph = cost_axes.plot(
            lambda x: 0.1 * (x - 2) ** 2 + 1,
            x_range=[-2, 6],
            color=GREEN
        )
        
        cost_label = Text("Cost Function", font_size=24).next_to(cost_axes, UP)
        return VGroup(cost_axes, cost_graph, cost_label)

    def create_gradient_descent(self):
        # Create a point and path for gradient descent visualization
        point = Dot(color=RED)
        
        # Create the path on the main axes
        path = VMobject()
        path.set_points_smoothly([
            self.axes.c2p(x, 15 * x + 20)  # Using the same line equation as our fit
            for x in np.linspace(5, 2, 100)
        ])
        return (point, path)

if __name__ == "__main__":
    with tempconfig({"quality": "medium_quality", "preview": True}):
        scene = LinearRegressionScene()
        scene.render()