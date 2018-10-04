/*
    Programmer: Ryan Stoughton
    Class: Java GUI's 
    Assignment: Homework 3
*/

package code;

import java.io.File;
import java.util.Scanner;

import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.control.Label;
import javafx.scene.layout.StackPane;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.lang.Math;

public class Circles extends Application {

    public void start(Stage stage) throws Exception {
        // READ IN DIMENSIONS
        File file = new File("C:\\Users\\Ryan\\Documents\\Course_Work\\CS5405_JavaGUIs\\hw3\\inFile.txt");
        Scanner scanner = new Scanner(file);
        int x1 = scanner.nextInt();
        int y1 = scanner.nextInt();
        int r1 = scanner.nextInt();
        int x2 = scanner.nextInt();
        int y2 = scanner.nextInt();
        int r2 = scanner.nextInt();
        scanner.close();

        // DETERMINE INTERSECTION
        Label label = new Label();
        if (Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2)) > r1 + r2) {
            label.setText("They are Disjoint");
        } else if (Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2)) == r1 + r2 || 
                   Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2)) == Math.abs(r1 - r2)) {
            label.setText("They touch");
        } else if (Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2)) < Math.abs(r1 - r2)) {
            label.setText("One is inside the other");
        } else {
            label.setText("They properly overlap");
        }
        
        // SET CIRCLES
        Circle circle1 = new Circle();
        circle1.setCenterX(x1);
        circle1.setCenterY(y1);
        circle1.setRadius(r1);
        circle1.setFill(Color.RED);
        circle1.setStroke(Color.BLUE);
        circle1.setStrokeWidth(3);

        Circle circle2 = new Circle();
        circle2.setCenterX(x2);
        circle2.setCenterY(y2);
        circle2.setRadius(r2);
        circle2.setFill(Color.AQUA);
        circle2.setStroke(Color.BLUE);
        circle2.setStrokeWidth(3);

        // DISPLAY CONTENT
        Group root = new Group();
        root.getChildren().addAll(label, circle1, circle2);

        Scene scene = new Scene(root, 400, 300);
        stage.setScene(scene);
        stage.show();

        System.out.println("In case it is covered, the label reads: " + label.getText());
    }

}