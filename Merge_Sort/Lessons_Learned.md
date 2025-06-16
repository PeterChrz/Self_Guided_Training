#Lessons Learned
//Document findings from hands practice.
#### Python Power
I never appreciated how much Python abstracts away from users through lists, we get dynamic arrays and high-level data manipulation all built in. These features I had to manually add in to my FreePascal code when looking to collect user input to build a list to sort.
The advantage Pascal gains from this being a manual process is better memory managment, arrays are fixed sized. I was able to create a dynamic array object when initially receiving user input, but once complete I copy that into a fixed size array and release the memory of the dynamic array. I'm sure that with scale this brings a huge benefit for FreePascal programs. 
