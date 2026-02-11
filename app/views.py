import os
import cv2
import numpy as np
import pytesseract
from flask import render_template, request, jsonify
from werkzeug.utils import secure_filename
from app import app
import base64

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def get_grayscale(image):
    """Convert image to grayscale"""
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def remove_noise(image):
    """Remove noise using median blur"""
    return cv2.medianBlur(image, 5)

def thresholding(image):
    """Apply thresholding to image"""
    return cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

def deskew(image):
    """Correct image skew"""
    coords = np.column_stack(np.where(image > 0))
    angle = cv2.minAreaRect(coords)[-1]
    
    if angle < -45:
        angle = -(90 + angle)
    else:
        angle = -angle
    
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)
    
    M = cv2.getRotationMatrix2D(center, angle, 1.0)
    rotated = cv2.warpAffine(
        image,
        M,
        (w, h),
        flags=cv2.INTER_CUBIC,
        borderMode=cv2.BORDER_REPLICATE
    )
    return rotated

def preprocess_image(image):
    """Apply all preprocessing steps to image"""
    # Convert to grayscale
    gray = get_grayscale(image)
    
    # Remove noise
    denoised = remove_noise(gray)
    
    # Apply thresholding
    thresh = thresholding(denoised)
    
    # Deskew
    deskewed = deskew(thresh)
    
    return deskewed

def extract_text_from_image(image_path):
    """Extract text from image using Tesseract OCR"""
    try:
        # Read image
        image = cv2.imread(image_path)
        
        if image is None:
            return "Error: Could not read image"
        
        # Preprocess image
        processed_image = preprocess_image(image)
        
        # Extract text using Tesseract
        custom_config = r'--oem 3 --psm 6'
        text = pytesseract.image_to_string(processed_image, config=custom_config)
        
        # Clean up text - remove special characters using translation table for efficiency
        characters_to_remove = "!@#$%^*()+-;/[]{}&^~_`"
        translation_table = str.maketrans('', '', characters_to_remove)
        cleaned_text = text.translate(translation_table)
        
        return cleaned_text.strip() if cleaned_text.strip() else "No text detected in image"
        
    except Exception as e:
        return f"Error processing image: {str(e)}"

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/extract', methods=['POST'])
def extract():
    """Handle image upload and text extraction"""
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
    
    file = request.files['image']
    
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        # Save file securely
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # Extract text
        extracted_text = extract_text_from_image(filepath)
        
        # Read image and convert to base64 for preview
        with open(filepath, 'rb') as img_file:
            img_data = base64.b64encode(img_file.read()).decode('utf-8')
        
        # Clean up - remove uploaded file
        os.remove(filepath)
        
        return jsonify({
            'text': extracted_text,
            'image': img_data
        })
    
    return jsonify({'error': 'Invalid file type'}), 400
