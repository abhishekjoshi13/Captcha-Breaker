import os
import subprocess
import sys

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result.returncode, result.stdout, result.stderr
    except subprocess.CalledProcessError as e:
        return e.returncode, e.stdout, e.stderr

def test_full_project():
    print("Testing CAPTCHA Breaker Project...")
    print("=" * 50)
    
    print("1. Checking requirements...")
    returncode, stdout, stderr = run_command("pip install -r requirements.txt")
    if returncode == 0:
        print("Requirements installed successfully")
    else:
        print("Failed to install requirements")
        return
    
    print("\n2. Generating CAPTCHA images...")
    returncode, stdout, stderr = run_command("python utils.py")
    if returncode == 0:
        print("CAPTCHA images generated successfully")
        
        images = [f for f in os.listdir('captcha_images') if f.endswith('.png')]
        print(f"Generated {len(images)} CAPTCHA images")
    else:
        print("Failed to generate CAPTCHA images")
        return
    
    print("\n3. Training the model...")
    print("This may take a few minutes...")
    returncode, stdout, stderr = run_command("python train.py")
    if returncode == 0:
        print("Model trained successfully")
    else:
        print("Training failed or was interrupted")
    
    print("\n4. Testing predictions...")
    returncode, stdout, stderr = run_command("python predict.py")
    if returncode == 0:
        print("Prediction test completed")
    else:
        print("Prediction test failed")
    
    print("\n" + "=" * 50)
    print("Project testing completed!")
    print("\nTo test manually:")
    print("1. python utils.py  (regenerate images)")
    print("2. python train.py  (retrain model)") 
    print("3. python predict.py (test predictions)")

if __name__ == "__main__":
    test_full_project()
