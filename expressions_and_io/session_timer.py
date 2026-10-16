#Gharam Alkaraki
#session_timer.py
# Description: Session Timer script that converts seconds into minutes and remaining seconds.
total_seconds = int(input("Session length in seconds: "))
minutes = total_seconds // 60
seconds = total_seconds % 60

print(f"Session length: {minutes} minutes and {seconds} seconds")
#لما ندخل 905اعطاني 15 دقيقه و 5 ثواني
