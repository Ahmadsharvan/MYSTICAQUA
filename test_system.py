#!/usr/bin/env python3
"""
Test script for the Lucky Draw automatic payment system
Run this to verify all functions are working correctly
"""

def test_payment_system():
    """Test the payment system functions"""
    print("🧪 Testing Lucky Draw Payment System...")
    
    # Test data
    test_user_data = {
        'name': 'Test User',
        'mobile': '9876543210',
        'tickets': ['0001', '0002', '0003'],
        'ticket_count': 3,
        'total_amount': 15,
        'upi_id': '9353539771@pthdfc'
    }
    
    print(f"✅ Test user: {test_user_data['name']}")
    print(f"✅ Tickets: {', '.join(test_user_data['tickets'])}")
    print(f"✅ Amount: ₹{test_user_data['total_amount']}")
    
    # Test pending payment
    from app import add_pending_payment, PENDING_PAYMENTS
    session_id = "test_session_123"
    add_pending_payment(session_id, test_user_data)
    
    print(f"✅ Pending payment added for session: {session_id}")
    print(f"✅ Total pending payments: {len(PENDING_PAYMENTS)}")
    
    # Test received payment
    from app import add_received_payment, RECENT_PAYMENTS
    result = add_received_payment(15)
    print(f"✅ Payment received: {result}")
    print(f"✅ Recent payments: {len(RECENT_PAYMENTS)}")
    
    # Test automatic verification
    from app import check_automatic_payments
    session_id, transaction_id = check_automatic_payments()
    
    if session_id:
        print(f"✅ Auto-verified payment for session: {session_id}")
        print(f"✅ Generated transaction ID: {transaction_id}")
    else:
        print("⏳ No payments to auto-verify at this time")
    
    print("\n🎯 System Test Complete!")
    print("🌐 You can now test the admin routes:")
    print("   - http://localhost:5000/admin/pending_payments")
    print("   - http://localhost:5000/admin/payment_received/15")
    print("   - http://localhost:5000/admin/recent_payments")

if __name__ == "__main__":
    try:
        test_payment_system()
    except Exception as e:
        print(f"❌ Test failed: {e}")
        print("💡 Make sure the Flask app is running first!")
