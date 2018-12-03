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
import javafx.scene.control.ComboBox;
import javafx.geometry.Pos;
import javafx.scene.media.*;
import javafx.scene.media.MediaPlayer.*;

public class Demo extends Application{

    Scene scene;
    Stage stage;
    
    Pane pane1 = new Pane();
    Pane pane2 = new Pane();
    Pane pane3 = new Pane();
    Pane pane4 = new Pane();
    Pane mainPane = new Pane();
    Pane root = new Pane();

    Pane audioPane = new Pane();
    Pane videoPane = new Pane();

    Text t1, t2, t3, t4;
    Button b1, b2, b3, b4;

    MediaPlayer audioPlayer, videoPlayer;
    MediaView videoView;

    public void start(Stage stage) throws Exception {
        infoPages();
        root.getChildren().addAll(b1, b2, b3, b4, mainPane); 
        scene = new Scene(root, 700, 950, Color.GRAY);
        stage.setTitle("Homework 9");
        stage.setScene(scene);
        stage.show();
    }
    
    public void demoPage() {
        pane4.setPrefWidth(700);
        pane4.setPrefHeight(600);

        // Setting Audio Pane components
        File audioDirectory = new File("./audios");
        ComboBox<String> audioSelector = new ComboBox<String>();
        for (File file : audioDirectory.listFiles()) {
            audioSelector.getItems().add(file.getName());
        }
        audioSelector.getSelectionModel().selectFirst();
        audioSelector.relocate(275, 10);

        audioPlayer = new MediaPlayer(new Media(new File("audios/" + audioSelector.getValue()).toURI().toString()));
        
        audioSelector.setOnAction(action -> {
            audioPlayer.stop();
            audioPlayer = new MediaPlayer(new Media(new File("audios/" + audioSelector.getValue()).toURI().toString()));
        });

        ImageView playAudioImage = new ImageView("images/play.png");
        playAudioImage.setFitWidth(50);
        playAudioImage.setFitHeight(50);
        Button playAudio = new Button("Play / Resume", playAudioImage);
        playAudio.relocate(100, 100);

        playAudio.setOnMouseClicked(e -> {
            System.out.println(audioPlayer.getStatus());
            if (audioPlayer != null) {
                if (audioPlayer.getStatus() == Status.READY || audioPlayer.getStatus() == Status.PAUSED) {
                    audioPlayer.play();
                } else if (audioPlayer.getStatus() == Status.PLAYING) { 
                    // Hit play while either audio ended or still ongoing. Restarts audio.
                    audioPlayer.stop();
                    audioPlayer = new MediaPlayer(new Media(new File("audios/" + audioSelector.getValue()).toURI().toString()));
                    audioPlayer.play();
                }
            } 
        });

        ImageView pauseAudioImage = new ImageView("images/pause.png");
        pauseAudioImage.setFitWidth(50);
        pauseAudioImage.setFitHeight(50);
        Button pauseAudio = new Button("Pause", pauseAudioImage);
        pauseAudio.relocate(300, 100);

        pauseAudio.setOnMouseClicked(e -> {
            if (audioPlayer != null) {
                audioPlayer.pause();
            }
        });

        ImageView replayAudioImage = new ImageView("images/reverse.png");
        replayAudioImage.setFitWidth(50);
        replayAudioImage.setFitHeight(50);
        Button replayAudio = new Button("Replay", replayAudioImage);
        replayAudio.relocate(450, 100);

        replayAudio.setOnMouseClicked(e -> {
            if (audioPlayer != null) {
                audioPlayer.stop();
                audioPlayer = new MediaPlayer(new Media(new File("audios/" + audioSelector.getValue()).toURI().toString()));
                audioPlayber.play();
            }
        });

        audioPane.setPrefWidth(700);
        audioPane.setPrefHeight(200);

        // Setting Video Pane components
        File videoDirectory = new File("./videos");
        ComboBox<String> videoSelector = new ComboBox<String>();
        for (File file : videoDirectory.listFiles()) {
            videoSelector.getItems().add(file.getName());
        }
        videoSelector.getSelectionModel().selectFirst();
        videoSelector.relocate(275, 10);

        videoPlayer = new MediaPlayer(new Media(new File("videos/" + videoSelector.getValue()).toURI().toString()));
        
        videoSelector.setOnAction(action -> {
            videoPlayer.stop();
            videoPlayer = new MediaPlayer(new Media(new File("videos/" + videoSelector.getValue()).toURI().toString()));
            videoView.setMediaPlayer(videoPlayer);
        });

        ImageView playVideoImage = new ImageView("images/play.png");
        playVideoImage.setFitWidth(50);
        playVideoImage.setFitHeight(50);
        Button playVideo = new Button("Play / Resume", playVideoImage);
        playVideo.relocate(100, 400);

        playVideo.setOnMouseClicked(e -> {
            System.out.println(videoPlayer.getStatus());
            if (videoPlayer != null) {
                if (videoPlayer.getStatus() == Status.READY || videoPlayer.getStatus() == Status.PAUSED) {
                    videoPlayer.play();
                } else if (videoPlayer.getStatus() == Status.PLAYING) { 
                    // Hit play while either audio ended or still ongoing. Restarts audio.
                    videoPlayer.stop();
                    videoPlayer = new MediaPlayer(new Media(new File("videos/" + videoSelector.getValue()).toURI().toString()));
                    videoView.setMediaPlayer(videoPlayer);
                    videoPlayer.play();
                }
            } 
        });

        ImageView pauseVideoImage = new ImageView("images/pause.png");
        pauseVideoImage.setFitWidth(50);
        pauseVideoImage.setFitHeight(50);
        Button pauseVideo = new Button("Pause", pauseVideoImage);
        pauseVideo.relocate(300, 400);

        pauseVideo.setOnMouseClicked(e -> {
            if (videoPlayer != null) {
                videoPlayer.pause();
            }
        });

        ImageView replayVideoImage = new ImageView("images/reverse.png");
        replayVideoImage.setFitWidth(50);
        replayVideoImage.setFitHeight(50);
        Button replayVideo = new Button("Replay", replayVideoImage);
        replayVideo.relocate(450, 400);

        replayVideo.setOnMouseClicked(e -> {
            if (videoPlayer != null) {
                videoPlayer.stop();
                videoPlayer = new MediaPlayer(new Media(new File("videos/" + videoSelector.getValue()).toURI().toString()));
                videoView.setMediaPlayer(videoPlayer);
                videoPlayer.play();
            }
        });

        videoView = new MediaView(videoPlayer);
        videoView.setFitWidth(480); // 16 : 9 aspect ratio
        videoView.setFitHeight(270); // 16 : 9 aspect ratio
        videoView.relocate(100, 100);

        videoPane.relocate(0,300);
        videoPane.setPrefWidth(700);
        videoPane.setPrefHeight(500);

        // Setting Panes
        audioPane.getChildren().clear();
        audioPane.getChildren().addAll(audioSelector, playAudio, pauseAudio, replayAudio);

        videoPane.getChildren().clear();
        videoPane.getChildren().addAll(videoSelector, videoView, playVideo, pauseVideo, replayVideo);

        pane4.getChildren().clear();
        pane4.getChildren().addAll(audioPane, videoPane);

        mainPane.getChildren().clear();
        mainPane.getChildren().add(pane4);
    }

    public void infoPages() {
        t1 = new Text(10, 90, "Homework 9 \nAuthor: Ryan Stoughton \nEmail: rds6y9@mst.edu");
        t1.setFont(new Font(20));
        t1.setWrappingWidth(600);
        t1.setTextAlignment(TextAlignment.CENTER);
        
        t2 = new Text(0, 20, "Homework 9 should enable the user to play audio and video.");
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
        mainPane.relocate(0, 100); 

        ImageView authorImage = new ImageView("images/author.png");
        authorImage.setFitWidth(30);
        authorImage.setFitHeight(30);

        b1 = new Button("Author", authorImage);     

        ImageView descImage = new ImageView("images/description.png");
        descImage.setFitWidth(30);
        descImage.setFitHeight(30);

        b2 = new Button("Description", descImage);      

        ImageView problemImage = new ImageView("images/question.jpg");
        problemImage.setFitWidth(40);
        problemImage.setFitHeight(30);

        b3 = new Button("Problems", problemImage); 

        ImageView demoImage = new ImageView("images/play.png");
        demoImage.setFitWidth(30);
        demoImage.setFitHeight(30);

        b4 = new Button("Demo", demoImage);

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
            pane4.getChildren().clear();
            demoPage();
        });         
    }

    public static void main(String[] args) {
        Application.launch(args);
    }

}