import time
phrase="python is the best coding language"
word_count=len(phrase.split())

print(f"types this fast : \n{phrase}\n")
input("press enter to start.")

start_time = time.time()
attempt=input("type here")
end_time=time.time()

time_taken= (end_time - start_time) /60
wpm=round(word_count/time_taken,2)

if attempt ==phrase:
    print(f"\n success ! your speed : {wpm} WPM")
else:
    print("\n nope. Try again")
