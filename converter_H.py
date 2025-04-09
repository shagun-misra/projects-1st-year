import pywhatkit as pw
import textwrap
import os

def get_user_input():
    
    txt = input("Enter the text you want to convert into handwriting: ")
    if len(txt.strip()) == 0:
        print("Error: Text cannot be empty. Please enter some text.")
        return get_user_input()  # Recursively prompt the user until valid input
    return txt

def format_text(text, width=50):
    
    return textwrap.fill(text, width=width)

def choose_color():
    
    print("Choose a color for the handwriting:")
    print("1: Red")
    print("2: Green")
    print("3: Blue")
    print("4: Custom RGB")
    choice = input("Enter the number corresponding to the color: ").strip()
    
    if choice == '1':
        return [255, 0, 0]  # Red
    elif choice == '2':
        return [0, 255, 0]  # Green
    elif choice == '3':
        return [0, 0, 255]  # Blue
    elif choice == '4':
        return get_custom_color()  # Get a custom RGB color
    else:
        print("Invalid choice. Please choose a valid option.")
        return choose_color()

def get_custom_color():
    
    try:
        r = int(input("Enter the Red value (0-255): "))
        g = int(input("Enter the Green value (0-255): "))
        b = int(input("Enter the Blue value (0-255): "))
        
        if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
            print("Error: RGB values must be between 0 and 255. Try again.")
            return get_custom_color()
        
        return [r, g, b]
    except ValueError:
        print("Error: Please enter valid integer values between 0 and 255.")
        return get_custom_color()

def save_handwritten_text(image_path):
    
    if not os.path.exists(os.path.dirname(image_path)) and os.path.dirname(image_path) != '':
        print(f"Error: Directory does not exist. Saving to the current directory.")
        image_path = "my_handwritten_text.png"  # Default to current directory
    
    print(f"Saving the image as '{image_path}'...")
    return image_path

def main():
    
    # Get input text from the user
    txt = get_user_input()
    
    # Format the text to be wrapped
    wrapped_text = format_text(txt, width=50)
    
    # Choose the handwriting color
    color = choose_color()
    
    # Ask where to save the image
    image_path = input("Enter the image filename (e.g., 'my_handwritten_text.png'): ").strip()
    image_path = save_handwritten_text(image_path)
    
    # Generate handwriting image
    try:
        pw.text_to_handwriting(wrapped_text, image_path, color)
        print(f"Handwritten text has been saved as '{image_path}'.")
    except Exception as e:
        print(f"Error generating handwriting: {e}")

if __name__ == "__main__":
    main()
