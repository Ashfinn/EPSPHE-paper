from manim import *
import numpy as np


class IntroScene(Scene):
    def construct(self):
        # Modern title animation
        title = Text("Early Prediction of Student Performance", font_size=64, gradient=(YELLOW, BLUE))
        subtitle = Text("Using Machine Learning & Data Mining", font_size=36, color=GRAY)
        group = VGroup(title, subtitle).arrange(DOWN)

        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP), run_time=1.5)
        self.wait(2)

        # Transition to the next scene
        self.play(FadeOut(group))


class EducationalDataMining(Scene):
    def construct(self):
        title = Text("What is Educational Data Mining?", font_size=48, gradient=(BLUE, PURPLE))
        self.play(Write(title), run_time=2)
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Flowchart animation for EDM process
        flowchart = VGroup(
            Text("Raw Data").set_color(RED),
            Arrow(ORIGIN, RIGHT),
            Text("Preprocessing").set_color(GREEN),
            Arrow(ORIGIN, RIGHT),
            Text("Analysis").set_color(YELLOW),
            Arrow(ORIGIN, RIGHT),
            Text("Insights").set_color(BLUE),
        ).arrange(RIGHT, buff=0.8)

        self.play(Create(flowchart), run_time=2)

        # Example animation: Data points transforming into clusters
        points = VGroup(*[Dot(point=[np.random.uniform(-4, 4), np.random.uniform(-3, 3), 0], color=WHITE) for _ in range(20)])
        self.play(AnimationGroup(*[GrowFromCenter(p) for p in points], lag_ratio=0.1))
        self.wait(1)

        clusters = [Circle(radius=1.5, color=random_bright_color(), fill_opacity=0.3).move_to(points[i].get_center()) for i in [5, 10, 15]]
        self.play(AnimationGroup(*[Create(c) for c in clusters], lag_ratio=0.2))
        self.wait(2)


class PredictiveFramework(Scene):
    def construct(self):
        title = Text("Predictive Framework", font_size=48, gradient=(PURPLE, ORANGE))
        self.play(Write(title), run_time=2)
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # Neural network visualization
        layers = [3, 4, 4, 1]  # Number of neurons per layer
        nn = VGroup()
        for i, layer_size in enumerate(layers):
            layer = VGroup(*[Circle(radius=0.2, color=BLUE, fill_opacity=0.4) for _ in range(layer_size)])
            layer.arrange(DOWN, buff=0.5)
            nn.add(layer)

        nn.arrange(RIGHT, buff=1.5).shift(UP)
        self.play(FadeIn(nn, shift=DOWN), run_time=2)

        # Animate data flow through the neural network
        for layer in nn:
            self.play(layer.animate.set_fill(opacity=0.7), run_time=0.5)
        self.wait(1)

        # Transition to metrics
        metrics = VGroup(
            Text("Accuracy: 95%", font_size=32, color=GREEN),
            Text("Precision: 92%", font_size=32, color=YELLOW),
            Text("Recall: 90%", font_size=32, color=BLUE),
        ).arrange(DOWN, buff=0.5).shift(DOWN * 2)

        self.play(FadeIn(metrics, shift=UP), run_time=2)
        self.wait(2)


class ClusteringAndDimensionalityReduction(Scene):
    def construct(self):
        title = Text("Clustering & Dimensionality Reduction", font_size=48, gradient=(ORANGE, GREEN))
        self.play(Write(title), run_time=2)
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        # t-SNE visualization: Points dynamically clustering
        points = VGroup(*[Dot(point=[np.random.uniform(-4, 4), np.random.uniform(-3, 3), 0], color=WHITE) for _ in range(50)])
        self.play(AnimationGroup(*[GrowFromCenter(p) for p in points], lag_ratio=0.05), run_time=2)

        for i in range(10):
            cluster_center = [np.random.uniform(-3, 3), np.random.uniform(-2, 2), 0]
            cluster = Circle(radius=0.5, color=random_bright_color(), fill_opacity=0.3).move_to(cluster_center)
            self.play(Create(cluster), run_time=0.5)

        self.wait(2)


class Conclusion(Scene):
    def construct(self):
        title = Text("Conclusion", font_size=48, color=GREEN)
        self.play(Write(title), run_time=2)
        self.wait(1)

        points = VGroup(
            Text("1. Early predictions reduce failure rates.", font_size=36),
            Text("2. Machine learning improves prediction accuracy.", font_size=36),
            Text("3. Future work involves deep learning.", font_size=36),
        ).arrange(DOWN, buff=0.5)

        self.play(FadeIn(points, shift=UP), run_time=2)
        self.wait(3)
