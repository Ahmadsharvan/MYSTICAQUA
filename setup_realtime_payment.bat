@echo off
echo ========================================
echo 🎯 Lucky Draw - Real-Time Payment Setup
echo ========================================
echo.

echo 📦 Installing required packages...
pip install -r requirements.txt

echo.
echo 🔑 Setting up Razorpay Integration...
echo.
echo ⚠️  IMPORTANT: You need to configure Razorpay API keys
echo.
echo 📋 Steps to get Razorpay API keys:
echo    1. Go to https://razorpay.com
echo    2. Sign up as a business account
echo    3. Complete KYC verification
echo    4. Go to Settings > API Keys
echo    5. Copy your Key ID and Key Secret
echo.
echo 🔧 Configuration needed:
echo    - Open app_realtime.py
echo    - Replace RAZORPAY_KEY_ID with your Key ID
echo    - Replace RAZORPAY_KEY_SECRET with your Key Secret
echo.
echo 🌐 Webhook Configuration:
echo    - In Razorpay Dashboard > Settings > Webhooks
echo    - Add webhook URL: http://your-domain.com/razorpay_webhook
echo    - Select events: payment.captured
echo.
echo 🚀 Starting the application...
echo.
python app_realtime.py

pause
