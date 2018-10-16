package code; 

import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.layout.Pane;
import javafx.scene.control.Button;
import java.io.File;
import java.util.Scanner;
import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.paint.Color;
import javafx.scene.shape.Circle;
import javafx.scene.text.*;
import javafx.scene.input.KeyCode;
import javafx.scene.control.TextField;

public class Demo extends Application{
    Pane pane1 = new Pane();
    Pane pane2 = new Pane();
    Pane pane3 = new Pane();
    Pane pane4 = new Pane();
    Pane pane5 = new Pane();
    Pane root = new Pane();

    Scene scene;
    Stage stage;

    Text t1, t2, t3, t4, t5;
    TextField tf1;
    Button b1, b2, b3, b4;

    Circle c1, c2;

    int x1, x2, y1, y2, r1, r2;

    double dist;

    public void start(Stage stage) throws Exception {
        //root.getChildren().addAll.(pane1, button1, b2, button3,)
        root = homePage();
        scene = new Scene(root,700,600,Color.GRAY);
        stage.setTitle("Homework 4");
        stage.setScene(scene);
        stage.show();
    }
    

    public Pane homePage() throws Exception {
        t1 = new Text(10,90, "Author Text");
        t1.setText("Homework 4 \nAuthor: Ryan Stoughton \nEmail: rds6y9@mst.edu");
        t1.setFont(new Font(20));
        t1.setWrappingWidth(600);
        t1.setTextAlignment(TextAlignment.CENTER);

        // t5 = new Text(10,100, "Another Test Text \n asdadsdasdasd \n asdasdd");
        // t6 = new Text(10, 180, "\nLink: url address for reference to specific page and quotation");
        
        t2 = new Text(0, 20, "Description Text");
        t2.setFont(new Font(20));              
        t2.setWrappingWidth(500);               
        t2.setText("Homework 4 should contain a four buttons.");
        
        t3 = new Text(20,40, "Description of Description");
        t3.setFont(new Font(15));
        t3.setWrappingWidth(600);
        t3.setText("The Author button should have the author name and email. \nThe Description button should contain problem description \nThe Problems button should list any problems encountered \nThe Demo button should provide a demo of Circles");        
        

        t4 = new Text(0, 20, "I had no issues with this assignment.");
        t4.setFont(new Font(20));
        t4.setWrappingWidth(600);    
        
        File file = new File("data/inFile.txt");
        Scanner scanner = new Scanner(file);
        x1 = scanner.nextInt();
        y1 = scanner.nextInt();
        r1 = scanner.nextInt();
        x2 = scanner.nextInt();
        y2 = scanner.nextInt();
        r2 = scanner.nextInt();
        scanner.close();

        c1 = new Circle();
        c1.setRadius(r1);
        c1.setCenterX(x1);
        c1.setCenterY(y1);
        c1.setFill(new Color(0,0,0,0));
        c1.setStroke(Color.RED);
        c1.setStrokeWidth(3);
        c2 = new Circle();
        c2.setRadius(r2);
        c2.setCenterX(x2);
        c2.setCenterY(y2);
        c2.setFill(new Color(0,0,0,0));
        c2.setStroke(Color.BLUE);
        c2.setStrokeWidth(3);

        t5 = new Text();
        t5.setX(300);
        t5.setY(20);
        t5.setFont(new Font(20));
        t5.setWrappingWidth(500);

        tf1 = new TextField("20 30 40 50 60 70");
        tf1.setFont(new Font(20));

        tf1.setOnKeyPressed(e -> {
            if (e.getCode() == KeyCode.ENTER) {
                UpdateCircles();
            }
        });
        
        dist = Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));

        if (r1 == r2 && dist == 0) {
            t5.setText("The circles are the same");
        } else if (dist > r1 + r2) {
            t5.setText("The circles do not touch");
        } else if (dist == r1 + r2) {
            t5.setText("The circles touch externally");
        } else if (dist < r2 - r1) {
            t5.setText("Circle 1 inside Circle 2 does not touch");
        } else if (dist == r2 - r1) {
            t5.setText("Circle 1 inside Circle 2 does touch");
        } else if (dist < r1 - r2) {
            t5.setText("Circle 2 inside Circle 1 does not touch");
        } else if (dist == r1 - r2) {
            t5.setText("Circle 2 inside Circle 1 does touch");
        } else {
            t5.setText("Circle 1 and Circle 2 have proper overlap");
        }
 
        pane1.getChildren().addAll(t1);        
        pane2.getChildren().addAll(t2,t3);        
        pane3.getChildren().addAll(t4);        
        pane4.getChildren().addAll(pane1);
        pane5.getChildren().addAll(c1, c2, t5, tf1);
        
        pane1.relocate(10,50);        
        pane2.relocate(10,50);        
        pane3.relocate(10,50);
        pane4.relocate(10,100);        
        b1 = new Button("Author");        
        b2 = new Button("Description");        
        b3 = new Button("Problems"); 
        b4 = new Button("Demo");       
        b1.relocate(100,20);        
        b2.relocate(250,20);        
        b3.relocate(400,20);
        b4.relocate(550,20);

        root.getChildren().addAll(b1, b2, b3, b4, pane4);        
        b1.setOnAction(ae->{pane4.getChildren().clear();pane4.getChildren().add(pane1);});        
        b2.setOnAction(ae->{pane4.getChildren().clear();pane4.getChildren().add(pane2);});        
        b3.setOnAction(ae->{pane4.getChildren().clear();pane4.getChildren().add(pane3);});
        b4.setOnAction(ae->{pane4.getChildren().clear();pane4.getChildren().add(pane5);});        
        
        return root; 
    }

    public void UpdateCircles() {
        String[] tokens = tf1.getText().split(" ");

        x1 = Integer.parseInt(tokens[0]);
        y1 = Integer.parseInt(tokens[1]);
        r1 = Integer.parseInt(tokens[2]);
        x2 = Integer.parseInt(tokens[3]);
        y2 = Integer.parseInt(tokens[4]);
        r2 = Integer.parseInt(tokens[5]);

        c1.setRadius(r1);
        c1.setCenterX(x1);
        c1.setCenterY(y1);

        c2.setRadius(r2);
        c2.setCenterX(x2);
        c2.setCenterY(y2);

        dist = Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2));

        if (r1 == r2 && dist == 0) {
            t5.setText("The circles are the same");
        } else if (dist > r1 + r2) {
            t5.setText("The circles do not touch");
        } else if (dist == r1 + r2) {
            t5.setText("The circles touch externally");
        } else if (dist < r2 - r1) {
            t5.setText("Circle 1 inside Circle 2 does not touch");
        } else if (dist == r2 - r1) {
            t5.setText("Circle 1 inside Circle 2 does touch");
        } else if (dist < r1 - r2) {
            t5.setText("Circle 2 inside Circle 1 does not touch");
        } else if (dist == r1 - r2) {
            t5.setText("Circle 2 inside Circle 1 does touch");
        } else {
            t5.setText("Circle 1 and Circle 2 have proper overlap");
        }
    }

    public static void main(String[] args){
        Application.launch(args);
    }
}