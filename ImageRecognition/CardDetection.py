import torch
import numpy as np
import cv2
from time import time


class ObjectDetection:
    """
    Class implements Yolo5 model to make inferences on a youtube video using Opencv2.
    """

    def __init__(self, capture_index, model_name):
        """ 
        Initializes the class with youtube url and output file.
        :param url: Has to be as youtube URL,on which prediction is made.
        :param out_file: A valid output file name.
        """
        self.capture_index = capture_index
        self.model = self.load_model(model_name)
        self.classes = self.model.names
        self.device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print("Using Device: ", self.device)

    def get_video_capture(self):
        """
        Creates a new video streaming object to extract video frame by frame to make prediction on.
        :return: opencv2 video capture object, with lowest quality frame available for video.
        """
      
        return cv2.VideoCapture(self.capture_index)

    def load_model(self, model_name):
        """
        Loads Yolo5 model from pytorch hub.
        :return: Trained Pytorch model.
        """
        if model_name:
            model = torch.hub.load('C:/Users/KrzyS/yolov5', 'custom', path='C:/Users/KrzyS/yolov5/best.pt', source='local')
        else:
            model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
        return model

    def score_frame(self, frame):
        """
        Takes a single frame as input, and scores the frame using yolo5 model.
        :param frame: input frame in numpy/list/tuple format.
        :return: Labels and Coordinates of objects detected by model in the frame.
        """
        self.model.to(self.device)
        frame = [frame]
        results = self.model(frame)
        labels, cord = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        return labels, cord

    def class_to_label(self, x):
        """
        For a given label value, return corresponding string label.
        :param x: numeric label
        :return: corresponding string label
        
        def string_lable(a):
            switcher = {
        0:"AS",1:"AC",2:"AD",3:"AH",
        4:"2S",5:"2C",6:"2D",7:"2H",        
        8:"3S",9:"3C",10:"3D",11:"3H",
        12:"4S",13:"4C",14:"4D",15:"4H",
        16:"5S",17:"5C",18:"5D",19:"5H",
        20:"6S",21:"6C",22:"6D",23:"6H",
        24:"7S",25:"7C",26:"7D",27:"7H",
        28:"8S",29:"8C",30:"8D",31:"8H",
        32:"9S",33:"9C",34:"9D",35:"9H",
        36:"10S",37:"10C",38:"10D",39:"10H",
        40:"JS",41:"JC",42:"JD",43:"JH",
        44:"QS",45:"QC",46:"QD",47:"QH",
        48:"KS",49:"KC",50:"KD",51:"KH",
        52:'JOKER'   
        }
            return switcher.get(a, 'nothing')
        return string_lable(int(x))
            """
        
        return self.classes[int(x)]

    def plot_boxes(self, results, frame):
        """
        Takes a frame and its results as input, and plots the bounding boxes and label on to the frame.
        :param results: contains labels and coordinates predicted by model on the given frame.
        :param frame: Frame which has been scored.
        :return: Frame with bounding boxes and labels ploted on it.
        """
        labels, cord = results
        n = len(labels)
        x_shape, y_shape = frame.shape[1], frame.shape[0]
        for i in range(n):
            row = cord[i]
            if row[4] >= 0.01:
                x1, y1, x2, y2 = int(row[0]*x_shape), int(row[1]*y_shape), int(row[2]*x_shape), int(row[3]*y_shape)
                bgr = (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), bgr, 2)
                cv2.putText(frame, self.class_to_label(labels[i]), (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 0.9, bgr, 2)

        return frame

    def __call__(self):
        """
        This function is called when class is executed, it runs the loop to read the video frame by frame,
        and write the output into a new file.
        :return: void
        """
        cap = self.get_video_capture()
        assert cap.isOpened()
      
        while True:
          
            start_time = time()
            
            ret, frame = cap.read()
            assert ret
            
            # Convert BGR to HSV
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
            #lower red
            lower_red = np.array([0,50,50])
            upper_red = np.array([10,255,255])

            #upper red
            lower_red2 = np.array([170,50,50])
            upper_red2 = np.array([180,255,255])

            mask = cv2.inRange(hsv, lower_red, upper_red)
            res = cv2.bitwise_and(frame,frame, mask= mask)

            mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
            res2 = cv2.bitwise_and(frame,frame, mask= mask2)

            #Black mask
            lower_black = np.array([0,0,0])
            upper_black = np.array([179, 90, 90])

            mask3 = cv2.inRange(hsv, lower_black, upper_black)
            res3 = cv2.bitwise_and(frame, frame, mask = mask3)
    
            img4 = cv2.add(mask,mask2)
            img5 = cv2.add(img4, mask3)
            
            results = self.score_frame(img5)
            frame = self.plot_boxes(results, frame)
            
            end_time = time()
            fps = 1/np.round(end_time - start_time, 2)
            #print(f"Frames Per Second : {fps}")
             
            cv2.putText(frame, f'FPS: {int(fps)}', (20,70), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0,255,0), 2)
            
            cv2.imshow('Black%White', img5)
            cv2.imshow('YOLOv5 Detection', frame)
 
            if cv2.waitKey(3) & 0xFF == 27:
                break
      
        cap.release()
        
        
# Create a new object and execute.
detector = ObjectDetection(capture_index=0, model_name=True)
detector()
