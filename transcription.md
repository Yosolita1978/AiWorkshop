# Workshop Transcript: Creating Social Media Avatars with Stable Diffusion

## Introduction

**Speaker:**  
You need to do when you are here on the workshop is create your own copy of this Workshop. You need to save this Workshop in your local Drive. Otherwise, you will not be able to install all the packages and create an image. So, here on the file menu, just go to save a copy in your drive.

## Setup and Configuration

**Speaker:**  
Once you have that copy, you can connect to the server from Google Colab here. On the right side of your screen, you will see the options for connection and you can change the runtime. By default, Google will give you this T4 GPU, which is fine, but it only has 16 gigabytes of memory, so I would recommend that you connect to a P100 GPU, which is faster. But this also depends on your budget because this one will cost you.

## Preparing Your Workspace

**Speaker:**  
You should create a folder that will have your photos. In this case, I decided that my handle for my photos will be a combination of my name. So I create a folder here, click with the mouse, and you create a new folder with my handle and I put all my photos there. Please notice that all the photos should be 512x512 pixels. It is important that the photos be this size; otherwise, the computer will not recognize the photo, and you will have an error.

## Running the Workshop

**Speaker:**  
Running this Workshop on Google Colab means that Google assigns you a space on a server that will run this code for you. You have the opportunity to learn code in the console or from Python 3. Anything in the code that you see with an exclamation point is running directly in the console of that server. The first two and three blocks of code have that exclamation point, meaning they are running in the console of the server.

## Using the Jupyter Colab Environment

**Speaker:**  
This Jupyter Colab Environment is very easy. You just need to click on the Play button beside the code. It will try to install these dependencies on that server space. You will see a result of everything and it will tell you if the process was successful or not. You don’t need to write any code. All the code that you need is there. You need to run it and be patient.

## Customizing Your Model

**Speaker:**  
There are three things that you need to change in order to run your own model. First, you need to change your handle. I'm using a combination of my name as my handle because it's pretty unique, but you need to change this. Then you need to specify the class of your model. In my case, it's a photo of a woman. You need to update this to match your handle.

## Training and Experimentation

**Speaker:**  
This is the moment that you can play with your model. Please don’t forget to start; all these steps will take a lot of time. In my case, it took almost 15 minutes to train my model. Be patient. Here is the part where you can play with your model. Use the handle that you decided. It will recognize you, and then you can just wait and see what Stable Diffusion will create with your prompts.
