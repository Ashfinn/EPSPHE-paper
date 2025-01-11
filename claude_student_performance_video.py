from manim import *
import numpy as np
from sklearn.manifold import TSNE
from sklearn.preprocessing import StandardScaler
import pandas as pd

# Custom color scheme for consistent branding
class ColorScheme:
    PRIMARY = "#1f77b4"  # Deep blue
    SECONDARY = "#2ecc71"  # Emerald green
    ACCENT = "#f1c40f"  # Sunflower yellow
    WARNING = "#e74c3c"  # Soft red
    BACKGROUND = "#2c3e50"  # Dark slate
    
    @classmethod
    def get_gradient(cls, n_colors):
        return color_gradient([cls.PRIMARY, cls.SECONDARY], n_colors)

# Custom transition effects
class CustomTransitionScene(Scene):
    def transition_out(self):
        # Create hexagonal grid transition
        hexagons = VGroup(*[
            RegularPolygon(n=6, fill_opacity=1, color=ColorScheme.PRIMARY)
            .scale(0.5)
            for _ in range(20)
            for _ in range(15)
        ]).arrange_in_grid(20, 15, buff=0)
        
        self.play(
            *[Create(hex, run_time=0.05) for hex in hexagons],
            lag_ratio=0.05
        )
        return hexagons

    def transition_in(self, hexagons):
        self.play(
            *[Uncreate(hex, run_time=0.05) for hex in hexagons],
            lag_ratio=0.05
        )

class TSNEVisualization(CustomTransitionScene):
    def construct(self):
        # Generate sample student data
        np.random.seed(42)
        n_samples = 300
        
        # Generate synthetic student data
        features = {
            'grades': np.random.normal(70, 15, n_samples),
            'attendance': np.random.normal(85, 10, n_samples),
            'study_hours': np.random.normal(20, 5, n_samples),
            'participation': np.random.normal(75, 20, n_samples)
        }
        
        # Create DataFrame
        df = pd.DataFrame(features)
        
        # Standardize features
        scaler = StandardScaler()
        data_scaled = scaler.fit_transform(df)
        
        # Apply t-SNE
        tsne = TSNE(n_components=2, random_state=42)
        data_tsne = tsne.fit_transform(data_scaled)
        
        # Create visualization
        axes = Axes(
            x_range=[-30, 30],
            y_range=[-30, 30],
            axis_config={"stroke_color": GREY_A}
        )
        
        # Create dots with color gradient based on grades
        dots = VGroup(*[
            Dot(point=[x, y, 0], color=ColorScheme.get_gradient(n_samples)[i])
            for i, (x, y) in enumerate(data_tsne)
        ])
        
        # Add title and legend
        title = Text("Student Clustering Visualization", 
                    color=ColorScheme.PRIMARY).to_edge(UP)
        
        # Create interactive animation
        self.play(Create(axes), Write(title))
        self.play(LaggedStart(*[
            Create(dot) for dot in dots
        ], lag_ratio=0.05))
        
        # Animate clustering
        self.play(*[
            dot.animate.shift(
                0.3 * (np.array([x, y, 0]) - dot.get_center())
            )
            for dot, (x, y) in zip(dots, data_tsne)
        ], run_time=3)
        
        # Add interactive tooltip
        tooltip = Text("Hover to see student details",
                      font_size=24,
                      color=ColorScheme.ACCENT)
        self.play(Write(tooltip.to_edge(DOWN)))
        
        hexagons = self.transition_out()
        return hexagons

class MethodologyBreakdown(CustomTransitionScene):
    def construct(self):
        # Create flowchart with detailed steps
        steps = [
            "Data Collection",
            "Preprocessing",
            "Feature Engineering",
            "Model Training",
            "Validation",
            "Deployment"
        ]
        
        # Create complex flowchart with branching
        boxes = VGroup(*[
            RoundedRectangle(
                height=1,
                width=2,
                corner_radius=0.2
            ).set_fill(ColorScheme.PRIMARY, opacity=0.3)
            for _ in steps
        ])
        
        # Position boxes in a more complex arrangement
        boxes.arrange_in_grid(3, 2, buff=1.5)
        
        # Add labels with detailed explanations
        labels = VGroup(*[
            Text(step, font_size=24, color=WHITE)
            for step in steps
        ])
        
        # Position labels in boxes
        for box, label in zip(boxes, labels):
            label.move_to(box)
        
        # Create directed arrows showing process flow
        arrows = VGroup(*[
            CurvedArrow(
                start_point=boxes[i].get_right(),
                end_point=boxes[i+1].get_left(),
                angle=-TAU/4
            )
            for i in range(len(boxes)-1)
        ])
        
        # Add detailed explanations that appear on hover
        explanations = [
            "Collection of student records, test scores, and behavioral data",
            "Data cleaning, normalization, and handling missing values",
            "Creation of new features from existing data",
            "Training multiple ML models with cross-validation",
            "Testing model performance on held-out data",
            "Integration with educational systems"
        ]
        
        explanation_texts = VGroup(*[
            Text(exp, font_size=20, color=ColorScheme.ACCENT)
            .next_to(box, DOWN)
            for exp, box in zip(explanations, boxes)
        ])
        
        # Animate the methodology breakdown
        self.play(Create(boxes), run_time=2)
        self.play(Write(labels), run_time=2)
        self.play(Create(arrows), run_time=2)
        
        # Show explanations one by one
        for exp in explanation_texts:
            self.play(
                FadeIn(exp),
                run_time=1
            )
            self.wait(0.5)
            self.play(
                FadeOut(exp),
                run_time=0.5
            )
        
        hexagons = self.transition_out()
        return hexagons

class ResultsVisualization(CustomTransitionScene):
    def construct(self):
        # Create comparison chart of different ML models
        models = ["Random Forest", "SVM", "Neural Network", "Gradient Boost"]
        accuracies = [0.85, 0.82, 0.88, 0.87]
        
        # Create bar chart
        axes = Axes(
            x_range=[0, len(models)],
            y_range=[0, 1, 0.2],
            axis_config={"stroke_color": GREY_A},
            y_axis_config={"label_direction": LEFT}
        )
        
        # Create bars with gradient colors
        bars = VGroup(*[
            Rectangle(
                height=acc * 5,  # Scale for visibility
                width=0.5,
                fill_opacity=0.8,
                color=ColorScheme.get_gradient(len(models))[i]
            ).move_to(axes.c2p(i + 0.5, acc/2, 0))
            for i, acc in enumerate(accuracies)
        ])
        
        # Add labels
        labels = VGroup(*[
            Text(model, font_size=20, color=WHITE)
            .rotate(PI/4)  # Rotate for better readability
            .next_to(bar, DOWN)
            for model, bar in zip(models, bars)
        ])
        
        # Add accuracy values
        values = VGroup(*[
            Text(f"{acc*100:.1f}%", font_size=20, color=ColorScheme.ACCENT)
            .next_to(bar, UP)
            for acc, bar in zip(accuracies, bars)
        ])
        
        # Animate results
        self.play(Create(axes))
        self.play(LaggedStart(*[
            Create(bar) for bar in bars
        ], lag_ratio=0.2))
        self.play(Write(labels))
        self.play(Write(values))
        
        # Add interactive elements
        highlight = Rectangle(
            height=6,
            width=1,
            fill_opacity=0.3,
            color=ColorScheme.ACCENT
        )
        
        # Animate highlighting each model
        for bar in bars:
            highlight.move_to(bar)
            self.play(
                FadeIn(highlight),
                run_time=0.5
            )
            self.wait(0.5)
            self.play(
                FadeOut(highlight),
                run_time=0.5
            )
        
        hexagons = self.transition_out()
        return hexagons

class FutureEnhancements(CustomTransitionScene):
    def construct(self):
        # Create 3D scene with floating elements
        frame = self.camera.frame
        frame.set_euler_angles(theta=30*DEGREES, phi=60*DEGREES)
        
        # Create floating cubes representing future features
        features = [
            "Real-time Monitoring",
            "Personalized Learning",
            "Behavioral Analysis",
            "Social Network Integration",
            "Automated Interventions"
        ]
        
        cubes = VGroup(*[
            Cube(side_length=1)
            .set_fill(ColorScheme.get_gradient(len(features))[i], opacity=0.8)
            for i in range(len(features))
        ])
        
        # Position cubes in 3D space
        for i, cube in enumerate(cubes):
            cube.move_to([
                2 * np.cos(2*PI * i/len(features)),
                2 * np.sin(2*PI * i/len(features)),
                np.random.uniform(-1, 1)
            ])
        
        # Add labels to cubes
        labels = VGroup(*[
            Text(feature, font_size=24)
            .next_to(cube, OUT)
            for feature, cube in zip(features, cubes)
        ])
        
        # Animate future enhancements
        self.play(
            Create(cubes),
            Write(labels),
            frame.animate.increment_phi(-30*DEGREES),
            run_time=3
        )
        
        # Rotate scene
        self.play(
            frame.animate.increment_theta(360*DEGREES),
            run_time=8
        )
        
        hexagons = self.transition_out()
        return hexagons

class Conclusion(CustomTransitionScene):
    def construct(self):
        # Create final impact visualization
        impact_text = Text(
            "Transforming Education\nThrough Data",
            gradient=(ColorScheme.PRIMARY, ColorScheme.SECONDARY),
            font_size=48
        )
        
        # Create particle system
        particles = VGroup(*[
            Dot(radius=0.05, color=ColorScheme.get_gradient(50)[i])
            .move_to([
                3 * np.random.normal(),
                3 * np.random.normal(),
                0
            ])
            for i in range(50)
        ])
        
        # Animate particles converging to form final message
        self.play(FadeIn(particles))
        self.play(
            *[particle.animate.move_to(
                impact_text.get_center() + 
                [np.random.uniform(-0.5, 0.5) for _ in range(3)]
            )
              for particle in particles],
            run_time=2
        )
        
        self.play(
            FadeIn(impact_text),
            *[particle.animate.set_opacity(0) for particle in particles]
        )
        
        # Add final call to action
        cta = Text(
            "Join us in revolutionizing\neducational outcomes",
            color=ColorScheme.ACCENT,
            font_size=36
        ).next_to(impact_text, DOWN)
        
        self.play(Write(cta))
        
        self.wait(2)

if __name__ == "__main__":
    scenes = [
        TSNEVisualization(),
        MethodologyBreakdown(),
        ResultsVisualization(),
        FutureEnhancements(),
        Conclusion()
    ]
    
    for i, scene in enumerate(scenes[:-1]):
        hexagons = scene.construct()
        scenes[i+1].transition_in(hexagons)