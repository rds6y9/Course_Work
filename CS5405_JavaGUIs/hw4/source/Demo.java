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
    Button b1, b2, b3, b4;

    Circle c1, c2;

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
        int x1 = scanner.nextInt();
        int y1 = scanner.nextInt();
        int r1 = scanner.nextInt();
        int x2 = scanner.nextInt();
        int y2 = scanner.nextInt();
        int r2 = scanner.nextInt();
        scanner.close();

        c1 = new Circle();
        c1.setRadius(r1);
        c1.setCenterX(x1);
        c1.setCenterY(y1);
        c1.setFill(Color.RED);
        c1.setStroke(Color.BLUE);
        c1.setStrokeWidth(3);
        c2 = new Circle();
        c2.setRadius(r2);
        c2.setCenterX(x2);
        c2.setCenterY(y2);
        c2.setFill(Color.AQUA);
        c2.setStroke(Color.BLUE);
        c2.setStrokeWidth(3);

        t5 = new Text();
        t5.setX(0);
        t5.setY(20);
        t5.setFont(new Font(20));
        t5.setWrappingWidth(500);

        if (Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2)) > r1 + r2) {
            t5.setText("They are Disjoint");
        } else if (Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2)) == r1 + r2 ||
                   Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2)) == Math.abs(r1 - r2)) {
            t5.setText("They touch");
        } else if (Math.sqrt(Math.pow(x1 - x2, 2) + Math.pow(y1 - y2, 2)) < Math.abs(r1 - r2)) {
            t5.setText("One is inside the other");
        } else {
            t5.setText("They properly overlap");
        }
 

        pane1.getChildren().addAll(t1);        
        pane2.getChildren().addAll(t2,t3);        
        pane3.getChildren().addAll(t4);        
        pane4.getChildren().addAll(pane1);
        pane5.getChildren().addAll(c1, c2, t5);
    

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
    public static void main(String[] args){
        Application.launch(args);
    }
}