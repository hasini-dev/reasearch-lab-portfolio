'''
import cv2
import easyocr
import pyttsx3


# Load the image
image = cv2.imread("quote_text1.jpg")

# Convert to grayscale (optional, EasyOCR can handle color images)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])  # Specify language ('en' for English)

# Extract text from image
results = reader.readtext(gray, detail=0)  # detail=0 returns only text

# Join extracted text into a single string
extracted_text = " ".join(results)

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.say(extracted_text)
engine.runAndWait()

# Print the extracted text
print("Extracted Text:", extracted_text)
'''
import cv2
import easyocr
import pyttsx3
import time

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])  # Specify language ('en' for English')

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Attempt to open iVCam camera (Try indexes 0, 1, 2)
  # Try different indexes (0, 1, 2)
cap = cv2.VideoCapture(1)
if cap.isOpened():
    print(f"Connected to camera at index {1}")
else:
    print("Error: Could not open iVCam camera.")
    exit()

print("Processing live text... Press CTRL+C to stop.")

try:
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        
        if not ret:
            print("Error: Couldn't capture video frame.")
            break

        # Convert frame to grayscale for better OCR accuracy
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Extract text using EasyOCR
        results = reader.readtext(gray, detail=0)  # detail=0 returns only text

        # Join extracted text into a single string
        extracted_text = " ".join(results)

        # Print and speak the extracted text
        if extracted_text.strip():  # Avoid speaking empty text
            print("Extracted Text:", extracted_text)
            engine.say(extracted_text)
            engine.runAndWait()

        # Add a small delay to prevent excessive CPU usage
        time.sleep(0.5)

except KeyboardInterrupt:
    print("\nExiting program...")

# Release the camera
cap.release()