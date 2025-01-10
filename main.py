from manim import *
import numpy as np

def get_random_points(n_points=20):
    return np.array([[np.random.uniform(-4, 4), np.random.uniform(-3, 3), 0] for _ in range(n_points)])

class StudentPerformancePrediction(Scene):
    def construct(self):
        # Opening sequence with mathematical beauty
        title = Tex(r"The Mathematics of", font_size=60)
        subtitle = Tex(r"Student Success Prediction", font_size=72)
        group = VGroup(title, subtitle).arrange(DOWN)
        
        # Create elegant background grid
        background_grid = NumberPlane(
            x_range=(-8, 8, 1),
            y_range=(-4, 4, 1),
            background_line_style={
                "stroke_opacity": 0.3,
                "stroke_width": 1,
                "stroke_color": BLUE_E
            }
        )
        
        self.play(
            Create(background_grid, run_time=2),
            Write(title),
            Write(subtitle)
        )
        self.wait()

        # Transform into a fascinating mathematical visualization
        self.play(
            FadeOut(title),
            FadeOut(subtitle)
        )

        # Creating student data points with mathematical beauty
        points = get_random_points()
        dots = VGroup(*[Dot(point=p, radius=0.05, color=BLUE) for p in points])
        
        # Add mathematical equations that govern student performance
        equation = MathTex(
            r"P(success) = \frac{1}{1 + e^{-(\beta_0 + \beta_1x_1 + \beta_2x_2)}}"
        ).to_edge(UP)

        # Show how data points transform into predictions
        self.play(
            *[GrowFromCenter(dot) for dot in dots],
            Write(equation)
        )

        # Create elegant coordinate system for performance visualization
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 10, 1],
            axis_config={"color": WHITE},
            x_length=6,
            y_length=4
        ).shift(DOWN)
        
        labels = axes.get_axis_labels(
            x_label=Tex("Time"), 
            y_label=Tex("Performance")
        )

        # Transform points into a beautiful performance curve
        def performance_curve(x):
            return 5 + 2 * np.sin(x/2) * np.exp(-x/10)
        
        curve = axes.plot(
            performance_curve,
            color=YELLOW,
            x_range=[0, 10]
        )

        # Add moving dot that traces the curve
        moving_dot = Dot(color=RED)
        moving_dot.move_to(axes.c2p(0, performance_curve(0)))

        def update_dot(mob, alpha):
            x = alpha * 10
            mob.move_to(axes.c2p(x, performance_curve(x)))

        # Create Neural Network Visualization
        def create_neural_network():
            layers = [3, 4, 4, 1]  # Network architecture
            network = VGroup()
            
            for i, layer_size in enumerate(layers):
                layer = VGroup(*[Circle(radius=0.2, fill_opacity=0.3) for _ in range(layer_size)])
                layer.arrange(DOWN, buff=0.5)
                if i > 0:  # Add connections between layers
                    prev_layer = network[-1]
                    for prev_neuron in prev_layer:
                        for neuron in layer:
                            connection = Line(prev_neuron, neuron, stroke_opacity=0.3)
                            network.add(connection)
                network.add(layer)
            
            network.arrange(RIGHT, buff=1)
            return network

        neural_network = create_neural_network().scale(0.7).to_edge(DOWN)

        # Elegant animation sequence
        self.play(
            Create(axes),
            Write(labels)
        )

        self.play(
            Create(curve),
            Create(neural_network)
        )

        # Show how different factors affect prediction
        factors = VGroup(
            Tex("Academic History"),
            Tex("Study Patterns"),
            Tex("Engagement Metrics")
        ).arrange(RIGHT, buff=1).next_to(neural_network, UP)

        # Create pulsing effect for neural network
        def get_pulse_animation(network):
            animations = []
            for layer in network:
                if isinstance(layer, Circle):
                    animations.append(
                        Succession(
                            ApplyMethod(layer.set_fill, BLUE, 0.8),
                            ApplyMethod(layer.set_fill, BLUE, 0.3)
                        )
                    )
            return animations

        # Animate dot moving along performance curve
        self.play(
            UpdateFromAlphaFunc(moving_dot, update_dot),
            *get_pulse_animation(neural_network),
            run_time=3
        )

        # Show mathematical transformation
        transform_eq = MathTex(
            r"\vec{x} \rightarrow W\vec{x} + \vec{b} \rightarrow \sigma(\vec{x})"
        ).next_to(neural_network, UP)

        self.play(
            Write(transform_eq),
            FadeOut(factors)
        )

        # Final elegant conclusion
        conclusion = Tex(
            r"Early intervention changes trajectories"
        ).scale(1.2).to_edge(UP)

        probability_distribution = axes.plot(
            lambda x: 4 + 2 * np.exp(-((x-5)**2)/4),
            color=BLUE,
            x_range=[0, 10]
        )

        self.play(
            ReplacementTransform(equation, conclusion),
            ReplacementTransform(curve, probability_distribution)
        )

        # Add confidence intervals
        upper_bound = axes.plot(
            lambda x: 4 + 2 * np.exp(-((x-5)**2)/4) + 0.5,
            color=BLUE_E,
            stroke_opacity=0.3
        )
        lower_bound = axes.plot(
            lambda x: 4 + 2 * np.exp(-((x-5)**2)/4) - 0.5,
            color=BLUE_E,
            stroke_opacity=0.3
        )

        confidence_region = axes.get_area(
            lower_bound,
            upper_bound,
            [0, 10],
            color=BLUE,
            opacity=0.2
        )

        self.play(
            Create(confidence_region),
            Create(upper_bound),
            Create(lower_bound)
        )

        # Final mathematical insight
        final_equation = MathTex(
            r"\lim_{t \to \infty} P(success|intervention) > P(success)"
        ).next_to(conclusion, DOWN)

        self.play(
            Write(final_equation)
        )

        self.wait(2)

def create_wandering_path():
    npoints = 100
    path_points = []
    cur_point = np.array([0, 0, 0])
    for _ in range(npoints):
        cur_point += np.random.normal(0, 0.1, size=3)
        path_points.append(cur_point.copy())
    return path_points

class MathematicalConcepts(Scene):
    def construct(self):
        # This is a supplementary scene showing the deeper mathematical concepts
        title = Tex("The Mathematics Behind Prediction").to_edge(UP)
        
        # Show probability spaces
        probability_space = Circle(radius=2, color=WHITE)
        regions = VGroup(
            Sector(radius=2, angle=PI/3, color=RED, fill_opacity=0.3),
            Sector(radius=2, angle=PI/2, color=BLUE, fill_opacity=0.3).rotate(PI/3),
            Sector(radius=2, angle=PI/6, color=GREEN, fill_opacity=0.3).rotate(5*PI/6)
        )
        
        self.play(
            Create(probability_space),
            Create(regions)
        )
        
        # Transform into feature space
        feature_axes = ThreeDAxes()
        self.play(
            ReplacementTransform(probability_space, feature_axes),
            FadeOut(regions)
        )
        
        # Show decision boundaries
        decision_plane = Surface(
            lambda u, v: np.array([u, v, 0.5*u + 0.3*v]),
            u_range=[-2, 2],
            v_range=[-2, 2]
        )
        
        self.play(
            Create(decision_plane)
        )
        
        self.wait(2)