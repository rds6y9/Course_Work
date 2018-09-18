/*
    Programmer: Ryan Stoughton
    Class: Java GUI's 
    Assignment: Homework 2
*/

package code;

import javafx.application.Application;
import javafx.scene.Group;
import javafx.scene.control.Label;
import javafx.scene.Scene;
import javafx.stage.Stage;

public class Demo extends Application {
    public void start(Stage stage) {
        Label label = new Label("Ryan Stoughton");
        Group root = new Group(label);
        Scene scene = new Scene(root, 400, 300);

        stage.setScene(scene);
        stage.show();
    }
}