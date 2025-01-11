from manim import *
import numpy as np


class IntroScene(Scene):
    def construct(self):
        title = Text("Predicting Student Performance", font_size=60, color=YELLOW)
        subtitle = Text("Using Data Mining & Machine Learning", font_size=36, color=BLUE)
        group = VGroup(title, subtitle).arrange(DOWN)
        self.play(Write(group))
        self.wait(2)
        self.play(FadeOut(group))


class EducationalDataMining(Scene):
    def construct(self):
        title = Text("Educational Data Mining", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        flowchart = VGroup(
            Text("Raw Data").scale(0.6).set_color(RED),
            Arrow(ORIGIN, RIGHT),
            Text("Preprocessing").scale(0.6).set_color(GREEN),
            Arrow(ORIGIN, RIGHT),
            Text("Analysis").scale(0.6).set_color(YELLOW),
            Arrow(ORIGIN, RIGHT),
            Text("Insights").scale(0.6).set_color(BLUE),
        ).arrange(RIGHT, buff=0.5)

        self.play(Create(flowchart))
        self.wait(2)


class PredictiveFramework(Scene):
    def construct(self):
        title = Text("Predictive Framework", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        inputs = VGroup(
            Text("Admission Scores").scale(0.5),
            Text("Course Grades").scale(0.5),
            Text("AAT/GAT Scores").scale(0.5),
        ).arrange(DOWN, buff=0.5)

        outputs = VGroup(
            Text("Predicted GPA").scale(0.5),
            Text("Risk Level").scale(0.5),
        ).arrange(DOWN, buff=0.5)

        framework = VGroup(
            inputs,
            Arrow(ORIGIN, RIGHT),
            Text("Machine Learning").scale(0.6).set_color(YELLOW),
            Arrow(ORIGIN, RIGHT),
            outputs,
        ).arrange(RIGHT, buff=1)

        self.play(Create(framework))
        self.wait(3)


class Methodology(Scene):
    def construct(self):
        title = Text("Methodology", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        clustering = Text("t-SNE Clustering", font_size=36).shift(LEFT * 3)
        classification = Text("Classification Models", font_size=36).shift(RIGHT * 3)
        arrow = Arrow(LEFT, RIGHT).scale(1.5)

        self.play(Write(clustering), Write(classification), Create(arrow))
        self.wait(2)


class Results(Scene):
    def construct(self):
        title = Text("Results & Discussion", font_size=48)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        axes = Axes(x_range=[0, 10, 1], y_range=[0, 1, 0.1], x_length=7, y_length=5)
        labels = axes.get_axis_labels("Model", "Accuracy")
        graph = axes.plot(lambda x: 0.6 + 0.3 * np.exp(-0.2 * x), x_range=[0, 10], color=BLUE)

        self.play(Create(axes), Write(labels))
        self.play(Create(graph))
        self.wait(2)


class Conclusion(Scene):
    def construct(self):
        title = Text("Conclusion", font_size=48, color=GREEN)
        self.play(Write(title))
        self.wait(1)
        self.play(title.animate.to_edge(UP))

        points = VGroup(
            Text("1. Early predictions reduce failure rates.", font_size=36),
            Text("2. Machine learning improves prediction accuracy.", font_size=36),
            Text("3. Future work involves deep learning.", font_size=36),
        ).arrange(DOWN, buff=0.5)

        self.play(Create(points))
        self.wait(3)
