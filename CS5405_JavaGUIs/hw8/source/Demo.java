package code; 

import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.control.Label;
import javafx.scene.control.Button;
import javafx.animation.RotateTransition;
import javafx.scene.control.Slider;
import javafx.animation.Animation;
import java.io.File;
import java.util.Scanner;
import javafx.util.Duration;
import javafx.application.Application;
import javafx.scene.shape.Arc;
import javafx.scene.shape.ArcType;
import javafx.geometry.Orientation;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.scene.text.*;
import javafx.scene.image.ImageView;
import javafx.scene.input.KeyCode;
import javafx.scene.control.TextField;
import javafx.scene.shape.Path;
import javafx.scene.input.MouseEvent;
import javafx.scene.shape.LineTo;
import javafx.scene.shape.MoveTo;
import javafx.scene.shape.Polyline;
import javafx.scene.shape.Line;
import javafx.scene.image.ImageView;

public class Demo extends Application{

    Scene scene;
    Stage stage;
    
    Pane pane1 = new Pane();
    Pane pane2 = new Pane();
    Pane pane3 = new Pane();
    Pane pane4 = new Pane();
    Pane mainPane = new Pane();
    Pane root = new Pane();

    Text t1, t2, t3, t4;
    Button b1, b2, b3, b4;

    //////// Demo Pane Stuff //////////

    // Pane for Buttons and blade count
    Pane subpane1 = new Pane();
    // Pane that contains the fan
    Pane subpane2 = new Pane();
    // Pane that contains the fan speed
    Pane subpane3 = new Pane();

    Circle circle1, circle2, circle3;
    int bladeCount;
    int fanSpeed;
    Slider blades, speed;

    Button pauseButton, playButton, reverseButton;
    RotateTransition fanAnimation;
    int animationDirection = 360; // 360 degrees means full rotation, can be negated to spin backwards
    boolean isRunning = false;

    public void start(Stage stage) throws Exception {
        infoPages();
        root.getChildren().addAll(b1, b2, b3, b4, mainPane); 
        scene = new Scene(root, 700, 600, Color.GRAY);
        stage.setTitle("Homework 8");
        stage.setScene(scene);
        stage.show();
    }
    
    public void demoPage() {
        pane4.setPrefWidth(700);
        pane4.setPrefHeight(600);

        subpane1.setPrefHeight(100);
        subpane1.setPrefWidth(700);

        ImageView playview = new ImageView("images/play.png");
        playview.setFitWidth(100);
        playview.setFitHeight(100);
        playButton = new Button("", playview);

        ImageView pauseview = new ImageView("images/pause.png");
        pauseview.setFitWidth(100);
        pauseview.setFitHeight(100);
        pauseButton = new Button("", pauseview);
        pauseButton.relocate(110,0);

        ImageView reverseview = new ImageView("images/reverse.png");
        reverseview.setFitWidth(100);
        reverseview.setFitHeight(100);
        reverseButton = new Button("", reverseview);
        reverseButton.relocate(220,0);

        Label speedLabel = new Label("Fan Speed");
        speedLabel.setFont(new Font(20));
        speedLabel.relocate(350, 0);

        speed = new Slider(1,10,0);
        speed.setOrientation(Orientation.HORIZONTAL);
        speed.relocate(350,50);
        speed.setMajorTickUnit(1);
        speed.setMinorTickCount(0);
        speed.setSnapToTicks(true);
        speed.setShowTickLabels(true);
        speed.setShowTickMarks(true);
        speed.valueProperty().addListener(action -> {
            setFanSpeed();
        });

        playButton.setOnAction(action -> {
            if (isRunning) {
                fanAnimation.stop();
                isRunning = false;
            } else {
                fanAnimation.play();
                isRunning = true;
            }
            
        });

        pauseButton.setOnAction(action -> {
            fanAnimation.stop();
            isRunning = false;
        });

        reverseButton.setOnAction(action -> {
            fanAnimation.stop();
            animationDirection = -animationDirection;
            fanAnimation.setByAngle(animationDirection);
            fanAnimation.play();
        });

        subpane1.getChildren().addAll(playButton, pauseButton, reverseButton, speedLabel, speed);

        subpane2.relocate(0,100);
        subpane2.setPrefHeight(300);
        subpane2.setPrefWidth(700);
        subpane2.setPickOnBounds(false);

        subpane3.relocate(0,400);
        subpane3.setPrefHeight(100);
        subpane3.setPrefWidth(700);

        Label bladesLabel = new Label("Blade Count");
        bladesLabel.setFont(new Font(20));
        bladesLabel.relocate(20, 10);

        blades = new Slider(3,10,0);
        blades.setOrientation(Orientation.HORIZONTAL);
        blades.setMajorTickUnit(1);
        blades.setMinorTickCount(0);
        blades.setSnapToTicks(true);
        blades.setShowTickLabels(true);
        blades.setShowTickMarks(true);
        blades.relocate(10, 50);
        blades.valueProperty().addListener(action -> {
            subpane2.getChildren().clear();
            drawNewFan();
        });
        
        // Setting transition on the entire fan pane
        setFanSpeed();
        drawNewFan();

        subpane3.getChildren().addAll(bladesLabel, blades);
        pane4.getChildren().addAll(subpane1, subpane2, subpane3);

        mainPane.getChildren().clear();
        mainPane.getChildren().add(pane4);
    }

    public void setFanSpeed() {
        if (fanAnimation != null) {
            fanAnimation.stop();
        } 
        fanAnimation = new RotateTransition(Duration.seconds(11 - (int) speed.getValue()), subpane2);
        fanAnimation.setByAngle(animationDirection);
        fanAnimation.setCycleCount(Animation.INDEFINITE);
        fanAnimation.play();
    }

    public void drawNewFan() {
        circle1 = new Circle();
        circle1.setCenterX(350);
        circle1.setCenterY(150);
        circle1.setRadius(100);
        circle1.setFill(new Color(0,0,0,0));
        circle1.setStroke(Color.FUCHSIA);
        circle1.setStrokeWidth(3);

        circle2 = new Circle();
        circle2.setCenterX(350);
        circle2.setCenterY(150);
        circle2.setRadius(70);
        circle2.setFill(Color.PINK);
        circle2.setStroke(Color.FUCHSIA);
        circle2.setStrokeWidth(3);

        circle3 = new Circle();
        circle3.setCenterX(350);
        circle3.setCenterY(150);
        circle3.setRadius(50);
        circle3.setFill(Color.BLUE);
        circle3.setStroke(Color.FUCHSIA);
        circle3.setStrokeWidth(3);

        for (int i = 0; i < (int)blades.getValue(); i++) {
            int degreeOffset = (360 / (int)blades.getValue()) * i;
            Arc arc = new Arc(350, 150, 150, 150, degreeOffset, 25);
            arc.setType(ArcType.ROUND);
            arc.setFill(Color.BLUEVIOLET);
            subpane2.getChildren().add(arc);
        }

        subpane2.getChildren().addAll(circle1, circle2, circle3);
    }

    public void infoPages() {
        t1 = new Text(10, 90, "Homework 8 \nAuthor: Ryan Stoughton \nEmail: rds6y9@mst.edu");
        t1.setFont(new Font(20));
        t1.setWrappingWidth(600);
        t1.setTextAlignment(TextAlignment.CENTER);
        
        t2 = new Text(0, 20, "Homework 8 should enable the user to manipulate a fan's animation using controls.");
        t2.setFont(new Font(20));              
        t2.setWrappingWidth(700);               
        
        t3 = new Text(20,80, "The Author button should have the author name and email. \nThe Description button should contain problem description \nThe Problems button should list any problems encountered \nThe Demo button should provide a line drawing demo.");
        t3.setFont(new Font(15));
        t3.setWrappingWidth(600);
        
        t4 = new Text(0, 20, "The only references were from class.");
        t4.setFont(new Font(20));
        t4.setWrappingWidth(600);   
        
        pane1.getChildren().addAll(t1);        
        pane2.getChildren().addAll(t2,t3);        
        pane3.getChildren().addAll(t4);

        mainPane.getChildren().addAll(pane1);
        
        pane1.relocate(10, 50);        
        pane2.relocate(10, 50);        
        pane3.relocate(10, 50);
        mainPane.relocate(0, 50); 

        b1 = new Button("Author");        
        b2 = new Button("Description");        
        b3 = new Button("Problems"); 
        b4 = new Button("Demo");

        b1.relocate(100,20);        
        b2.relocate(250,20);        
        b3.relocate(400,20);
        b4.relocate(550,20);
       
        b1.setOnAction(ae->{
            mainPane.getChildren().clear();
            mainPane.getChildren().add(pane1);
        });        
        
        b2.setOnAction(ae->{
            mainPane.getChildren().clear();
            mainPane.getChildren().add(pane2);
        });        
        
        b3.setOnAction(ae->{
            mainPane.getChildren().clear();
            mainPane.getChildren().add(pane3);
        });

        b4.setOnAction(ae->{
            subpane1.getChildren().clear();
            subpane2.getChildren().clear();
            subpane3.getChildren().clear();
            pane4.getChildren().clear();
            demoPage();
        });         
    }

    public static void main(String[] args) {
        Application.launch(args);
    }

}