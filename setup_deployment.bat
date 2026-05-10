@echo off
echo ========================================
echo 🚀 Lucky Draw Website - Deployment Setup
echo ========================================
echo.

echo 📋 This script will help you prepare your website for deployment
echo.

echo 🔧 Step 1: Check if Git is installed...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Git is not installed. Please install Git first:
    echo    Download from: https://git-scm.com/downloads
    pause
    exit /b 1
)
echo ✅ Git is installed

echo.
echo 📁 Step 2: Initialize Git repository...
if not exist .git (
    git init
    echo ✅ Git repository initialized
) else (
    echo ✅ Git repository already exists
)

echo.
echo 📝 Step 3: Add all files to Git...
git add .
echo ✅ Files added to Git

echo.
echo 💾 Step 4: Create initial commit...
git commit -m "Initial commit - Lucky Draw Website with Real-time Payments"
echo ✅ Initial commit created

echo.
echo ========================================
echo 🎉 Setup Complete!
echo ========================================
echo.
echo 📋 Next Steps:
echo    1. Create a GitHub repository
echo    2. Run these commands:
echo       git remote add origin https://github.com/YOUR_USERNAME/lucky-draw-website.git
echo       git push -u origin main
echo    3. Deploy to Render/Railway using the DEPLOYMENT_GUIDE.md
echo.
echo 📖 For detailed instructions, see: DEPLOYMENT_GUIDE.md
echo.
pause
