import write
def finalres():
    Quiz_res=int(write.read_file("quizcheck.txt"))
    Text_res=int(write.read_file("texttweet.txt"))
    Face_res=int(write.read_file("videocheck.txt"))
    Voice_res=int(write.read_file("voicecheck.txt"))
    print(Quiz_res)
    print(Text_res)
    print(Face_res)
    print(Voice_res)
    # max value is 4+2+2+2=10
    depressed_factor=Quiz_res+Text_res+Face_res+Voice_res
    if(depressed_factor<=2):
        result = 'Your Depression test result : No Depression'
    if(depressed_factor>2 and depressed_factor<=4):
        result = 'Your Depression test result : Mild Depression'
    if(depressed_factor>4 and depressed_factor<=6):
        result = 'Your Depression test result : Moderate Depression'
    if(depressed_factor>6 and depressed_factor<=8):
        result = 'Your Depression test result : Moderately severe Depression'
    if(depressed_factor>8 and depressed_factor<=10):
        result='Your Depression test result : Severe Depression'
    return result