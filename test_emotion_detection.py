import unittest
from EmotionDetection import emotion_detector


class EmotionTest(unittest.TestCase):
    def test_joy(self):
        result=emotion_detector("I am glad this happened")
        max_rez=0;
        max_emotion=None
        for emotion,value in result.items():
            if(value>max_rez):
                max_rez=value
                max_emotion=emotion
        self.assertEqual(max_emotion,"joy")

    def test_anger(self):
        result=emotion_detector("I am really mad about this")
        max_rez=0;
        max_emotion=None
        for emotion,value in result.items():
            if(value>max_rez):
                max_rez=value
                max_emotion=emotion
        self.assertEqual(max_emotion,"anger")

    def test_disgust(self):
        result=emotion_detector("I feel disgusted just hearing about this")
        max_rez=0;
        max_emotion=None
        for emotion,value in result.items():
            if(value>max_rez):
                max_rez=value
                max_emotion=emotion
        self.assertEqual(max_emotion,"disgust")

    def test_sadness(self):
        result=emotion_detector("I am so sad about this")
        max_rez=0;
        max_emotion=None
        for emotion,value in result.items():
            if(value>max_rez):
                max_rez=value
                max_emotion=emotion
        self.assertEqual(max_emotion,"sadness")

    def test_fear(self):
        result=emotion_detector("I am really afraid that this will happen")
        max_rez=0;
        max_emotion=None
        for emotion,value in result.items():
            if(value>max_rez):
                max_rez=value
                max_emotion=emotion
        self.assertEqual(max_emotion,"fear")

if __name__=="__main__":
    unittest.main()       
    
