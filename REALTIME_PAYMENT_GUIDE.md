# 🎯 Lucky Draw - Real-Time Payment Integration Guide

## 🔹 **What You've Got Now**

✅ **Real-time payment system** with Razorpay integration  
✅ **WebSocket support** for instant payment confirmation  
✅ **Automatic booking completion** when payment is received  
✅ **Darker background** on all pages  
✅ **Professional payment interface** with status tracking

## 🔹 **How It Works (Real-Time Flow)**

1. **User selects tickets** → **Clicks "Proceed to Payment"**
2. **Razorpay order created** → **Payment page shows with real-time status**
3. **User clicks "Pay"** → **Razorpay payment window opens**
4. **User completes payment** → **WebSocket instantly confirms payment**
5. **Booking automatically completed** → **Success page shown**
6. **Data saved to Excel** → **Tickets marked as booked**

## 🔹 **What You Need to Do**

### **Step 1: Create Razorpay Account**

1. **Go to**: [razorpay.com](https://razorpay.com)
2. **Sign up** as a business account
3. **Complete KYC verification**:
   - Business PAN Card
   - Bank Account Details
   - Business Address Proof
   - Business Registration (if applicable)
4. **Get API Keys**:
   - Go to Settings → API Keys
   - Copy your **Key ID** and **Key Secret**

### **Step 2: Configure the Application**

1. **Open**: `lucky_draw/app_realtime.py`
2. **Replace these lines**:
   ```python
   RAZORPAY_KEY_ID = "rzp_test_YOUR_KEY_ID"  # Replace with your Key ID
   RAZORPAY_KEY_SECRET = "YOUR_KEY_SECRET"    # Replace with your Key Secret
   ```

### **Step 3: Set Up Webhooks (For Production)**

1. **In Razorpay Dashboard** → **Settings** → **Webhooks**
2. **Add webhook URL**: `http://your-domain.com/razorpay_webhook`
3. **Select events**: `payment.captured`
4. **Copy webhook secret** and add to your code

### **Step 4: Run the Application**

```bash
# Install dependencies
pip install -r requirements.txt

# Run the real-time payment system
python app_realtime.py
```

## 🔹 **Files Created/Modified**

### **New Files:**

- `app_realtime.py` - Main application with real-time payments
- `templates/payment_realtime.html` - Real-time payment page
- `setup_realtime_payment.bat` - Setup script
- `requirements.txt` - Updated with new dependencies

### **Modified Files:**

- All template files - **Darker background** applied
- `requirements.txt` - Added WebSocket and Razorpay packages

## 🔹 **Features Included**

### **Real-Time Payment Features:**

- ✅ **Instant payment confirmation** via WebSockets
- ✅ **Live payment status** updates
- ✅ **Automatic booking completion**
- ✅ **Razorpay integration** with UPI support
- ✅ **Webhook handling** for server-side confirmation
- ✅ **Fallback manual payment** system

### **UI/UX Features:**

- ✅ **Darker, warmer background** on all pages
- ✅ **Animated payment status** indicators
- ✅ **Real-time status messages**
- ✅ **Professional payment interface**
- ✅ **Mobile-responsive design**

### **Admin Features:**

- ✅ **Complete admin dashboard**
- ✅ **Real-time payment monitoring**
- ✅ **Data export and reset**
- ✅ **Booking management**

## 🔹 **Testing the System**

### **Test Mode (Development):**

1. Use Razorpay test keys (start with `rzp_test_`)
2. Use test UPI numbers for payment
3. All features work exactly like production

### **Production Mode:**

1. Use live Razorpay keys (start with `rzp_live_`)
2. Real payments will be processed
3. Webhooks will confirm payments automatically

## 🔹 **Payment Flow Example**

```
User Flow:
1. Enter name & mobile → Select tickets → Click "Proceed to Payment"
2. See payment page with order details
3. Click "Pay ₹X" → Razorpay window opens
4. Complete payment → Instant confirmation
5. See success message → Booking completed

Admin Flow:
1. Monitor payments in real-time
2. View all bookings in admin dashboard
3. Export data to Excel
4. Reset system for new lucky draw
```

## 🔹 **Security Features**

- ✅ **Payment signature verification**
- ✅ **Webhook signature validation**
- ✅ **Session-based user tracking**
- ✅ **Secure API key handling**
- ✅ **Input validation and sanitization**

## 🔹 **Next Steps**

1. **Get your Razorpay API keys** (most important!)
2. **Configure the keys** in `app_realtime.py`
3. **Test with test keys** first
4. **Deploy to production** with live keys
5. **Set up webhooks** for automatic confirmation

## 🔹 **Support**

If you need help:

1. Check Razorpay documentation
2. Verify API keys are correct
3. Check webhook configuration
4. Monitor server logs for errors

---

**🎉 Your Lucky Draw system now has professional real-time payment integration!**
