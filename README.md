# Optical Character Recognition Web Application

A Flask-based web application that performs Optical Character Recognition (OCR) on uploaded images using Tesseract and OpenCV. The application features advanced image preprocessing techniques including grayscale conversion, noise removal, thresholding, and deskewing to improve text extraction accuracy.

## Features

- **User-Friendly Web Interface**: Clean and intuitive UI for uploading images and viewing extracted text
- **Advanced Image Preprocessing**:
  - Grayscale conversion
  - Noise removal using median blur
  - Adaptive thresholding
  - Automatic deskew correction
- **Real-time Image Preview**: See your uploaded image before processing
- **Instant Text Extraction**: Extract text from images with a single click
- **Support for Multiple Image Formats**: PNG, JPG, JPEG, GIF, BMP, TIFF

## Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.7 or higher
- Tesseract OCR

### Installing Tesseract OCR

**Ubuntu/Debian:**
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
sudo apt-get install libtesseract-dev
```

**macOS:**
```bash
brew install tesseract
```

**Windows:**
Download the installer from [GitHub Tesseract releases](https://github.com/UB-Mannheim/tesseract/wiki) and add Tesseract to your system PATH.

## Installation

1. **Clone the repository:**
```bash
git clone https://github.com/MuhammedSinanHQ/Optical-Character-Recognition-using-Images.git
cd Optical-Character-Recognition-using-Images
```

2. **Create a virtual environment (recommended):**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install required dependencies:**
```bash
pip install -r requirements.txt
```

## Running the Application

### Local Development

1. **Start the Flask application:**
```bash
python app.py
```

2. **Open your web browser and navigate to:**
```
http://localhost:5000
```

3. **Using the application:**
   - Click "Choose Image" to upload an image file
   - Preview the uploaded image on the right side
   - Click "Extract Text" to process the image
   - View the extracted text on the left side

### Production Deployment

For production deployment on platforms like Heroku:

```bash
# The application uses the Procfile for deployment
web: gunicorn app:app
```

## Project Structure

```
Optical-Character-Recognition-using-Images/
├── app/
│   ├── __init__.py           # Flask app initialization
│   ├── views.py              # Routes and OCR logic
│   ├── templates/
│   │   └── index.html        # Main web interface
│   └── static/
│       └── style.css         # Styling
├── uploads/                   # Temporary upload directory (auto-created)
├── app.py                     # Application entry point
├── requirements.txt           # Python dependencies
├── Procfile                   # Deployment configuration
├── Optical_Character_Recognition_using_Images.ipynb  # Original notebook
└── README.md                  # This file
```

## How It Works

1. **Image Upload**: Users upload an image through the web interface
2. **Preprocessing Pipeline**:
   - Convert image to grayscale
   - Apply median blur to remove noise
   - Use adaptive thresholding to enhance text
   - Correct image skew using deskewing algorithm
3. **Text Extraction**: Tesseract OCR processes the preprocessed image
4. **Text Cleaning**: Remove unwanted special characters
5. **Display Results**: Show extracted text and image preview

## Technologies Used

- **Flask**: Web framework
- **OpenCV**: Image preprocessing
- **Tesseract**: OCR engine
- **NumPy**: Array operations
- **Pillow**: Image handling
- **Gunicorn**: Production WSGI server

## Troubleshooting

### Tesseract Not Found Error
If you encounter a "Tesseract not found" error, ensure Tesseract is installed and added to your system PATH.

### Image Upload Issues
Make sure the image file size is under 16MB and is in a supported format.

### Poor OCR Results
For best results:
- Use high-resolution images
- Ensure good contrast between text and background
- Avoid heavily skewed or rotated images
- Use clear, printed text rather than handwritten text

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Author

Muhammed Sinan

## Acknowledgments

- Based on the Optical Character Recognition using Images Jupyter notebook
- Uses Tesseract OCR engine developed by Google
